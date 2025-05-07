import numpy as np

def m1():
    # 创建一个一维数组
    data = np.array([1, 2, 3, 4, 5, 6])

    # 参数1 代表行数          参数2代表  列数
    # reshape_data = data.reshape(6, 1)

    # -1 特殊含义    自动计算行数
    # reshape_data = data.reshape(-1, 1)
    # 等价于
    reshape_data = data.reshape(len(data), 1)

    print(reshape_data)


def m2():
    a = np.array([[1], [2], [3]])
    b = np.array([[4], [5], [6]])
    new_data = np.hstack((a, b))
    print(new_data)


def m3():
    # 创建一个数组
    arr = np.array([4, 1, 3, 6, 2, 7])
    # np.argsort : 对数组进行排序并返回索引
    old_index = np.argsort(arr)

    print(f"原始数组: {arr}")
    print(f"{old_index}")
    print(arr[old_index])


if __name__ == '__main__':
    m3()
