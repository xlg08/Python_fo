
import pandas as pd
import numpy as np

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, classification_report

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score




data = pd.read_csv("../../data/churn.csv")

# data.loc[data['Churn'] == 'Yes', 'Churn'] = 1
# data.loc[data['Churn'] == 'No', 'Churn'] = 0
# data.loc[data['gender'] == 'Male', 'gender'] = 1
# data.loc[data['gender'] == 'Female', 'gender'] = 0

data.Churn.replace("Yes", "1", inplace=True)
data.Churn.replace("No", "0", inplace=True)
data.gender.replace("Female", "1", inplace=True)
data.gender.replace("Male", "0", inplace=True)



x = data.iloc[:, 1:]
y = data.iloc[:, 0]

x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.1563, random_state=20)


es = LogisticRegression()
es.fit(x_train, y_train)

y_pre = es.predict(x_test)
print("预测值：", y_pre)

print(f"准确率是：{accuracy_score(y_test, y_pre)}")




