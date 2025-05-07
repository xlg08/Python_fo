'''
    1.导包
    2.加载数据
    3.数据预处理
    4.特征工程
        4.1：特征提取 -- 专业人士   （类似于海选）
        4.2：特征预处理       (归一化、标准化)
        4.3：特征降维
        4.4：特征选择    （类似于选拔之后）
        4.5：特征组合
    5.模型训练 -->  机器学习
    6.模型预测
    7.模型评估（准确率）
'''
import matplotlib.pyplot as plt
# 1.导包
from sklearn.datasets import load_iris  # 加载鸢尾花数据集
from sklearn.preprocessing import StandardScaler  # 导入标准化的包
from sklearn.neighbors import KNeighborsClassifier  # 导入KNN分类对象

from sklearn.model_selection import train_test_split  # 分割训练集和测试集 (7 3 & 8 2)
from sklearn.metrics import accuracy_score  # 模型评估，计算模型预测准确率

import pandas as pd
import seaborn as sns  # 可视化工具包


def demo01_分析数据集():
    # 2.加载数据集
    iris_data = load_iris()  # 因为这是自带的数据集
    # print(iris_data)          # 通过分析：iris数据集是一个字典

    print(iris_data.keys())
    # 字典中的键
    #   data    数据
    #   target    目标值
    #   frame     数据框
    #   target_name   目标名称
    #   DESCR     描述
    #   feature_names     特征名称
    #   filename    文件名
    #   data_module   数据模块

    # print("♥"*50)
    # print(iris_data.__len__())      # 有8个键值对
    # print(len(iris_data))

    # print("♥"*50)
    # target 目标值 --> 标签字段       150个标签字段
    # print(iris_data["target"])
    # print(iris_data.target)

    # print("♥"*50)
    # data 数据
    # print(iris_data["data"])
    # print(iris_data.data[:5])

    # print('♥'*50)
    # DESCR 描述
    # print(iris_data["DESCR"])
    # print(iris_data.DESCR)

    # print('♥'*50)
    # target_names 类别名称
    # ['setosa' 'versicolor' 'virginica']
    # print(iris_data.target_names)

    # print('♥'*50)
    # feature_names 特征名称
    # 花瓣、花萼.....
    # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    # print(iris_data.feature_names)

    # print('♥'*50)
    # filename 文件名称
    # iris.csv
    # print(iris_data.filename)

    # print('♥'*50)
    # data_module 模块名称
    # sklearn.datasets.data
    # print(iris_data.data_module)

    # print('♥'*50)
    # frame 数据框
    # print(iris_data.frame)      # None


def demo02_show_iris():
    # 1.加载鸢尾花数据
    iris_data = load_iris()

    # 2.将原数据封装dataframe
    iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    # print(iris_df)

    # 3.给df对象新增一个列  表示标签
    iris_df['label'] = iris_data.target
    print(iris_df)

    # 4.具体数据的可视化 : 散点图
    # x x轴      花瓣长度
    # y y轴      花瓣宽度
    # hue   颜色
    # fit_reg （False）      不绘制拟合回归线
    sns.lmplot(data=iris_df, x='petal length (cm)', y='petal width (cm)', hue='label', fit_reg=True)

    plt.title('iris data')
    plt.show()


def demo03_train_test_split():
    # 1.加载数据集
    iris_data = load_iris()

    # 2.具体的数据集划分    训练集 和 测试集
    # iris_data.data --> 特征 150条
    # 数据进行划分  测试集占比0.2(20%)     训练集占比0.8(80%)   将采用 训练集：测试集 -->  8:2

    # test_size 表示测试集占比 0.2  即：训练集是 0.8
    # random_state:随机种子。如果种子一样，则每次划分的数据集都是一样的
    #                      如果种子不一样，则每次元数据都不一样。固定随机种子
    # 随机种子大白话理解：这是使用第几套测试集和训练集的随机方案
    #       理解为：一种解决方案(1)(2)(3)(4)  随机训练集和测试集，当种子值固定的话
    # 随机种子范围 [0, 4294967295]
    # 若不填写随机种子值则随机选择方案,所以一般需要填写随机种子值
    x_train, x_test, y_train, y_test = \
        train_test_split(iris_data.data, iris_data.target, test_size=0.2,
                                                        random_state=24)
    print(x_train)
    print(f"训练集：       x-特征：{len(x_train)}")
    print(f"训练集标签：       y-标签：{len(y_train)}")
    print(f"测试集：       x-测试特征：{len(x_test)}")
    print(f"测试集标签：       y-测试标签：{len(y_test)}")


def demo04_模型预测评估():
    # 1.加载数据
    iris_data = load_iris()

    # 2.数据预处理
    x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2,
                                                        random_state=24)

    # 3.特征工程
    # 特征提取  、 特征预处理 （归一化、标准化）
    transfer = StandardScaler()
    # 同时完成 fit  和   transform()
    # fit_transform 作用：先基于训练集特征进行拟合：例如：均值、方差、标准差等信息。内置好的模型对象
    transfer.fit_transform(x_train)

    # 基于训练集特征，调用内置好的模型（标准化对象），上一步结果，进行转换
    transfer.fit_transform(x_test)

    # 4.模型训练 -->  机器学习

    # 4.1：创建模型对象
    es = KNeighborsClassifier(n_neighbors=5)
    # 4.2：模型训练
    es.fit(x_train, y_train)

    # 模型预测
    y_predict = es.predict(x_test)
    print(f"测试集的预测结果：{y_predict}")
    print(f"真实值标签结果{y_test}")

    # 5.对模型进行训练
    # 5.1:定义新的数据集
    # 花萼长  花萼宽   花瓣长   花瓣宽
    x_test_new = [[2.21, 3.4, 5.4, 7.2]]
    # 5.2：对新的数据集进行标准化
    x_test_new = transfer.transform(x_test_new)
    # 5.3：预测
    y_test_new = es.predict(x_test_new)
    print(f"新数据及预测结果：{y_test_new}")

    # 6.模型评估
    # 方式一：针对测试值的特征 和测试值的标签进行预测
    # 传入测试集特征   测试标签
    print(f"直接评估：{es.score(x_test, y_test)}")

    # 方式二：用预测值和真实值进行比较，得到准确率
    print(f"预测值和真实值的对比评估，准确率为：{accuracy_score(y_test, y_predict)}")


if __name__ == '__main__':
    # demo01_分析数据集()
    # demo01_show_iris()
    # demo03_train_test_split()
    demo04_模型预测评估()
