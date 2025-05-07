'''

'''

import joblib  # 保存和加载模型的
import numpy as np
import pandas as pd
import xgboost as xgb  # 极限梯度提升树对象
from collections import Counter  # 统计数据
from sklearn.model_selection import train_test_split, GridSearchCV # 训练集和测试集划分
from sklearn.metrics import classification_report  # 模型评估和分配报告
from sklearn.model_selection import StratifiedKFold  # 分层K折交叉验证类似于网格搜索 cv=折数
from sklearn.utils import class_weight  # 计算样本的权重
from sklearn.preprocessing import LabelEncoder

# 通过 xgboost 极限梯度提升树完成对红酒品质的分类案例


def demo1_data_split():
    df = pd.read_csv('../../data/红酒品质分类.csv')
    # df.info()
    # print(df.head(5))
    # 找x轴
    x = df.iloc[:, :-1]  # 特征
    # 找y轴
    y = df.iloc[:, -1]  #

    print(x[:5])
    print(y[:5])
    print("查看标签结果的分布情况，是否均衡：\n", Counter(y))

    # 通过标签编码器  把标签列 转换为 数值列
    le = LabelEncoder()
    y = le.fit_transform(y)
    y = pd.DataFrame(y)

    # 切分训练集和测试集
    x_train, x_test, y_train, y_test = \
        train_test_split(x, y, test_size=0.1563, random_state=20, stratify=y)

    # 区分训练集和测试集
    pd.concat([x_train, y_train], axis=1).to_csv('../../data/红酒品质分类_train.csv', index=False)
    pd.concat([x_test, y_test], axis=1).to_csv('../../data/红酒品质分类_test.csv', index=False)


# 定义函数、训练模型、保存模型
def demo02_train_mode():
    # 1.读取训练集和读取测试集
    train_data = pd.read_csv("../../data/红酒品质分类_train.csv")
    test_data = pd.read_csv("../../data/红酒品质分类_test.csv")

    # 2.提取训练集和测试集中的数据特征 & 标签
    x_train = train_data.iloc[:, :-1]  # 除了最后一列，其他都是特征
    y_train = train_data.iloc[:, -1]  # 最后一列是特征

    x_test = test_data.iloc[:, :-1]
    y_test = test_data.iloc[:, -1]

    # 创建模型
    es = xgb.XGBClassifier(
        max_depth=5,  # 最大深度
        n_estimators=100,  # 树的数量
        learning_rate=0.1,  # 学习率
        random_state=24,
        objective='multi:softmax'  # 多分类问题，使用多分类模型
    )

    # 加入平衡权重，因为数据集样本不均衡
    class_weight.compute_sample_weight('balanced', y_train)

    # 模型训练
    es.fit(x_train, y_train)

    # 评估准确率
    print(f"准确率：{es.score(x_test, y_test)}")

    # 保存模型
    joblib.dump(es, "../../model/红酒的品质分类.pkl")

def demo3_use_model():
    # 1.读取训练集和读取测试集
    train_data = pd.read_csv("../../data/红酒品质分类_train.csv")
    test_data = pd.read_csv("../../data/红酒品质分类_test.csv")

    # 2.提取训练集和测试集中的数据特征 & 标签
    x_train = train_data.iloc[:, :-1]  # 除了最后一列，其他都是特征
    y_train = train_data.iloc[:, -1]  # 最后一列是特征

    x_test = test_data.iloc[:, :-1]
    y_test = test_data.iloc[:, -1]

    # 加载模型
    es = joblib.load('../../model/红酒的品质分类.pkl')

    param_dict = {
        'learning_rate': [0.01, 0.3, 0.5, 0.8, 1.0, 1.2, 1.5],
        'n_estimators': [50, 60],
        'max_depth': [3, 5, 8, 10, 15, 20]
    }

    # 创建分层采样
    # n_splits 折数           shuffle 是否打乱数据
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=2)
    gs_es = GridSearchCV(es, param_dict, cv=skf)
    gs_es.fit(x_train, y_train)

    y_pre = gs_es.predict(x_test)
    print(f"预测值：{y_pre}")

    # 打印模型评估系数
    print(f"最优评分：{gs_es.best_score_}")
    print(f"最优参数：{gs_es.best_params_}")
    print(f"准确率：{gs_es.score(x_test, y_test)}")


if __name__ == '__main__':
    # demo1_data_split()
    # demo02_train_mode()
    demo3_use_model()