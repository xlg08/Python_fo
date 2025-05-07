# AdaBoost实战葡萄酒数据
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier     # 集成学习
from sklearn.metrics import accuracy_score

df_wine = pd.read_csv('../../data/wine0501.csv')
# print(df_wine.head(3))
# df_wine.info()

# 从数据集中找到特征标签  Alcohol  酒精   色调 Hub
# Class label 葡萄酒种类 3  [1 2 3]      决策树     只识别二分类
print(df_wine['Class label'].unique())      # [1 2 3]


# 数据处理
# 过滤标签
df_wine = df_wine[df_wine["Class label"] != 3]      # 去掉 3
print(df_wine['Class label'].unique())      # [1 2]

# 获取特征列         标签列
x = df_wine[['Alcohol', 'Hue']]
y = df_wine['Class label']      # 标签列

# print(x[:3])
# print('*' * 30)
# print(y[:3])
# print(type(y))
# print(y.dtype)
# 通过标签编码器  把标签列 转换为 数值列
le = LabelEncoder()
y = le.fit_transform(y)
print(y)
# print(type(y))
# print(y.dtype)

# 训练集
# stratify 参数：按比例y品类值
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3, random_state=75, stratify=y)
    # train_test_split(x, y, test_size=0.2, random_state=244, stratify=y)
    # train_test_split(x, y, test_size=0.2, random_state=4, stratify=y)

# 特征工程


# 单一决策树
# 创建模型对象
es1 = DecisionTreeClassifier(max_depth=3)
# 训练模型
es1.fit(x_train, y_train)
# 预测
y_pre = es1.predict(x_test)
print("单一决策树的预测结果：", y_pre)
# 模型评估
print(f"单一决策树的预测得分：{accuracy_score(y_test, y_pre)}")

# 场景2  -->  集成学习     CART树
# es2 = AdaBoostClassifier(estimator=es1, n_estimators=100, learning_rate=10, algorithm='SAMME')
# es2 = AdaBoostClassifier(estimator=es1, n_estimators=100, learning_rate=5, algorithm='SAMME')
es2 = AdaBoostClassifier(estimator=es1, n_estimators=50, learning_rate=2, algorithm='SAMME.R')
es2.fit(x_train, y_train)
y_pre2 = es2.predict(x_test)
print(f"AdaBoost集成学习预测结果：{y_pre2}")
print(f"AdaBoost集成学习预测正确率：{accuracy_score(y_test, y_pre2)}")




