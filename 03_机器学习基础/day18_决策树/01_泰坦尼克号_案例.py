import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

from sklearn.preprocessing import StandardScaler

"""
    决策树分层
"""
# 1 读取数据
train_df = pd.read_csv('../../data/train.csv')

# print(train_df.head(5))
# train_df.info()

# 2.数据预处理
# 2.1：获取特征列 和 标签列       船舱等级、性别、年龄
x = train_df[['Pclass', 'Sex', 'Age']]
y = train_df['Survived']

# 2.2：用age处理   age列求平均值
x['Age'] = x['Age'].fillna(x['Age'].mean())

# 2.3：查看数据
# x.info()
# print(x.head(5))

# 分析 age 需要处理  采用热编码
x = pd.get_dummies(x)
# print(x.head(5))
x.drop('Sex_male', axis=1, inplace=True)
print(x.head(5))

# 拆分训练集和测试集
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.152, random_state=20)
print(x_train.head(5))

# 是否需要特征工程
# trainfer = StandardScaler()
# x_train = trainfer.fit_transform(x_train)
# x_test = trainfer.transform(x_test)


# 是否需要特征工程
es = DecisionTreeClassifier()
es.fit(x_train, y_train)

y_pre = es.predict(x_test)
print("预测结果：", y_pre)       # 0： 已故            1： 活着


# 模型评估
print(f"准确率：{es.score(x_test, y_test)}")
print(f"分类报告：{classification_report(y_test, y_pre, target_names=['Died', 'Survivor'])}")

# 绘制
# 设置画布大小
plt.figure(figsize=(80, 50))

# 绘制决策树
#         filled 填充颜色    max_depth 层数
plot_tree(es, max_depth=15, filled=True)

# 保存图片
plt.savefig('../../data/train_img.png')

plt.show()

