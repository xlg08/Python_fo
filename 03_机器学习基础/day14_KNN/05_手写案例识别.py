# 1.导包
import joblib
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier  # 导入KNN分类对象
from sklearn.model_selection import train_test_split, GridSearchCV  # 分割训练集和测试集 (7 3 & 8 2)

import pandas as pd
from collections import Counter

# 拓展：忽略警告
import warnings

# 参1：忽略警告
# 参2：忽略模块
warnings.filterwarnings('ignore', module='sklearn')


# 1.定义函数，接受用户传入的索引值，展示该索引值的对应图片
def show_digit(idx):
    # 1.读取数据，获取数据源
    df = pd.read_csv(r"../../data/手写数字识别.csv")
    # print(df)

    # 2.判断传入的索引是否越界
    if idx < 0 or idx > len(df) - 1:
        print('索引越界')
        return

    # 3.走到此处，说明索引没有越界，就能正常获取数据
    # iloc 根据索引来获取值
    # 格式：df.iloc[行号，列索引]
    x = df.iloc[:, 1:]
    y = df.iloc[:, 0]  # 获取所有数字

    # 4.查看每个数字到底有几种？在4W2000个数据中
    print(f"数字的种类：{Counter(y)}")
    print(f"像素的形状：{x.shape}")

    # 5.根据传入的索引值，获取该行的数据    （excel的第一行 label、pixel0 需要去掉这行）
    #   然后索引数字要从0开始
    # 故：想获取标签中的5值，实际传入的是多少？    是索引 8    索引从0开始
    print(f"传入的索引，对应的数字是{y[idx]}")

    # 6.绘制图片        把之前的(784, ) 转换成 (28,28)
    x = x.iloc[idx].values.reshape(28, 28)

    # 7.绘制灰度图形
    plt.imshow(x, cmap='gray')  # 灰度图
    plt.axis("off")  # 不显示坐标轴
    plt.show()  # 展示图象


# 2.定义函数，训练模型，保存模型到本地
def train_model():
    # 1.读取数据，获取数据源
    df = pd.read_csv(r"../../data/手写数字识别.csv")

    # 2.对数据进行预处理
    x = df.iloc[:, 1:]  # 获取特征列
    y = df.iloc[:, 0]  # 获取标签列
    # 2.2：拆分训练集和测试集
    # 参考y值进行抽取，划分训练集和测试集，保持标签的比例
    # 如果不设置这个，可能会出现抽取的测试值里面全部是某一个值
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=24, stratify=y)

    # 3.特征工程
    # 特征预处理 因为x是像素，范围是[0,255], y的数值是[0,9]
    # x_train = x_train / 255
    trainsfer = StandardScaler()
    x_train = trainsfer.fit_transform(x_train)
    x_test = trainsfer.transform(x_test)

    # 4.模型训练
    # 4.1：创建模型对象
    es = KNeighborsClassifier(n_neighbors=40)
    # 4.2：模型训练
    es.fit(x_train, y_train)

    # 5.模型评估
    print(f"准确率：{es.score(x_test, y_test)}")

    # 6.保存模型（保存到本地）
    # 参1：要保存那个模型
    # 参2：模型保存路径
    joblib.dump(es, '../../model/手写数字识别.pkl')  # pickle 文件 python(pandas)独有的文件类型
    print("模型保存成功!!")


# 3.定义函数：使用模型（测试模型）
def use_model():
    # 1.读取图片
    # img = plt.imread('../../data/demo.png')  # 28*28像素

    img = plt.imread('../../data/8.png')  # 28*28像素

    # img = plt.imread('../../data/a.png')  # 28*28像素
    # img.resize([28, 28])

    # print(img)  # [[像素1,像素2,像素3,像素4,像素5,像素6,...,像素28],[像素1,像素2,像素3,像素4,像素5,像素6,...,像素28],[像素1,像素2,像素3,像素4,像素5,像素6,...,像素28]]

    # 2.读取模型，加载模型对象
    knn = joblib.load('../../model/手写数字识别.pkl')
    # print(knn)

    # 3.模型预测
    # y_predict = knn.predict(img.reshape(1, -1))      # 1行   -1 无穷  ，后面有多少，就加载多少
    y_predict = knn.predict(img.reshape(1, 784))  # 1行    784列
    print(f"预测的是：{y_predict}")


if __name__ == '__main__':
    # 1.定义函数，接受用户传入的索引值，展示该索引值的对应图片
    # show_digit(11)

    # 2.定义函数，训练模型，保存模型到本地
    # train_model()

    # 3.定义函数：使用模型（测试模型）
    use_model()
