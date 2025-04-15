'''
    KNN(K-近邻算法)
        概述：
            专业：找离测试集最近的哪K个样本，然后投票。哪个标签值多，就用它作为测试集的最终结果
            大白话：近朱者赤，近墨者黑
        KNN算法实现思路：
            思路1：分类思路   投票，选票数最多的
            思路2：回归思路    求平均值
        KUN算法分类思路原理如下：
            1.基于欧氏距离计算      每个训练集 离 测试集的距离
                欧氏距离：对应特征差值的平方和 开根号
            2：按照这个距离值，进行升序排列，找到距离最小的那个K值的样本
            3：分类思想：投票选取，票数最多的哪个标签值-》作为测试集的标签
                如果标签票数一致  参考：最简单的模型（即：最近距离的哪个标签结果）。奥卡姆剃刀原则
        KNN算法  代码实现思路
            1：导包
                    确保你已经安装了这个库scikit-learn
            2：创建模型（算法）对象
            3：准备训练集（x_train,y_train）
            4:准备测试集（x_test）     ->     要求计算的就是y_test (三缺一)
            5:模型训练
            6：模型预测（打印预测结果）


        分类任务: 标签必须为离散值(整数或字符串)，通过多数投票预测类别.
        回归任务: 标签必须为连续值(浮点数或整数)，通过均值预测数值.
        核心原则:确保标签类型与任务类型一致，并提前处理缺失值和异常标签.
'''

# 1.导包      KNN算法 --> 分类对象
from sklearn.neighbors import KNeighborsClassifier

# 2.创建模型的对象
# es : estimator -->  评估、预测
# n_neighbors ：邻居的数量，默认是5
es = KNeighborsClassifier(n_neighbors=2)

# 3.准备训练集
# x_train = [[1], [2], [3], [4]]
# 如果邻居数量是4，即等于训练样本总个数，则返回最小值
# 当训练标签中的类型的比例为 1 : 1 时，也返回最小值
# 根据奥卡姆剃刀原则：当值并列的时候取最小值与距离和顺序无关

# y_train = [0, 0, 1, 1]
# y_train = [7, 5, 2, 8]

x_train = [[1], [2], [3], [4], [5]]
y_train = [0, 1, 2, 3, 4]

# y_train = [0.1, 0.2, 0.3, 0.4]      # 报错
# 分类问题传连续值会报错 未知标签类型：连续。也许您正在尝试拟合一个分类器，该分类器期望具有连续值的回归目标上的离散类。
# ValueError: Unknown label type: continuous. Maybe you are trying to fit a classifier,
# which expects discrete classes on a regression target with continuous values.

'''
# y_train = [1, 0, 0, 1]        # 0
# y_train = ["0", "0", "1", "1"]        # "0"
# y_train = ["B", "A", "A", "B"]        # "A"
# y_train = ["A", "A", "B", "B"]        # "A"
# y_train = ["AB", "AB", "BA", "BA"]        # "AB"
# y_train = ["BA", "AB", "AB", "BA"]        # "AB"
# print("AB" < "BA")      # True   
'''


# 4.测试集     # !!!!注意，这里的格式容易出现错误
x_test = [[5]]      # 两层

# 5.模型训练
# 参一：训练集的特征    参二：训练集的标签
es.fit(x_train, y_train)

# 6.模型预测
# 传入 测试集的特征，基于模型 获取测试集的标签
y_test = es.predict(x_test)
print(f"预测结果是：{y_test}")