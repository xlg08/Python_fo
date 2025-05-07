import numpy as np  # 数学计算包
import pandas as pd  # 数据处理包
import matplotlib.pyplot as plt  # 画图包
import jieba  # 分词包
from sklearn.feature_extraction.text import CountVectorizer  # 词频统计包, 把评论内容 转成 词频矩阵.
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB  # 朴素贝叶斯对象


# 1.读取数据文件，获取原始数据集
df_book = pd.read_csv(r'../../data/书籍评价.csv', encoding='gbk')
# print(df_book)
# df_book.info()


# 数据预处理
# 1.处理标签
df_book['labels'] = np.where(df_book['评价'] == '好评', 1, 0)
# df_book.info()
# 2.抽取标签列，作为：标签
y = df_book['labels']

# x数据处理
# jieba.lcut(df_book['内容'])     # 报错
# 当前的格式 [[],[],[], ....]
test = [','.join(jieba.lcut(line)) for line in df_book['内容']]
# 数据格式 ：['第一条评论切片', '第二条评论切片', ... ]
# print(test)

# 加载停用词列表，即：里面记录的词，不需要参考模型训练  的 啊 哈  ...
with open(r"../../data/stopwords.txt", 'r', encoding='utf-8') as src_f:
    # 一次读取所有的行
    stopwords_list = src_f.readlines()
    # print(stopwords_list)
    #   : 删除最后 \n
    stopwords_list = [line.strip() for line in stopwords_list]
    # print(stopwords_list)
    stopwords_list = list(set(stopwords_list))
    print("*" * 50)
    print("停用词：\n", stopwords_list)
    print("*" * 50)


# 创建向量化对象，从评论切词列表中删除停用词。并且统计词频矩阵 (单词矩阵)
#   词频矩阵(单词矩阵)：
transfer = CountVectorizer(stop_words=stopwords_list)
print("*" * 50)
print("向量化对象：\n", transfer)
# 统计词频矩阵 先训练后转换  转换为数组
# transfer.fit(test)
# x = transfer.transform(test)

print("*" * 50)
# print("1", test)
for i in test:
    print(i)
# x = transfer.fit_transform(test).toarray()
x = transfer.fit_transform(test)
print("*" * 50)
print(x)
x = x.toarray()
print("*" * 50)
print("词频矩阵：\n", x)     # 词频矩阵
# print(x)


print("*" * 50)
# 看一下，13条评估 切词 ， 删除 停用词后 ， 一共还剩下多少词
print("还剩下的词：\n", pd.DataFrame(transfer.get_feature_names_out()))


print("*" * 50)
# 13条评论  切词  、 且删除停用词， 一共多少词？
print("一共还剩下多少个：", len(transfer.get_feature_names_out()))
print("形状：\n", transfer.get_feature_names_out().shape)


# 因为13条      前十条当作训练集    后三当作测试集
x_train = x[:10]
y_train = y[:10]
print("特征个数：\n", len(x_train[0]))       # 37 个特征
print("训练集的x：\n", x_train)
print("训练集的y：\n", y_train)


x_test = x[10:]
y_test = y[10:]
print("测试集的x：\n", x_test)
print("测试集的y：\n", y_test)


# 模型训练
es = MultinomialNB()
es.fit(x_train, y_train)


# 模型预测
y_pre = es.predict(x_test)
print(f"模型预测结果：{y_pre}")

print(f"准确率：{accuracy_score(y_test, y_pre)}")


# 演示字符串 join 函数用法
# mylist = ['aa', 'bb', 'cc']
# print(','.join(mylist))


# ci = []
# with open(r"../../data/stopwords.txt", 'r') as fr:
#     _ = fr.read()
#     ci.append(_)
# print(ci)

# content = df_book.内容.tolist()
# # print(content)

# for i in content:
#     str = jieba.lcut(i)
#     # 去掉停用词
#     print([i for i in str if i not in ci and i.strip() != ''])

