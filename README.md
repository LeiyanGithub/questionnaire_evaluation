# 人工评价指引

### 1. 快速开始

1) 输入 annotation id， 点击'Start'按钮开始评价,一共100条数据，需要为3个不同的模型进行打分，按照不同的指标
2) 给出 6 个评分，点击'Submit'按钮

### 2. 问卷评价任务简介

给定一个主题，围绕该主题生成问卷，评价问卷的质量。

---

### 3. 评价指标

<img width="70%" alt="image" src="https://github.com/LeiyanGithub/questionnaire_evaluation/assets/45895439/f02bcaef-a130-4593-90cf-5f02eddcd967">

人工评价中考虑 8 个方面的文本质量，分数都是越高越好。

- **1. 背景调查Background问题数量**
受访者的背景直接关系问卷的结论，比如说主题是调研老年人使用电子设备情况，由于线上问卷，无法准确约束填写对象，因此有可能是年轻人填写，因此，需要做个人信息调查。一份高质量问卷应该包含用户背景调查、用户行为调查、用户态度调查。
填写背景调查问题个数，例如：姓名/性别/专业等
<img width="80%" alt="image" src="https://github.com/LeiyanGithub/questionnaire_evaluation/assets/45895439/13f2ef6c-550d-4f1e-9086-92e627565821">


- **2. 具体度Specificity（1-5）**: 问卷整体问题的具体程度。
一份高质量的问卷中的问题应该是具体清晰的，而不应该是抽象宏观的。
> 举例说明：

<img width="90%" alt="image" src="https://github.com/LeiyanGithub/questionnaire_evaluation/assets/45895439/175cd99f-3e99-4145-af99-96598bd4ebb8">

| 评分 | 标准                                        |
| ---- | ------------------------------------------- |
| 5    | 所有句子都非常具体.                             |
| 3    | 大约一半的句子具体.                           |
| 1    | 所有句子很抽象，无法具体到细节.              |


- **3. 相关性Relevance（1-5）**: 问卷中问题与主题不相关的比例
> 举例说明：
<img width="80%" alt="image" src="https://github.com/LeiyanGithub/questionnaire_evaluation/assets/45895439/39b098ed-0aad-4763-a7a4-32cf9f5ab1ea">

| 评分 | 标准                         |
| ---- | ---------------------------- |
| 5    | 几乎没有不相关问题.  |
| 3    | 大约一半以上的问题都不相关。|
| 1    | 问题都完全不相关。 |

- **4. 顺序合理性Order（1-5）**: 问卷中问题顺序合理性
举例说明：
<img width="80%" alt="image" src="https://github.com/LeiyanGithub/questionnaire_evaluation/assets/45895439/ab30011f-2aec-4759-9998-e00e7a51b7c1">
<img width="80%" alt="image" src="https://github.com/LeiyanGithub/questionnaire_evaluation/assets/45895439/a7424b02-8289-4ada-8803-870130f8c814">
<img width="80%" alt="image" src="https://github.com/LeiyanGithub/questionnaire_evaluation/assets/45895439/b8d420d5-9694-41be-92bc-8fc7f78e9fec">


| 评分 | 标准                         |
| ---- | ---------------------------- |
| 5    | 问题逻辑流畅.  |
| 3    | 问题顺序需要部分调整。|
| 1    | 问题顺序严重不合理，阅读困难。 |

- **5. 选项合理性Rationality（1-5）**: 问卷中选项与问题不匹配、不互斥、不完备
> 举例说明：
<img width="80%" alt="image" src="https://github.com/LeiyanGithub/questionnaire_evaluation/assets/45895439/66ffc3fb-9daa-4e18-ab79-a1f30da33c4a">

| 评分 | 标准                                 |
| ---- | ------------------------------------ |
| 5    | 几乎没有不合理的选项设置.   |
| 3    | 大约一半以上问题对应的选项都不合理  |
| 1    | 严重不合理。  |

- **6. 数据差异化Distinction（1-5）**: 问卷整体问题的具体程度。
> 举例说明：
<img width="80%" alt="image" src="https://github.com/LeiyanGithub/questionnaire_evaluation/assets/45895439/7aedc4e4-38ac-4bd7-b6c6-779a80ecdb07">

| 评分 | 标准                                        |
| ---- | ------------------------------------------- |
| 5    | 所有问题对应的选项对应的填写结果尽可能满足正态分布.                             |
| 3    | 大约一半的问题以及选项能够符合正态分布.                           |
| 1    | 所有问题几乎选项偏差大.              |

- **7. 流畅性Fluency（1-5）**: 问卷中句子流畅可读程度比例。
> 举例说明：

| 评分 | 标准                                        |
| ---- | ------------------------------------------- |
| 5    | 所有句子都流畅.                             |
| 3    | 大约一半的句子都流畅.                           |
| 1    | 所有句子都难以阅读.              |

- **8. 非重复度Non-Repetition（1-5）**: 问卷中句子重复比例。
<img width="707" alt="image" src="https://github.com/LeiyanGithub/questionnaire_evaluation/assets/45895439/4fcffff4-5871-4e31-b765-16959692604b">

举例说明：

| 评分 | 标准                           |
| ---- | ------------------------------ |
| 5    | 几乎没有重复.   |
| 3    | 大约一半以上的句子都出现重复。   |
| 1    | 重复严重。|

# High-level

- **整体质量（排序）**: 高质量->低质量: 2 0 1
