'''
    标准化介绍：
        概述：特征预处理一种方案
        公式： x' = (x - 该列平均值) / 该列的标准差
        公式解释：
            x --> 某特征列的某个具体的值 即：原值
            mean --> 该列的平均值
        应用场景：比较合适的大数据集的应用场景。当数据量比较大的时候
            受最大值和最小值的影响会微乎其微。
        总结：
            无论是归一化，还是标准化，目的都是避免因为特征列的量纲问题，导致权重不同
            从而影响预测结果
'''
# 1.导包
from sklearn.preprocessing import StandardScaler        # 标准化的类

# 2.准备特征数据      每个子列表 = 1个样本
data = [[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]]
data1 = [[90, 2, 10], [60, 4, 15], [75, 3, 13]]

# 3.创建标准化对象     （没有默认的生成区间）
transfer = StandardScaler()

# 4.具体的 标准化动作
new_data = transfer.fit_transform(data)
new_data1 = transfer.fit_transform(data1)

# 5.显示标准化结果
print(f"标准化后的数据集：\n{new_data}")


# 6.获取平均值和标准差
print(f"平均值：{transfer.mean_}")
print(f"标准差：{transfer.scale_}")