"""
    需求：基于传入的文件，创建生成器，生产批次歌词
    分批加载歌词：  歌词  假设 8条为一个批次
"""
from math import ceil


# 定义函数   返回生成器
# batch_size：批次大小
def dataset_loader(batch_size):
    print("aaa")
    # 读取文件
    with open("day_05/geci.txt", "r", encoding="utf-8") as src_f:
        # 一次读取一行数据
        lines = src_f.readlines()
        print("111",type(lines))

        # 计算批次的总数   假设5批  每个批次8条  5*8 =   40 条函数
        # 之所以使用 math.ceil, 是因为考虑到可能最后歌词数不够8条，也算一个批次
        # ceil 向上取整函数
        # 总批次(total_batch) = ceil(len(lines) / batch_size)
        total_batch = ceil(len(lines) / batch_size)

        # 循环  获取到[每个批次]的数据 ， 放入到生成器中，并返回
        for idx in range(total_batch):
            # 取批次
            # 假设 total_batch 是5个批次  range(5)  则idx值  0   1   2   3   4
            # 第一批歌词  批次索引(idx=0)  歌词为：第1条~第8条  索引为 0~7
            # 第一批歌词  批次索引(idx=1)  歌词为：第9条~第16条  索引为 8~15
            # 第一批歌词  批次索引(idx=2)  歌词为：第17条~第24条  索引为 16~23
            # yield lines[0:8]      包左不包右       前面的值   idx  * batch_size
            # yield lines[8；16]     包左不包右      前面的值   idx  * batch_size
            yield lines[idx*batch_size:idx*batch_size+batch_size]

d1 =dataset_loader(8)
print(next(d1))

# for temp_batch in d1:
#     print(temp_batch)

