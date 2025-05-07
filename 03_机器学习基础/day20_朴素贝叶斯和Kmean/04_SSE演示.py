"""
聚类算法的评估指标 即：SSE+肘部法 ，SC轮廓系数法，CH轮廓系数法
    思路1： SSE+肘部法
            SSE概述：所有的簇的 所有样本到该簇质心的误差的平方和
            特点：随着K的增加 ，SSE值会减少
            目的：SSE值越小，代表簇内的样本越聚集，即内聚程度高
        肘部法：
            K值增加,SSE会减少 ，下降梯度会陡然变缓，那个k值，就是我们要的最佳值（分几个簇最佳）
    思路2：sc轮廓系数
        考虑簇外 -->  聚集程度  -->  越小越好
        考虑簇外 -->  分离程度  -->  越大越好

"""

import os
os.environ['OMP_NUM_THREADS'] = '4'  # 设置OMP程序运行时使用的线程数

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import silhouette_score


def dm01_sse():
    # 创建一个sse列表，记录每个K值的sse值
    sse_list = []
    # 1、生成数据集
    x, y = make_blobs(
        n_samples=1000,  # 样本数量
        n_features=2,  # 特征数
        centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],  # 质心点坐标
        cluster_std=[0.4, 0.2, 0.2, 0.2],  # 4个簇的std标准差
        random_state=24  # 固定随机种子
    )

    # for循环，获取到每个K值，计算其对应sse值，并且找一个容器存储起来
    # 从 1 个簇的情况 到 100 个簇的情况
    for k in range(1, 101):
        # 创建KMeans对象
        # max_iter 最大迭代次数
        # 随机种子
        es = KMeans(n_clusters=k, max_iter=100, random_state=24)
        # 训练模型
        es.fit(x)

        # 获取每种簇sse值     -->    误差平方和
        sse_value = es.inertia_
        print(f"{k}个簇下的sse(误差平方和)值：", sse_value)
        # 将每个k对应的sse值，添加到了列表中
        sse_list.append(sse_value)

    # 绘制图形曲线 -》 sse曲线 实现可视化
    # 设置画布
    plt.figure(figsize=(20, 10))
    # 设置标题
    plt.title("sse value")
    # 设置x轴刻度
    plt.xticks(range(0, 100, 1))
    # 设置y轴
    plt.yticks(range(0, 1000000, 1))
    plt.xlabel("k")
    plt.ylabel("sse")
    # 绘制网格
    plt.grid()
    # 参1：k的值   参2：k值对应sse值
    plt.plot(range(1, 101), sse_list)
    plt.show()


def dm02_轮廓系数():
    sc_list = []

    # 造数据
    # 1、生成数据集
    x, y = make_blobs(
        n_samples=1000,  # 样本数量
        n_features=2,  # 特征数
        centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],  # 质心点坐标
        cluster_std=[0.4, 0.2, 0.2, 0.2],  # 4个簇的std标准差
        random_state=24  # 固定随机种子
    )

    print("真实值为：", y)

    # K ??
    # for 循环遍历，获取到每个k的值，计算sc值，并且添加到列表中
    for k in range(2, 101):
        es = KMeans(n_clusters=k, max_iter=100, random_state=24)
        es.fit(x)
        y_pred = es.predict(x)
        print("预测值为：", y_pred)
        # 获取每个簇的sc值
        sc_value = silhouette_score(x, y_pred)
        print(f'{k}个簇时的sc值：{sc_value}')
        # 将每个k值对应sc值添加到列表中
        sc_list.append(sc_value)

    # 绘制 sc 区间
    plt.figure(figsize=(20, 10))
    plt.title("sc value")
    # 设置 x 轴的刻度
    plt.xticks(range(0, 101, 4))
    plt.xlabel("k")
    plt.ylabel("sc")

    # 绘制网格
    plt.grid()
    # 注意！！ 要从 2 开始
    plt.plot(range(2, 101), sc_list)
    plt.show()


def dm03_CH轮廓系数():
    ch_list = []

    # 造数据
    # 1、生成数据集
    x, y = make_blobs(
        n_samples=1000,  # 样本数量
        n_features=2,  # 特征数
        centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],  # 质心点坐标
        cluster_std=[0.4, 0.2, 0.2, 0.2],  # 4个簇的std标准差
        random_state=24  # 固定随机种子
    )

    for k in range(2, 100):
        es = KMeans(n_clusters=k, max_iter=100, random_state=24)
        # es.fit(x)
        y_pre = es.fit_predict(x)
        # 获取每个k值的ch值
        ch_value = calinski_harabasz_score(x, y_pre)
        print(f'{k}个簇时的ch值：{ch_value}')
        ch_list.append(ch_value)

    # 绘制 ch 区间  -->  数据可视化
    plt.figure(figsize=(20, 10))
    plt.title("ch value")
    # 设置 x 轴的刻度
    plt.xticks(range(0, 101, 3))
    plt.xlabel("k")
    plt.ylabel("ch")

    # 绘制网格
    plt.grid()
    # 注意！！ 要从 2 开始
    plt.plot(range(2, 100), ch_list)
    plt.show()


if __name__ == '__main__':
    # dm01_sse()
    # dm02_轮廓系数()
    dm03_CH轮廓系数()
