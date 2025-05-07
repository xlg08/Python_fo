import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,classification_report

# print(os.getcwd())

data =pd.read_csv("../../data/churn.csv")
# print(data)
data.info()
dx_data =data.copy()


# dx_data.loc[dx_data['Churn']=='Yes','Churn']= 1
# dx_data.loc[dx_data['Churn']=='No','Churn'] =0



dx_data.Churn.replace("Yes", "1", inplace=True)
dx_data.Churn.replace("No", "0", inplace=True)


# print(dx_data)
dx_data.info()
# 特征列
dx_data_new=dx_data.iloc[:,9:]
print(dx_data_new)
# # 标签
dx_data_label=dx_data['Churn']
dx_data_label.info()
# # print(dx_data_label)
# # 数据是否有缺失值
# # print(np.all(pd.notnull(data)))
# # 缺失值分布
# # print(pd.isna(data).sum())
# # 缺失值的位置
# # miss_rows,miss_cols=np.where(data.isna())
# # miss_pos =list(zip(miss_rows,miss_cols))
# # print(miss_pos)
# # 查看某列是否有缺失值
# # print(data[data['landline'].isna()].index.tolist())
# # 填充缺失值
#导函数模型
x_train,x_test,y_train,y_test=\
    train_test_split(dx_data_new,dx_data_label,test_size=0.2,random_state=24)
#
# # 预处理量纲问题
# transfer =StandardScaler()
# x_train =transfer.fit_transform(x_train)
# x_test =transfer.transform(x_test)
# # print(x_train)
# # 训练逻辑回归算法模型
estimator =LogisticRegression()
estimator.fit(x_train,y_train)

y_pre = estimator.predict(x_test)
print("预测值：", y_pre)

print(f"准确率是：{accuracy_score(y_test, y_pre)}")

# # 训练完测试预测值
# y_test_pre =estimator.predict(x_test)
# # 评估模型精确率
# print(f'准确率{estimator.score(x_test,y_test)}')
# print(f'精确率{precision_score(y_test,y_test_pre)}')
# print(f'召回率{recall_score(y_test,y_test_pre)}')
# print(f'f1曲线{f1_score(y_test,y_test_pre)}')
# print(f'roc曲线{roc_auc_score(y_test,y_pre)}')
# 分类评估报告
# print(f'分类评估报告{classification_report(y_test,y_pre)}')






# x =DX_data.iloc[:,1:]
# y =DX_data.iloc[:,0]
# # print(x)
# # print(y)
# #处理数据
# x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=24)
# #标准化
# transfer =StandardScaler()
# transfer.fit_transform()







