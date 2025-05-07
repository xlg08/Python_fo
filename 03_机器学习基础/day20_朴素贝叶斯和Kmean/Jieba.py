import jieba

str1 = '我饿了'

str2 = '吃嘛不吃不吃就不吃'

str3 = '释迦摩尼吃释迦果'

str4 = '吃饭吗我去我不去'


print(jieba.lcut(str1))
print(jieba.lcut(str2))
print(jieba.lcut(str3))
print(jieba.lcut(str4))