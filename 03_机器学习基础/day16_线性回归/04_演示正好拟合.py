import numpy as np          # 主要是用来做数学相关的运算的
import matplotlib.pyplot as plt         # 绘图的
from sklearn.linear_model import LinearRegression           # 线性回归
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error        # 计算均方误差

# from sklearn.model_selection import train_test_split              # 切割训练集和测试集


np.random.seed(24)  # 设置随机种子

# x轴 和 y轴
# x轴坐标
x = np.random.uniform(-3, 3, size=100)

# y轴
y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)

# 数据集预处理
X_train = x.reshape(-1, 1)

# hstack()      垂直合并  即:竖直方向的合并
x2 = np.hstack([X_train, X_train ** 2])
# print(f"{X_train}")
# print(f"{x2}")


# 创建模型
es = LinearRegression()

# 模型训练
es.fit(x2, y)
# print("w:", es.coef_)
# print("w:", len(es.coef_))
# print("b:", es.intercept_)
# 模型预测
y_pre = es.predict(x2)

# 模型评估
print(f"均方误差: {mean_squared_error(y, y_pre)}")
print(f"均方根误差: {root_mean_squared_error(y, y_pre)}")
print(f"平均绝对值误差: {mean_absolute_error(y, y_pre)}")

# 画图
# 真实x和真实y       --    绘制散点
plt.scatter(x, y)
# plt.plot(x2, y_pre, color='red')        # 没有排序,乱画线
# np.sort(x)    如果进行排序了,会破坏打乱原有的x和y的对应关系
# np.argsort(x)     拿到之前的关系的索引.   返回的是索引值.  y_pre[]
plt.plot(np.sort(x), y_pre[np.argsort(x)], color='red')
plt.show()
