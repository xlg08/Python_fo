import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# data_df = pd.read_csv('./data.csv', encoding='utf-8')

data = {
        '电视广告数（x）': [1, 3, 2, 1, 3],
        '汽车销售数（y）': [14, 24, 18, 17, 27]
        }
data_df = pd.DataFrame(data)
print(data_df)

x = data_df[['电视广告数（x）']]
y = data_df['汽车销售数（y）']

es = LinearRegression()
es.fit(x, y)

print(f"斜率是: {es.coef_[0]}")
print(f"截距是: {es.intercept_}")

# 预测值
y_pred = es.predict(x)

# 绘制图形
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='r', label='实际数据')
plt.plot(x, y_pred, color='b', label='线性回归拟合线')
plt.xlabel('电视广告数（x）')
plt.ylabel('汽车销售数（y）')
plt.legend()
plt.show()
