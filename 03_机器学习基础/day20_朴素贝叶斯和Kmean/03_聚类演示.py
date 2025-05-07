# 1.导入工具包
# 1.导入工具包
from sklearn.cluster import KMeans  # 聚类 API   指定质心  来分簇
import matplotlib.pyplot as plt  # 绘图的
from sklearn.datasets import make_blobs  # 默认会按照高斯分布（正态分布）生成数据集，只需要指定均差，标准差
from sklearn.metrics import calinski_harabasz_score  # calinski_harabaz_score 废弃

# 准备数据集
#   n_samples 样本数量
#   n_features 样本特征数量
#   centers 质心点
#   cluster_std 标准差
x, y = make_blobs(n_samples=1000, n_features=2, centers=[[-1, -1], [0, 0], [1, 1], [2, 2]], cluster_std=[0.4, 0.2, 0.2, 0.2], random_state=24)

print(x)
print(y)

# 绘制上述的图形
#   参1：横坐标
#   参2：纵坐标
#   参3：
plt.scatter(x[:, 0], x[:, 1], marker='o', c='r')
plt.show()


# KMeans 对象
es = KMeans(n_clusters=4, random_state=24)
y_pre = es.fit_predict(x)       # 预测值

plt.scatter(x[:, 0], x[:, 1], c=y_pre)
plt.show()

print("评价指标（评分）", calinski_harabasz_score(x, y_pre))





