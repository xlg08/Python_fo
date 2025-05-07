'''
    演示:
        拟合问题
        回顾:
            拟合:指的是模型和数据之间存在关系,即:预测值和真实值之间的关系

            欠拟合:模型在训练集、测试集表现都不好
                原因:模型(特征太少)太简单了
            过拟合:模型在训练集变现好,在测试集表现不好
                原因:模型(特征太多)过于复杂了        数据不纯、数据量小
            正好拟合(泛化):模型在训练集,测试集都好
            奥卡姆剃刀:在误差相同(泛化程度一样)的情况下,优先选择简单的模型

        正则化:

'''


import numpy as np      # 主要是用来做数学相关的运算的
import matplotlib.pyplot as plt     # 绘图的
from sklearn.linear_model import LinearRegression           # 线性回归
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error     # 计算均方误差
# from sklearn.model_selection import train_test_split      # 切割训练集和测试集


np.random.seed(24)      # 设置随机种子


# 获取数据源
x = np.random.uniform(-3, 3, size=100)      # uniform 生成-3到3之间的100个数
# y = 0.5 * x ** 2 + x + 2 + 噪声     (正态分布生成随机值)
# random.normal()
# 均值是 0      标准差是 1        生成100个
y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)
print(f"x轴的值: {x}")
print(f"y轴的值: {y}")          # 现在数据的样子是:  []

# 数据的预处理,  因为训练要求的数据 [[  ]],目前数据时[]  重构
X1_train = x.reshape(-1, 1)

# print(X1_train)
Y1_train = y

# 创建模型对象
# 1.线性回归 正规方程
es = LinearRegression()
# 模型训练
es.fit(X1_train, Y1_train)

# 4.模型预测
y_pre = es.predict(X1_train)


# 模型评估
print(f"均方误差: {mean_squared_error(y, y_pre)}")
print(f"均方根误差: {root_mean_squared_error(y, y_pre)}")
print(f"平均绝对值误差: {mean_absolute_error(y, y_pre)}")


# 5.绘制图形
plt.scatter(x, y)       # 真实值x和y  散点图
plt.plot(X1_train, y_pre, color='red')       # 预测值 x y轴   绘制折线图(拟合回归线)
plt.show()

