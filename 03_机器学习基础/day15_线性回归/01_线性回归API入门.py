'''
    线性回归解释：
        用来描述1个或者多个自变量（特征）和因变量（标签）之间关系。进行建模分析
    分析：
        一元线性回归：
            1个特征值   1个标签
        多元线性回归：
            多个特征    1个标签
    应用场景：
        有特征、有标签。且标签是连续的
    线性回归公式：
        一元线性回归： y=kx+b = wx + b
        多元线性回归：y=w的转置 * x + b
    名词解释：
        关于 y=kx+b
            k：斜率，在机器学习中叫 权重  简称 w
            b：截距，在机器学习中叫 偏置  简称 b

    回顾机器学习实现步骤：
        1.获取数据（导包）
        2.数据预处理
        3.特征工程
        4.模型训练
        5.模型预测
        6.模型评估
'''

from sklearn.linear_model import LinearRegression

# 1.准备数据集
x_train = [[160], [166], [172], [174], [180]]
y_train = [56.3, 60.6, 65.1, 68.5, 75]

# 测试数据
x_test = [[176]]

# 2.创建线性回归模型
es = LinearRegression()

# 3.模型训练
es.fit(x_train, y_train)

# 4.模型进行预测
y_pre = es.predict(x_test)
print(f"预测值为{y_pre}")

print(f"权重：{es.coef_}")
print(f"偏置：{es.intercept_}")
