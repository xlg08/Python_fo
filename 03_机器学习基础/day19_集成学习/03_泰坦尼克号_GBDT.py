import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV

# 读数据
df_data = pd.read_csv("../../data/train.csv")
# df_data.info()

# 对数据进行预处理
x = df_data[['Pclass', 'Sex', 'Age']].copy()
y = df_data['Survived']

# 对age缺失值进行处理
x['Age'] = x['Age'].fillna(x['Age'].mean())

# 热编码
# get_dummies 是用于 将分类变量转换为虚拟变量（dummy/indicator variables） 的函数。
x = pd.get_dummies(x)
print(x)


x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.2, random_state=24)

# 特征工程 略


# 场景1：构建单一决策树
es = DecisionTreeClassifier()
es.fit(x_train, y_train)

y_pre = es.predict(x_test)
print(f"单个决策树预测结果{y_pre}")
print(f"单个决策树模型评估{accuracy_score(y_test, y_pre)}")

# 梯度提升树对象(GBDT)
es2 = GradientBoostingClassifier()
es2.fit(x_train, y_train)
y_pre2 = es2.predict(x_test)
print(f"梯度提升决策树预测结果{y_pre2}")
print(f"梯度提升决策树模型评估{accuracy_score(y_test, y_pre2)}")

# 场景3： 针对GBDT 模型进行参数调优
# learning_rate = 0.1,
# n_estimators = 100,
# max_depth = 3,

param_dict = {
    'learning_rate': [0.01],
    'n_estimators': [50, 60],
    'max_depth': [3, 5]
}

es3 = GradientBoostingClassifier()
es4 = GridSearchCV(es3, param_dict, cv=2)
es4.fit(x_train, y_train)

print(f"网格搜索后的最高评分:{es4.best_score_}")
print(f"网格搜索后的模型:{es4.best_estimator_}")
