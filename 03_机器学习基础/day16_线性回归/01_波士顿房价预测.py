# 导包
# from sklearn.datasets import load_boston  # 数据
from sklearn.preprocessing import StandardScaler  # 特征处理
from sklearn.model_selection import train_test_split  # 数据集划分
from sklearn.linear_model import LinearRegression  # 正规方程的回归模型
from sklearn.linear_model import SGDRegressor  # 梯度下降的回归模型
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error  # 均方误差评估 平均值绝对误差评估  均值根误差评估
from sklearn.linear_model import Ridge, RidgeCV  # l1正则化  l2正则化

import pandas as pd
import numpy as np

# 加利福尼亚住房
# from sklearn.datasets import fetch_california_housing
# housing = fetch_california_housing()

# from sklearn.datasets import fetch_openml
# housing = fetch_openml(name="house_prices", as_frame=True)


"""
    机器学习项目研发流程：
        1.获取数据
        2.数据预处理
        3.特征工程
            特征提取、特征预处理（标准化、归一化）
            特征降维
            特征选取
            特征组合
        4.模型训练
        5.模型预测
        6.模型评估
"""

# 1.获取数据集
# data = load_boston()      # version 1.2. 之前的波士顿房价数据涉及种族歧视，因此version 1.2.及以后不提供了
# print(data)


data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
# print(data)

# print(f"data类型: {type(data)}")
# print(f"data：{len(data)}, {data[:5]}")
# print(f"target类型: {type(target)}")
# print(f"目标：{len(target)}, {target[:5]}")

# df = pd.DataFrame(data)
# print(df.info())
# print(df.describe())

# 2.数据预处理                                        特征   标签    测试集占比       随机种子
x_train, x_test, y_train, y_test = \
    train_test_split(data, target, test_size=0.2, random_state=2)

# 3.特征工程
# 3.1:创建标准化
transfer = StandardScaler()
# 3.2:训练集 测试
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4.模型训练
# 4.1:创建线性回归之正规方程对象
# fit_intercept=True    表示是否计算偏置
es = LinearRegression(fit_intercept=True)
# 4.2:模型进行训练
es.fit(x_train, y_train)


# 5.模型预测
y_pre = es.predict(x_test)
print(f"预测值: {y_pre}")
print(f"权重: {es.coef_}")
print(f"偏置: {es.intercept_}")


# 6.模型评估        需要衡量预测得值准不准,需要模型进行评估
# knn : 准确率     线性回归方程  损失函数(预测值 - 真实值) MAE RMSE MSE
print(f"平均绝对误差: {mean_absolute_error(y_test, y_pre)}")
print(f"均方误差: {mean_squared_error(y_test, y_pre)}")
print(f"均方根误差: {root_mean_squared_error(y_test, y_pre)}")
