人工评价指引

### 快速开始
1. 输入annotation id， 点击'Start'按钮开始评价
2. 给出6个评分，点击'Submit'按钮

### 问卷评价任务简介
**问卷评价描述**
给定一个主题，围绕该主题生成问卷，让受访者填写。

### 评价指标
人工评价中考虑6个方面的文本质量。

**流畅性（1-5）**: 问卷中句子流畅可读程度比例。

常见的不流畅情况：
1) 句子读不通 ：您认为大学生是否认为自己所以不会做网上课？
2) 句子有歧义 ：您觉得自己的生活费还有盈利？

举例说明：
5: 
4:
3:
2:
1: 


| 评分 | 标准                                                          |
|-------|-------------------------------------------------------------------|
| 5     | 所有句子都流畅.                                         |
| 4     | 大多数句子都流畅, 只有少数句子有问题.                  |
| 3     | 大约一半的句子都流畅.                           |
| 2     | 大多数句子都难以阅读, 只有少数句子可以阅读. |
| 1     | 所有句子都难以阅读.                                   |


**多样性（1-5）**: 问卷中句子重复比例。计算方式（独特的问题）/总问题数

举例说明：
5:
4:
3:
2:
1:


| 评分 | 标准                                                                             |
|-------|--------------------------------------------------------------------------------------|
| 5     | 几乎没有重复.       |
| 4     | 存在个别重复句子。       |
| 3     | 大约一半以上的句子都出现重复。 |
| 2     | 大多数句子重复，只有少数多样。 |
| 1     | 重复严重。         |


**相关性（1-5）**: 问卷中问题与主题不相关的比例
举例说明：
5:
4:
3:
2:
1:

| 评分 | 标准                                                                             |
|-------|--------------------------------------------------------------------------------------|
| 5     | 几乎没有不相关问题.       |
| 4     | 存在不相关问题。       |
| 3     | 大约一半以上的问题都不相关。 |
| 2     | 大多数问题不相关。 |
| 1     | 问题都完全不相关。         |


**合理性（1-5）**: 问卷中选项与问题不匹配、不互斥、不完备
举例说明：
5:
4:
3:
2:
1:

| 评分 | 标准                                                                             |
|-------|--------------------------------------------------------------------------------------|
| 5     | 几乎没有不合理的选项设置.       |
| 4     | 存在个别不合理的选项设置。       |
| 3     | 大约一半以上问题对应的选项都不合理。 |
| 2     | 大多数问题对应的选项不合理。 |
| 1     | 严重不合理。         |


**信息量（1-5）**: 问卷中每个问题应该都是有价值的，当受访者填写完之后，要么能够得到统计表，要么能得到结论，如果填写之后没有收获，则任务信息量为0，统计有信息量问题个数
举例说明：
5:
4:
3:
2:
1:
| 评分 | 标准                                                                             |
|-------|--------------------------------------------------------------------------------------|
| 5     | 几乎所有问题都有信息量.       |
| 4     | 少数问题没有意义。       |
| 3     | 大约1/3的问题有价值。 |
| 2     | 少数问题有意义。 |
| 1     | 几乎没有有价值的问题。         |

**支撑度（1-5）**: 问卷中的问题是否能够支撑主题，满足调研目标
举例说明：
yes:
no:

| 评分 | 标准                                                                             |
|-------|--------------------------------------------------------------------------------------|
| yes     | 能够满足调查需求.       |
| no     | 不能满足调研需求。       |


