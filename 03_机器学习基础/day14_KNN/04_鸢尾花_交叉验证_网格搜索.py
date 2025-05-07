'''
    交叉验证解释：
        概述：交叉验证是一种更完善、可信度更高的一种模型评估方法。
        思路：把 数据集 分N份，每次都去选1份当作测试集，其他当作训练集，然后再给模型评分
            然后再用下一份当作测试集，其他当作训练集（皇帝轮流做，今天到你家）。最后计算所有的均值，
            当模型最终评分。
        思路是：
            把数据分成N份，例如：数据分成4份，4折交叉验证
                第1次：把第1份数据作为验证集（测试集），其他当作训练集，训练模型，模型预测，获取：准确率 --> 准确率1
                第2次：把第2份数据作为验证集（测试集），其他当作训练集，训练模型，模型预测，获取：准确率 --> 准确率2
                第3次：把第3份数据作为验证集（测试集），其他当作训练集，训练模型，模型预测，获取：准确率 --> 准确率3
                第4次：把第4份数据作为验证集（测试集），其他当作训练集，训练模型，模型预测，获取：准确率 --> 准确率4
                然后计算上述4次的准确率的平均值，作为模型最终准确率。
                假设第四次最好（准确率最高），则：用全部数据（训练集+测试集）训练模型，再用第4次的测试集对模型进行测试
            目的：
                为了让模型最终结果更加准确
            好处：
                相比单一切分的训练集和测试集获取的评分，经过交叉验证可信度更高。
    网格搜素：
        概述：机器学习内置API，一般结合交叉验证使用，通过API实现找到最优超参数
        目的：网格搜索+交叉验证 ： 让模型变得更强
'''

# 1.导入工具包
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris  # 加载鸢尾花数据集
from sklearn.preprocessing import StandardScaler  # 导入标准化的包
from sklearn.neighbors import KNeighborsClassifier  # 导入KNN分类对象

from sklearn.model_selection import train_test_split, GridSearchCV  # 分割训练集和测试集 (7 3 & 8 2)
from sklearn.metrics import accuracy_score  # 模型评估，计算模型预测准确率

import pandas as pd
import seaborn as sns  # 可视化工具包

# 2.加载数据集
iris_data = load_iris()

# 3.数据预处理
x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target,
                                                    test_size=0.2,
                                                    random_state=24)

# 4.特征工程
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)     # 训练 拟合 + 转换
x_test = transfer.transform(x_test)      # 只转换，不进行拟合
# 以下代码有问题，不对，不要选下面的，用上面的,下面的没有进行赋值
# transfer.fit_transform(x_train)     # 训练 拟合 + 转换
# transfer.transform(x_test)      # 只转换，不进行拟合

# 5：模型训练
es = KNeighborsClassifier()    # 注意这里不要传递超参数 即：k的值

# 5.1：定义一个字典  记录超参数可能出现的值
param_dict = {'n_neighbors': [i for i in range(1, 11)]}

# 5.2 创建 GridSearchCV对象 --> 寻找超参数。  使用网格搜索 + 交差验证方式
# es:需要计算超参数模型对象
# param_dict：该模型可能出现超参数
# cv：交叉验证折数   这里是4，代表4折交叉验证  k = [1~10]     4 * 10 = 40次
# 返回的es是处理后的模型对象
es = GridSearchCV(es, param_dict, cv=4)

# 具体的训练动作
es.fit(x_train, y_train)

# 打印最优超参组合
print(f"最优评分：{es.best_score_}")     # 最优组合评分
print(f"最优模型：{es.best_estimator_}")     # 最优模型
print(f"最优的超参组合：{es.best_params_}")     # 最优超参组合  K = ？
# print(f"具体交叉验证结果：{es.cv_results_}")     # 所有组合的评分结果（过程）

# 再次评估
# 获取到最优超参的模型对象
es = KNeighborsClassifier(n_neighbors=3)
# 模型训练
es.fit(x_train, y_train)
# 模型预测
y_pre = es.predict(x_test)
print(f"准确率：{accuracy_score(y_test, y_pre)}")