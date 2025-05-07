import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

"""
    案例：集成学习之bagging思想 随机森林算法 代码
        集成学习：
            概述：把多个弱学习器，组成一个强的学习器的过程 --> 集成学习
            思想：
                bagging思想：
                    1.有放回的随机抽取
                    2.平权投票
                    3.可以并行执行
                boosting思想：
                    1.每次训练都使用全部的训练集(样本)
                    2.加权投票 --> 预测正确：权重降低，预测错误：权重升高
                    3.只能串行执行
                bagging思想代表：
                    随机森林算法
                
                随机森林：
                    1.每个弱学习器都是CART树(必须是二叉树)
                    2.有放回的随机抽样，平权投票，并行执行


"""

# 2.读取数据
data = pd.read_csv('../../data/train.csv')
print(data)

# 3.数据预处理
# 抽取特征和标签
x = data[["Pclass", "Sex", "Age"]].copy()
y = data['Survived']

# 4.处理空值
x['Age'] = x['Age'].fillna(x['Age'].mean())

x = pd.get_dummies(x)
print(x.info)

x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.152, random_state=20)

# 做特征工程（标准化）

# 单一的决策树
es = DecisionTreeClassifier()
es.fit(x_train, y_train)
# 预测
y_pre = es.predict(x_test)
print(f"y预测值：{y_pre}")
# 模型评估 决策树模型预测准确率
print(f"决策树模型预测评分：{es.score(x_test, y_test)}")
print(f"获取模型特征：{es}")
print(f"获取模型每个特征重要性得分：", es.feature_importances_)
print(f"获取模型属性参数：", es.get_params())
print("*" * 30)

# 随机森林算法
es2 = RandomForestClassifier()
# 训练
es2.fit(x_train, y_train)
# 预测
y_pre2 = es2.predict(x_test)
print(f"随机森林模型预测评分：{es.score(x_test, y_test)}")

# 场景3：网格搜索
es3 = RandomForestClassifier()
params = {"n_estimators": [30, 60, 90, 120], 'max_depth': [2, 3, 5, 7, 10, 15, 20, 30]}
gs_es = GridSearchCV(es3, param_grid=params, cv=6)
gs_es.fit(x_train, y_train)
y_pre3 = gs_es.predict(x_test)
print(f"预测值：{y_pre3}")
print(f'随机森林模型预测准确率：{gs_es.score(x_test, y_test)}')
print(f"最佳参数：{gs_es.best_params_}")
