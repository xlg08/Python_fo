'''
    案例：癌症预测案例   目的：演示逻辑回归API
    逻辑回归：
        概述：分类算法的一种，一般使用二分类
        原理：
            1.基于线性回归，综合特征值，计算标签值（输入）
            2.把上述的标签值，传递激活函数（sigmoid函数），映射[0，1]区间值
            3.手动设置阈值，来完成分类划分
                例如： 0.6  则
                        结果 > 0.6  A类
                        否则        B类
        损失函数：
            先基于 极大似然函数计算，然后转换对数似然估计，结合梯度下降，计算最小值
        总结：
            逻辑回归原理：线性回归输出，作为逻辑回归的输入
            默认情况下：样本少的当作正例，其他当作反例（假例）
            （逻辑回归）损失函数设计原则：真实例子是正例的情况下，概率值越大越好

    机器学习开发流程：
        1.准备数据
        2.数据预处理
        3.特征工程
        4.模型训练
        5.模型预测
        6.模型评估

'''

# 导包
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler



# 1.准备数据
data = pd.read_csv("../../data/breast-cancer-wisconsin.csv")
# data.info()
# data.describe()
# print(data)

# 2.数据预处理
data = data.replace("?", np.NaN)
# data.info()

# 2.2:缺失值预处理,    axis=0  (默认行)
data.dropna(axis=0, inplace=True)
# data.info()


# 3.特征工程
x = data.iloc[:, 1:-1]      # 索引从1开始，直到最后一列(不包含最后一列)  去掉了第一个和最后一个
# x.info()

y = data.Class
# y.info()
# print(y)

# 3.特征工程
# 3.1：拆分数据集
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.2, random_state=24)

# 3.2：标准化
# transfer = StandardScaler()
# x_train = transfer.fit_transform(x_train)
# x_test = transfer.transform(x_test)

# 4.模型训练
es = LogisticRegression()
es.fit(x_train, y_train)

# 模型预测
y_pre = es.predict(x_test)
print("预测值：", y_pre)
# print("w：", es.coef_)
# print("b：", es.intercept_)

# 预测准确率
print(f"准确率是：{accuracy_score(y_test, y_pre)}")
# 做的是癌症预测。仅仅通过正确率，不能衡量逻辑回归的结果
#   目前只知道正确率，不知道哪个预测成功，哪个预测失败了，所以需要对数据进行进一步评估
#   混淆矩阵、精确率（掌握）、召回率（掌握）、F1值（掌握）、ROC曲线（了解）、AUC值（了解）



