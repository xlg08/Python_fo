# 数据处理与统计分析

## 第一阶段 ： Numpy

### 1.创建数组

> np.arange(15).reshape(3,5)
> 
> np.array()
> 


## 第二阶段 ： Pandas

### 1.数据类型

### 2.基本操作
    
#### 1.去除不需要的元素
        dataframe.drop(columns=[列名1, 列名2, ..])

#### 2.通过索引获取元素
##### 场景一：根据行列索引来获取元素    先列后行
##### 场景二：结果loc 和iloc
            根据行索引 和 列名来获取元素
            格式：  df.loc[行索引, 列名]
            格式：  df.iloc[行号, 列索引]
        
##### 取多个数据:
            df.iloc[行号:行号, 列索引:列索引]
            df.loc['行索引':'行索引', ['列名','列名']]
    
#### 3.赋值操作
        df['列名'] = 23
        df.列名 = 22.5        # 此处列名不能存在空格
    
#### 4.排序操作
        格式：sort_values()
        ascending 参数 为True 为升序    False为降序    默认为True
        by 参数 为按哪一列进行排序
        df.sort_values(by='列名', ascending=False)
        df.open.sort_values()       # 对df的open进行排序
        df.sort_index(ascending=True)       # 对索引进行排序

#### 5.基本元素算术运算

#### 6.逻辑运算      & 、 /

#### 7.筛选固定值  isin

#### 8.统计运算

### 自定义函数

    目前使用的都是pandas已经提供好的函数，sum、max、min
    要传入一组数据，按照自身业务规则进行运算，apply函数！！！
    格式：df.apply(自定义函数， axis=0)  0列    1行

## 第三阶段：pandas 和 MySQL 数据库交互

### 1.先安装与数据库交互所需要的python包

    pip install pymysql==1.0.2 -i https://pypi.tuna.tsinghua.edu.cn/simple/
    如果后边的代码运行提示找不到sqlalchemy的包，和pymysql一样进行安装即可
    pip install sqlalchemy==2.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple/

### 2.


