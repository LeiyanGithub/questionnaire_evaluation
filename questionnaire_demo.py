import datetime
import json
import random
from pathlib import Path

import pandas as pd
import gradio as gr
import jsonlines
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

CURRENT_DIR = Path(__file__).parent
TEST_SAMPLES_FILE = CURRENT_DIR / "vtt_test.jsonl"
TEST_RESULTS_FILE = CURRENT_DIR / "human_test_results.jsonl"
RESULT_DIR = Path("./data/human_evaluation")
RESULT_DIR.mkdir(exist_ok=True, parents=True)
REPEAT = 2
MAX_IMAGES_ROW = 6

MODEL_LIST = ['human', 'chatglm-6', 'chatgpt']

ORDER_LIST = {}


# MODEL_LIST = [{"model": "chatglm-6", "url": "https://docs.google.com/spreadsheets/d/1XErn55RW4-6UUN_Lpo-usB6wN_GZ_DBi-_7KZrJgH4g/edit#gid=0"},
#               {"model": "chatgpt", "url": "https://docs.google.com/spreadsheets/d/1oMo7TTybTk2Ly18EQgGoiOEfx-IiF_kfPB679CPNBwY/edit#gid=861815217"},
#               {"model": "human", "url": "https://docs.google.com/spreadsheets/d/12nBl8qO_KOPwIskZtSH6U14eBrImzyf_Szao-SKqS3w/edit#gid=1331716189"}]
# # ORDER_LIST = {'1': }

# URL = "https://docs.google.com/spreadsheets/d/1XErn55RW4-6UUN_Lpo-usB6wN_GZ_DBi-_7KZrJgH4g/edit?usp=sharing"
# csv_url = URL.replace('/edit#gid=', '/export?format=csv&gid=')

MODE = "EN"

if MODE == "EN":
    TITLE = "Human Evaluation for Questtionnaires"
    START_TEXT = "Start / Jump"
    NEXT_TEXT = "Next"
    SKIP_TEXT = "Cannot Decide"
    SUBMIT_TEXT = "Submit"
    BACKGROUND_TEXT = 'Background 背景调查数量,如姓名，年龄等'
    SPECIFICITY_TEXT = 'Specificity 问卷问题具体程度。5分代表非常清晰具体，1分代表特别抽象'
    RELEVANCE_TEXT = "Relevance 问卷中问题相关的程度 5分代表绝大部分问题都非常相关，1分代表绝大部分问题与主题不相关"
    ORDER_TEXT = "Order 问卷中问题顺序合理性，5分代表无需调整，3分代表部分问题需要调整顺序，1分代表问题顺序特别乱"
    RATIONALITY_TEXT = 'Rationality 问卷中选项不合理的比例， 5分代表选项设置非常不合理，1分代表选项非常合理]'
    DISTINCTOIN_TEXT = 'Distinction 问卷中的废话问题的比例，5分代表问题都非常有价值，有必要，1分代表即使填写问题，统计数据不符合正态分布'
    FLUENCY_TEXT = "Fluency 问卷中问题流畅程度 5分代表流畅度最高，1分代表不流畅]"
    NON_REPETITION_TEXT = 'Non-Repetition 问卷中问题重复问题出现比例 5分代表问题几乎没有重复，1分代表重复严重]'
    
    RANK_TEXT = '排序 按照 0 1 2格式'

    # OVERAL_RANK = 'quality'
    # SUPPORT_TEXT = 'support'
    QUESTIONNAIRE_TEXT = "Questionnaire"
    TOPIC_TEXT = "Topic"
    START_TIME_TEXT = "Start Time"
    LAST_COST_TIME_TEXT = "Last Sample Cost Time (s)"
    GUIDELINE_TEXT = "Guideline"
    COMPLETED_ANNOTATIONS_TEXT = "Completed Annotations"
    REFRESH_TEXT = "Refresh"
elif MODE == "CN":
    TITLE = "人工评估 问卷"
    START_TEXT = "开始 / 跳转"
    NEXT_TEXT = "下一个"
    SKIP_TEXT = "无法决定"
    SUBMIT_TEXT = "提交"
    FLUENCY_TEXT = "流畅度"
    RELEVANCE_TEXT = "相关性"
    LOGICAL_SOUNDNESS_TEXT = "逻辑性"
    CATEGORY_TEXT = "类别"
    TOPIC_TEXT = "主题"
    START_TIME_TEXT = "开始时间"
    LAST_COST_TIME_TEXT = "上一样本耗时 (秒)"
    GUIDELINE_TEXT = "指南"
    COMPLETED_ANNOTATIONS_TEXT = "已完成标注"
    REFRESH_TEXT = "刷新"

results = {}

with jsonlines.open(TEST_SAMPLES_FILE) as reader:
    samples = list(reader)

for model_name in MODEL_LIST:
    with jsonlines.open('./dataset/' + model_name + '.jsonl') as reader:
        results[model_name] = list(reader)[0]


def get_sample(annotation_id):
    validate_annotation_id(annotation_id)
    random.shuffle(MODEL_LIST)
    for index in range(len(MODEL_LIST)):
        ORDER_LIST[index] = MODEL_LIST[index]
    samples = []
    for model_name in MODEL_LIST:
        samples.append(results[model_name][annotation_id])
    
    # 记录全局顺序
    return samples


def get_questionnaire(annotation_id):
    samples = get_sample(annotation_id)
    questionnaires = [_sample['answer'] for _sample in samples]
    return samples[0]['topic'], questionnaires


def save_result(annotation_id, model_name, info):
    # result = results[annotation_id]
    # result.update(info)
    for id in range(len(MODEL_LIST)):
        with open(RESULT_DIR / f"{model_name}/human_{annotation_id}.json", "w") as f:
            json.dump(info, f, ensure_ascii=False)


def try_read_history(annotation_id):
    paths = [RESULT_DIR / f"{model_name}/human_{annotation_id}.json" for model_name in MODEL_LIST]
    print("paths: ", paths)
    questionnaires, model_rank_names, background, specificity, relevance, order, rationality, distinction, fluency, non_Repetition = [], [], [], [], [], [], [], [], [], []
    flag = False
    for path in paths:
        if path.exists():
            with open(path) as f:
                data = json.load(f)
            # print("data: ", data)
            questionnaires.append(data['questionnaire'])
            model_rank_names.append(data['model_rank_name'])
            background.append(data['background'])
            specificity.append(data['specificity'])
            relevance.append(data['specificity'])
            order.append(data['order'])
            rationality.append(data['rationality'])
            distinction.append(data['distinction'])
            fluency.append(data['fluency'])
            non_Repetition.append(data['non_repetition'])
            flag = True
        else:
            questionnaires.append(None)
            model_rank_names.append(None)
            background.append(None)
            specificity.append(None)
            relevance.append(None)
            order.append(None)
            rationality.append(None)
            distinction.append(None)
            fluency.append(None)
            non_Repetition.append(None)
    # print(fluencys + diversities + relevances + rationalities + qualityes + supportes)
    return flag, questionnaires, model_rank_names, background + specificity + relevance + order + rationality + distinction + fluency + non_Repetition


def get_time_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def validate_annotation_id(annotation_id):
    annotation_id = max(0, min(int(annotation_id), len(results[MODEL_LIST[0]]) - 1))
    return annotation_id


def start(annotation_id):
    annotation_id = validate_annotation_id(annotation_id)
    topic, questionnaires = get_questionnaire(annotation_id)
    flag, questionnaires_saved, model_rank_names, datas = try_read_history(annotation_id)
    # print("questionnaires_saved: ", questionnaires_saved)
    # print("datas: ", datas)
    
    if flag:
        return (annotation_id, topic, model_rank_names) + tuple(questionnaires_saved) + tuple(datas)
    print(datas)
    return (annotation_id, topic, 0) + tuple(questionnaires) + tuple(datas)


def next_sample(annotation_id):
    annotation_id = validate_annotation_id(annotation_id + 1)
    topic, questionnaire = get_questionnaire(annotation_id)
    flag, model_rank_names, questionnaires_saved, datas = try_read_history(annotation_id)
    print(datas)
    if flag:
        return (annotation_id, get_time_now(), topic, model_rank_names, questionnaires_saved, datas)
        
    return (annotation_id, get_time_now(), topic, [], questionnaire, datas)


def submit(annotation_id, model_rank, questionnaire_0, questionnaire_1, questionnaire_2, background_0, background_1, background_2, specificity_0, specificity_1, specificity_2, relevance_0, relevance_1, relevance_2, order_0, order_1, order_2, rationality_0, rationality_1, rationality_2, distinction_0, distinction_1, distinction_2, fluency_0, fluency_1, fluency_2, non_repetition_0, non_repetition_1, non_repetition_2):
    annotation_id = validate_annotation_id(annotation_id)
    # time_now = get_time_now()
    # duration = (
    #     datetime.datetime.strptime(time_now, "%Y-%m-%d %H:%M:%S")
    #     - datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    # ).seconds

        # print(exec('fluency_{index}'.format(index)))
    print("model_rank: ", model_rank, "len: ", len(model_rank))
    if len(model_rank)<7:
        model_rank_name = " ".join([ORDER_LIST[int(id)] for id in model_rank.split(' ')])
        
        print("model_rank_name: ", model_rank_name)
    else:
        model_rank_name = model_rank
    save_result(
        annotation_id,
        ORDER_LIST[0],
        {
            "questionnaire": questionnaire_0,
            "model_rank_name": model_rank_name,
            "background": background_0,
            "specificity": specificity_0,
            "relevance": relevance_0,
            "order": order_0,
            "rationality": rationality_0,
            "distinction": distinction_0,
            "fluency": fluency_0,
            "non_repetition": non_repetition_0,
        },
    )

    save_result(
        annotation_id,
        ORDER_LIST[1],
        {
            "questionnaire": questionnaire_1,
            "model_rank_name": model_rank_name,
            "background": background_1,
            "specificity": specificity_1,
            "relevance": relevance_1,
            "order": order_1,
            "rationality": rationality_1,
            "distinction": distinction_1,
            "fluency": fluency_1,
            "non_repetition": non_repetition_1,
        },
    )

    save_result(
        annotation_id,
        ORDER_LIST[2],
        {
            "questionnaire": questionnaire_2,
            "model_rank_name": model_rank_name,
            "background": background_2,
            "specificity": specificity_2,
            "relevance": relevance_2,
            "order": order_2,
            "rationality": rationality_2,
            "distinction": distinction_2,
            "fluency": fluency_2,
            "non_repetition": non_repetition_2,
        },
    )

    annotation_id = validate_annotation_id(annotation_id + 1)
    topic, questionnaires = get_questionnaire(annotation_id)

    flag, model_rank_name, questionnaires_saved, datas = try_read_history(annotation_id)
    if flag:
        return (annotation_id, topic) + tuple(model_rank_name) + tuple(questionnaires_saved) + tuple(datas)

    return (annotation_id, topic, 0) + tuple(questionnaires) + tuple(datas)

def update_completed_annotations():
    path_list = list(RESULT_DIR.glob("human_*.json"))
    completed_annotations = sorted(
        [int(x.stem.split("_")[1]) for x in path_list]
    )
    complete_str = ""
    pre = None
    tmp_str = ""
    for x in completed_annotations:
        if pre is None:
            complete_str += f"{x}"
        elif x > pre + 1:
            complete_str += tmp_str
            complete_str += f", {x}"
            tmp_str = ""
        else:
            tmp_str = f"-{x}"
        pre = x
    complete_str += tmp_str

    return complete_str


def main():

    with gr.Blocks(title="Questionnaire Evaluation") as demo:
        gr.Markdown(f"## {TITLE}")

        with gr.Row():
            annotation_id = gr.Number(label="Annotation ID")
            model_rank = gr.Textbox(lines=1, label="Model Rank", interactive=True)
            topic = gr.Text(label=TOPIC_TEXT, interactive=True)
            with gr.Row():
                start_button = gr.Button(START_TEXT)
                next_button = gr.Button(NEXT_TEXT)

        # questionnaires, fluencys, diversities, relevances, rationalities, qualityes, supports = [], [], [], [], [], [], []
        
        id = 0
        with gr.Tab(f"Model_{id}"):
            with gr.Row():
                questionnaire_0 = gr.Textbox(lines=40, label=QUESTIONNAIRE_TEXT, interactive=True)
                with gr.Column():
                    background_0 = gr.Textbox(lines=1, label=BACKGROUND_TEXT, interactive=True)

                    specificity_0 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=SPECIFICITY_TEXT, interactive=True
                        )
                    relevance_0 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=RELEVANCE_TEXT, interactive=True
                        )
                    order_0 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=ORDER_TEXT, interactive=True
                        )
                    rationality_0 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=RATIONALITY_TEXT, interactive=True
                        )
                    distinction_0 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=DISTINCTOIN_TEXT, interactive=True
                        )
                    fluency_0 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=FLUENCY_TEXT, interactive=True
                        )
                    non_repetition_0 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=NON_REPETITION_TEXT, interactive=True
                        )
        
        id += 1
        with gr.Tab(f"Model_{id}"):
            with gr.Row():
                questionnaire_1 = gr.Textbox(lines=40, label=QUESTIONNAIRE_TEXT, interactive=True)
                with gr.Column():

                    background_1 = gr.Textbox(lines=1, label=BACKGROUND_TEXT, interactive=True)

                    specificity_1 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=SPECIFICITY_TEXT, interactive=True
                        )
                    relevance_1 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=RELEVANCE_TEXT, interactive=True
                        )
                    order_1 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=ORDER_TEXT, interactive=True
                        )
                    rationality_1 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=RATIONALITY_TEXT, interactive=True
                        )
                    distinction_1 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=DISTINCTOIN_TEXT, interactive=True
                        )
                    fluency_1 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=FLUENCY_TEXT, interactive=True
                        )
                    non_repetition_1 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=NON_REPETITION_TEXT, interactive=True
                        )
        id += 1
        with gr.Tab(f"Model_{id}"):
            with gr.Row():
                questionnaire_2 = gr.Textbox(lines=40, label=QUESTIONNAIRE_TEXT, interactive=True)
                with gr.Column():

                    background_2 = gr.Textbox(lines=1, label=BACKGROUND_TEXT, interactive=True)

                    specificity_2 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=SPECIFICITY_TEXT, interactive=True
                        )
                    relevance_2 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=RELEVANCE_TEXT, interactive=True
                        )
                    order_2 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=ORDER_TEXT, interactive=True
                        )
                    rationality_2 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=RATIONALITY_TEXT, interactive=True
                        )
                    distinction_2 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=DISTINCTOIN_TEXT, interactive=True
                        )
                    fluency_2 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=FLUENCY_TEXT, interactive=True
                        )
                    non_repetition_2 = gr.Radio(
                        choices=["1", "2", "3", "4", "5"], label=NON_REPETITION_TEXT, interactive=True
                        )
                # questionnaires += [questionnaire_0, questionnaire_1, questionnaire_2]
                # fluencys += [fluency_0, fluency_1, fluency_2]
                # diversities += [diversity_0, diversity_1, diversity_2]
                # relevances += [relevance_0, relevance_1, relevance_2]
                # rationalities += [rationality_0, rationality_1, rationality_2]
                # qualityes += [objectivity_0, objectivity_1, objectivity_2]
                # supports += [informativess_0, informativess_1, informativess_2]

        # with gr.Row():
        #     start_time = gr.Text(label=START_TIME_TEXT)
        #     last_duration = gr.Text(label=LAST_COST_TIME_TEXT)
        
    
        # with gr.Tab(GUIDELINE_TEXT):
        #     if MODE == "CN":
        #         GUIDE_FILE = CURRENT_DIR / "guideline_cn.md"
        #     else:
        #         GUIDE_FILE = CURRENT_DIR / "guideline.md"

        #     with open(GUIDE_FILE) as f:
        #         guideline = f.readlines()
        #     gr.Markdown("")
        #     gr.Markdown("".join(guideline))
        
        # with gr.Tab(COMPLETED_ANNOTATIONS_TEXT):
        #     refresh_button = gr.Button(REFRESH_TEXT)
        #     completed_annotations = gr.Text(label=COMPLETED_ANNOTATIONS_TEXT)

        # refresh_button.click(
        #     update_completed_annotations, outputs=[completed_annotations]
        # )
        
        start_button.click(
            start,
            inputs=[annotation_id],
            outputs=[
                annotation_id,
                topic,
                model_rank,
                questionnaire_0,
                questionnaire_1,
                questionnaire_2,
                background_0,
                background_1,
                background_2,
                specificity_0,
                specificity_1,
                specificity_2,
                relevance_0,
                relevance_1,
                relevance_2,
                order_0,
                order_1,
                order_2,
                rationality_0,
                rationality_1,
                rationality_2,
                distinction_0,
                distinction_1,
                distinction_2,
                fluency_0,
                fluency_1,
                fluency_2,
                non_repetition_0,
                non_repetition_1,
                non_repetition_2
            ]
        )

        next_button.click(
            submit,
            inputs=[
                annotation_id,
                model_rank,
                questionnaire_0,
                questionnaire_1,
                questionnaire_2,
                background_0,
                background_1,
                background_2,
                specificity_0,
                specificity_1,
                specificity_2,
                relevance_0,
                relevance_1,
                relevance_2,
                order_0,
                order_1,
                order_2,
                rationality_0,
                rationality_1,
                rationality_2,
                distinction_0,
                distinction_1,
                distinction_2,
                fluency_0,
                fluency_1,
                fluency_2,
                non_repetition_0,
                non_repetition_1,
                non_repetition_2
            ],
            outputs=[
                annotation_id,
                topic,
                model_rank,
                questionnaire_0,
                questionnaire_1,
                questionnaire_2,
                background_0,
                background_1,
                background_2,
                specificity_0,
                specificity_1,
                specificity_2,
                relevance_0,
                relevance_1,
                relevance_2,
                order_0,
                order_1,
                order_2,
                rationality_0,
                rationality_1,
                rationality_2,
                distinction_0,
                distinction_1,
                distinction_2,
                fluency_0,
                fluency_1,
                fluency_2,
                non_repetition_0,
                non_repetition_1,
                non_repetition_2
            ],
        )

    demo.launch()
    # demo.launch(server_name="0.0.0.0", share=True)


if __name__ == "__main__":
    main()
