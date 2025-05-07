from sklearn.neighbors import KNeighborsRegressor

'''
    当样本数大于5时使用的是ball树搜索，小于等于5时使用的暴力搜索，导致的样本数变化值不同
'''
knn1 = KNeighborsRegressor(n_neighbors=2)
x_train_1 = [[2], [2], [3], [9], [5], [7]]
y_train_1 = [8, 2, 3, 4, 5, 99]
knn1.fit(x_train_1, y_train_1)

x_test = [[3]]
y_test = knn1.predict(x_test)
print(y_test)
distances, indices = knn1.kneighbors(x_test)
print("最近的邻居索引:", indices)
print("最近的邻居距离:", distances)
print("对应的邻居目标值:", [y_train_1[i] for i in indices[0]])
print("预测值:", knn1.predict(x_test))
print('使用的算法：', knn1._fit_method)

knn2 = KNeighborsRegressor(n_neighbors=2)

x_train_2 = [[2], [2], [3], [9], [5]]
y_train_2 = [8, 2, 3, 4, 5]
knn2.fit(x_train_2, y_train_2)

x_test = [[3]]
y_test = knn2.predict(x_test)
print(y_test)
# 预测并输出邻居信息
distances, indices = knn2.kneighbors(x_test)
print("最近的邻居索引:", indices)
print("最近的邻居距离:", distances)
print("对应的邻居目标值:", [y_train_2[i] for i in indices[0]])
print("预测值:", knn2.predict(x_test))
print('使用的算法：', knn2._fit_method)


# 大模型：      -->     k=2 当两个值相同时，随机选

# 实际测试：当老numpy版本时(例如 1.24.4)，
#   当k=2 且两个样本的特征值相同时，会选择索引值小的哪个样本的标签

#   老numpy版本(例如 1.24.4)时，底层使用的快排，(不稳定)
#   新numpy版本(例如：2.2.4)时，底层使用的 Timsort，(效率高，稳定)
