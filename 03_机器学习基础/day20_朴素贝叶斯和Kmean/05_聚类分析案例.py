import os

os.environ['OMP_NUM_THREADS'] = '1'  # 设置OMP程序运行时使用的线程数
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
import numpy as np


def dm_k():
    sse_list = []
    sc_list = []
    # 1、获取数据
    df = pd.read_csv("../../data/customers.csv")
    df.info()

    # 抽取特征
    x = df.iloc[:, 3:5]
    print(x)

    # for循环，测试不同k值的评估效果
    for k in range(2, 60):
        es = KMeans(n_clusters=k, max_iter=100, random_state=24)
        y_pre = es.fit_predict(x)
        # SSE sc  分别把评分添加到对应列值红
        sse_list.append(es.inertia_)
        sc_list.append(silhouette_score(x, y_pre))

    # 绘制图形
    plt.figure(figsize=(20, 10))
    plt.plot(range(2, 60), sse_list, label='SSE')
    plt.xticks(range(0, 100, 1))
    plt.grid()
    plt.show()

    plt.figure(figsize=(20, 10))
    plt.plot(range(2, 60), sc_list, label='SC')
    plt.xticks(range(0, 100, 1))
    plt.grid()
    plt.show()


# 最优k =5 效果最好

def dm02_train_model():
    df = pd.read_csv("../../data/customers.csv")
    x = df.iloc[:, 3:5]
    es = KMeans(n_clusters=5, max_iter=100, random_state=24)
    y_pre = es.fit_predict(x)
    # print(y_pre)

    # print(x.values)
    #
    # # 绘制5个簇样本点 -》散点图
    plt.scatter(x.values[y_pre == 0, 0], x.values[y_pre == 0, 1], c='pink', label='Standard')  # 0号簇
    plt.scatter(x.values[y_pre == 1, 0], x.values[y_pre == 1, 1])       # 1号簇
    plt.scatter(x.values[y_pre == 2, 0], x.values[y_pre == 2, 1])       # 2号簇
    plt.scatter(x.values[y_pre == 3, 0], x.values[y_pre == 3, 1])       # 3号簇
    plt.scatter(x.values[y_pre == 4, 0], x.values[y_pre == 4, 1])       # 4号簇

    # print("质心：", es.cluster_centers_)

    # 绘制5个簇的质心
    plt.scatter(es.cluster_centers_[:, 0], es.cluster_centers_[:, 1])
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()


def 巧用array性质():
    # x.values [[15,39],[ 15,81],[16,6],[16,77],[17,40],[17,76]]
    x = [[15, 39], [15, 81], [16, 6], [16, 77], [17, 40], [17, 76]]  # 模拟x.values
    # print(type(x))  #<class 'list'>
    x2 = np.array(x)  # <class 'numpy.ndarray'>

    #  模拟 x.values[y_pre ==0]  传入布尔值
    result = x2[[True, False, True, True, False, False]]
    # [[15, 39], [15, 81], [16, 6], [16, 77], [17, 40], [17, 76]]
    # # [[15 39]            [16  6]  [16 77]]
    # print(result)

    # 模拟 x.values[y_pre ==0,0]
    result1 = x2[[True, False, True, True, False, False], 0]  # 0,0 获取x轴数据
    # print(result1)  #[15 16 16]

    # [y_pre == 0, 1]
    result2 = x2[[True, False, True, True, False, False], 1]  # 0,0 获取y轴数据
    print(result2)  # [15 16 16]


if __name__ == '__main__':
    dm02_train_model()
