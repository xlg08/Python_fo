import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, \
    classification_report


# def 非热编码数据清洗():
#     data = pd.read_csv("../data/churn.csv")
#     # data.info()
#     gender_datas = data['gender'].map({'Female':0,'Male':1})
#     Churn_datas = data['Churn'].map({'No':0,'Yes':1})
#     data['gender_s']=gender_datas
#     data['Churn_']=gender_datas
#     data.drop('gender',axis=1,inplace=True)
#     data.drop('Churn',axis=1,inplace=True)
#     # print(datas)
#     data.info()
#     # print(data.head(4))


def dm1_数据预处理():
    data = pd.read_csv('../data/churn.csv')
    # data.info()
    print(data.Churn.value_counts())
    # 标签：客户流失情况  churn   数据是什么样 ？
    # ？？？  查看值（伴侣属性 、固定电话（））
    # print(data.head(5))  # 是  否

    # 演示热编码
    # 背景 ： churn  gender 字符串类型
    # data.info()
    # data = pd.get_dummies(data)
    # # data.info()
    # print(data.head(5))
    #
    # #热编码后删除多余的字段
    # data.drop(['gender_Male','Churn_No'],axis=1,inplace=True)
    # # data.info()
    #
    # #我们修改标签的名字
    # data.rename(columns={'Churn_Yes':'flag'},inplace=True)
    # data.info()
    #


def dm2_逻辑回归模型训练与评估():
    # 1、读取数据
    data = pd.read_csv("../../data/churn.csv")
    # 2、对数据进行处理
    data = pd.get_dummies(data)
    # 热编码后删除多余的字段
    data.drop(['gender_Male', 'Churn_No'], axis=1, inplace=True)
    # 我们修改标签的名字
    data.rename(columns={'Churn_Yes': 'flag'}, inplace=True)
    # 3、选择特征   (找业务去确定)
    x = data[['PaymentElectronic', 'Contract_Month', 'MonthlyCharges']]
    y = data['flag']
    # 训练集和测试切分
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=20)

    es = LogisticRegression()
    es.fit(x_train, y_train)

    # 模型预测
    y_pre = es.predict(x_test)
    # print(f"预测值{y_pre}")

    # 模型评估
    print(f"准确率{es.score(x_test, y_test)}")
    print(f"精确率{precision_score(y_test, y_pre, pos_label=False)}")
    # print(f"召回率{recall_score(y_test,y_pre,pos_label='True')}")
    # print(f"f1值{f1_score(y_test,y_pre,pos_label='True')}")
    # print(f"roc曲线{roc_auc_score(y_test,y_pre,pos_label='True')}")

    # 分类评估报告
    # sklearn.metrics.classification_report(y_true, y_pred, labels=[], target_names=None)
    # y_true：真实目标值
    # y_pred：估计器预测目标值
    # labels:指定类别对应的数字
    # target_names：目标类别名称
    print(f"分类评估报告{classification_report(y_test, y_pre)}")
    # return：每个类别精确率与召回率


if __name__ == '__main__':
    # 非热编码数据清洗()
    # dm1_数据预处理()
    dm2_逻辑回归模型训练与评估()
