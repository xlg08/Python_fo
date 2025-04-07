'''
    @User: LG
    @Auther: http://www.xlonggang.cn
    @Date: 2025/4/6 0006 18:02 
    @Description: 
    @Project ：HaskMaProject 
    @File    ：03_numpy_ndarray.py
    @version: 1.0
'''

import pandas as pd
import numpy as np

# 创建ndarray对象
# 1.array()函数：可以把python的列表转换为->ndarray对象
my_list = [11,22,33,44,55,66]
print(type(my_list))

# 2.把python列表传入 array()  ---->  ndarray对象
arr1 = np.array(my_list)
print(type(arr1))