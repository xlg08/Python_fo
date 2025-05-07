import numpy as np  # 主要是用来做数学相关的运算的
import matplotlib.pyplot as plt  # 绘图的
from sklearn.linear_model import LinearRegression  # 线性回归
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error  # 计算均方误差

# from sklearn.model_selection import train_test_split      # 切割训练集和测试集

# 获取数据
np.random.seed(24)  # 设置随机种子

x = np.random.uniform(-3, 3, size=200)
y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=200)

# 数据处理
X1 = x.reshape(-1, 1)
X3 = np.hstack(
    [X1, X1 ** 2, X1 ** 3, X1 ** 4, X1 ** 5, X1 ** 6, X1 ** 7, X1 ** 8, X1 ** 9, X1 ** 10, X1 ** 11, X1 ** 12, X1 ** 13,
     X1 ** 14, X1 ** 15, X1 ** 16, X1 ** 17, X1 ** 18, X1 ** 19, X1 ** 20, X1 ** 21, X1 ** 22, X1 ** 23, X1 ** 24,
     X1 ** 25, X1 ** 26, X1 ** 27, X1 ** 28, X1 ** 29])

# X3 = np.hstack([X1, X1**2, X1, X1, X1, X1, X1, X1, X1, X1, X1, X1, X1, X1, X1, X1])
# X3 = np.hstack([X1, X1**2])
# 创建模型
es = LinearRegression()
es.fit(X3, y)
print("w:", es.coef_)
print("w:", len(es.coef_))
print("b:", es.intercept_)

# 模型预测
y_pre = es.predict(X3)

# 模型评估
print(f"均方误差: {mean_squared_error(y, y_pre)}")
print(f"均方根误差: {root_mean_squared_error(y, y_pre)}")
print(f"平均绝对值误差: {mean_absolute_error(y, y_pre)}")

plt.scatter(x, y)
plt.plot(np.sort(x), y_pre[np.argsort(x)], color='red')
plt.show()
