'''
    混淆矩阵
        概述：用于展示真实值和预测值之间  正例和反例的情况
        模型：会用分类少的样本当作正例
        混淆矩阵名称：
                        预测值（正例）         预测值（反例）
        真实值（正例）     真正例（TP）           伪反例（FN）
        真实值（反例）     伪正例（FP）           真反例（TN）
    逻辑回归评估方式：
        精确率：
            预测正确的/样本总数
            tp/(tp+fp)
        召回率：
            tp/(tp+fn)
        f1值：
            (2*精确率*召回率) /(精确率+召回率)
'''

import pandas as pd
#                               混淆矩阵           精确率          召回率         f1值
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

from sklearn.metrics import roc_auc_score



# 2.定义数据集 样本集10样本       手动指定：恶性 正例      良性 反例
y_train = ['恶性', '恶性', '恶性', '恶性', '恶性', '恶性', '良性', '良性', '良性', '良性']

# 定义标签名     标签1代表正样本（正例）        标签2代表负样本（反例）
label = ['恶性', '良性']
df_label = ['恶性(正例)', '良性(反例)']

y_pre_A = ['恶性', '恶性', '恶性', '良性', '良性', '良性', '良性', '良性', '良性', '良性']

# cm_A = confusion_matrix(y_train, y_pre_A)
cm_A = confusion_matrix(y_train, y_pre_A, labels=label)
# print(f"混淆矩阵：\n{cm_A}")
df_A = pd.DataFrame(cm_A, index=df_label, columns=df_label)
print("预测结果A对应的DataFrame对象\n", df_A)

# 定义  预测B模型结果       预测对了6个恶性    1个良性
y_pre_B = ['恶性', '恶性', '恶性', '恶性', '恶性', '恶性', '恶性', '恶性', '恶性', '良性']
cm_B = confusion_matrix(y_train, y_pre_B, labels=label)
df_B = pd.DataFrame(cm_B, index=df_label, columns=df_label)
print("预测结果B对应的DataFrame对象\n", df_B)

# 打印预测 y_pre_A   和 y_pre_B  精准、召回、f1值
# 参1：真实样本       参2：预测样本         参3：正例标签
print(f"预测结果A的精确率：{precision_score(y_train, y_pre_A, pos_label='恶性')}")
print(f"预测结果B的精确率：{precision_score(y_train, y_pre_B, pos_label='恶性')}")

print(f"预测结果A的召回率：{recall_score(y_train, y_pre_A, pos_label='恶性')}")
print(f"预测结果B的召回率：{recall_score(y_train, y_pre_B, pos_label='恶性')}")

print(f"预测结果A的F1值：{f1_score(y_train, y_pre_A, pos_label='恶性')}")
print(f"预测结果B的F1值：{f1_score(y_train, y_pre_B, pos_label='恶性')}")


# 精确率：也叫查准率，对正例样本的预测准确率。
# 召回率：也叫查全率，指的是预测为真正例样本占所有真实正例样本的比重
# F1值：模型在这两个评估方向的综合预测能力

# 精确率：衡量模型预测为正的样本中有多少是真正的正例。
# 召回率：衡量模型能从所有真实正例中找出多少。
# F1值是：精确率和召回率的调和平均值，综合评价模型的准确性与全面性，帮助衡量模型的整体表现。

# 精确率：衡量错误预测的代价，
# 召回率：衡量漏掉正例的风险，
# F1值：综合评价模型在这两者间的平衡，帮助选择最优的模型性能。

# 1.精确率（Precision）：指的是所有被模型预测为正例的样本中，实际为正例的比例。
#       关注的是“假正例”（误判为正的负样本）有多少，反映了模型预测为正时的可靠性。
#       作用：减少假正例，避免不必要的错误分类。
#       意义：高精确率意味着模型更少给出错误的正类预测。

# 2.召回率（Recall）：指的是所有真实正例中，模型能够预测出来的比例。
#       关注的是“假负例”（误判为负的正样本）有多少，反映了模型对正类样本的“找全”能力。
#       作用：减少假负例，避免漏掉真正的正类。
#       意义：高召回率意味着模型能找出大部分正类样本，避免漏判。

# 3.F1值：是精确率和召回率的调和平均数，用来综合衡量模型的表现，特别是在精确率和召回率之间找到平衡。
#       作用：在精确率和召回率之间找到一个折衷，特别是在这两者相互矛盾时。
#       意义：F1值越高，说明模型在预测时既能准确地识别正例，又能尽可能地找到所有的正例，表现更全面。

# 总结来说，
#   精确率关注预测的准确性，
#   召回率关注找全正类的能力，
#   F1值则是综合考虑这两个因素，帮助评估模型的综合表现。