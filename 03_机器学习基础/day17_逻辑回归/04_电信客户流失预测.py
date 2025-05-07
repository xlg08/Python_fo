'''

'''


import pandas as pd
import numpy as np

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, classification_report

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score

import warnings
warnings.filterwarnings('ignore',module='sklearn')
warnings.filterwarnings('ignore',category=FutureWarning)

import matplotlib as plt
import seaborn as sns

data = pd.read_csv("../../data/churn.csv")
# data.info()
# print(data.describe())

data.Churn.replace("Yes", "1", inplace=True)
data.Churn.replace("No", "0", inplace=True)
data.gender.replace("Female", "1", inplace=True)
data.gender.replace("Male", "0", inplace=True)


# print(data)
# print('data:', data.head(10))
# data.info()

counts = data.Churn.value_counts(1)
print('counts：\n', counts)

# sns.countplot(data=data, y = “Contract_Month”, hue=‘flag’)
# plt.show()



x = data.iloc[:, 1:]
y = data.iloc[:, 0]
# print(y)


x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.1563, random_state=20)
    # train_test_split(x, y, test_size=0.15, random_state=20)


transfer = StandardScaler()
# # 3.2:训练集 测试
x_train.iloc[:, -1:] = transfer.fit_transform(x_train.iloc[:, -1:])
x_test.iloc[:, -1:] = transfer.transform(x_test.iloc[:, -1:])

es = LogisticRegression()
es.fit(x_train, y_train)

y_pre = es.predict(x_test)
print("预测值：", y_pre)

print(f"准确率是：{accuracy_score(y_test, y_pre)}")

label = ["0", "1"]
cm_A = confusion_matrix(y_test, y_pre, labels=label)
print(cm_A)

print(f"预测结果的精确率：{precision_score(y_test, y_pre, pos_label='1')}")
print(f"预测结果的召回率：{recall_score(y_test, y_pre, pos_label='1')}")
print(f"预测结果的F1值：{f1_score(y_test, y_pre, pos_label='1')}")


# 计算ROC曲线面积，即AUC值
# y_true：每个样本的真实类别，必须为0(反例), 1(正例)标记
# y_score：预测得分，可以是正例的估计概率、置信值或者分类器方法的返回值
'''
    AUC 越大表示分类器性能越好
        当 AUC=0.5 时，表示分类器的性能等同于随机猜测
        当 AUC=1 时，表示分类器的性能完美，能够完全正确地将正负例分类
'''
print(es.predict_proba(x_test))         # 得到获得每一类标签的概率值
y_prob = es.predict_proba(x_test)[:, 1]         # 取要的那一类标签的概率值
# print(y_prob)
print("AUC:", roc_auc_score(y_test, y_prob))


'''
    y_true：   真实目标值
    y_pred：   估计器预测目标值
    labels:    指定类别对应的数字
    target_names：  目标类别名称
    return：   每个类别精确率与召回率
'''
cr = classification_report(y_test, y_pre, labels=label, target_names=data.Churn)
print(cr)


