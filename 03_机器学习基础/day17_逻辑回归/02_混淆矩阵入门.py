'''
    混淆矩阵
        概述：用于展示真实值和预测值之间  正例和反例的情况
        模型：会用分类少的样本当作正例
        混淆矩阵名称：
                        预测值（正例）         预测值（反例）
        真实值（正例）     真正例（TP）           伪反例（FN）
        真实值（反例）     伪正例（FP）           真反例（TN）
'''

# 导包    需求分析    模型 （包）
import pandas as pd

from sklearn.metrics import confusion_matrix  # 混淆矩阵

# 2.定义数据集 样本集10样本       手动指定：恶性 正例      良性 反例
y_train = ['恶性', '恶性', '恶性', '恶性', '恶性', '恶性', '良性', '良性', '良性', '良性']

# 定义标签名     标签1代表正样本（正例）        标签2代表负样本（反例）
label = ['恶性', '良性']
df_label = ['恶性(正例)', '良性(反例)']

# 定义预测结果  模型A       预测对了   3个恶性   4个良性
# 真实有几个 6个恶性。  预测3个恶性。有另外3个预测错了。随便从里面找3个恶性改为良性
# 故 3个恶性的  7个良性的
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

# 精确率：预测的正例中预测对的比例（有几个预测对了）
# 召回率：





