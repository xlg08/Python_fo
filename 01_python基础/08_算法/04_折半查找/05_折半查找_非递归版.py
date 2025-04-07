"""
    二分（折半）查找
        概述：
            属于查找类的算法，相对来说效率比较高。时间复杂度 O(logn)
        前提：
            列表必须有序
        原理：
            1.比较 要查找的元素和列表中的值，如果一样则返回True。程序结束
            2.如果 要查找的元素比中值小，去前半段（中值前）查找
            3.如果 要查找的元素比中值大，去后半段（中值后）查找
            4.重复上述动作，直至找完。如果找完了，还没找到。就返回False
"""

# my_list 原列表 target 要查找的目标值
def binary_search_not_re(my_list, target):
    start = 0
    end = len(my_list) - 1
    # 循环查找，只要条件就一直找
    while start <= end:
        # 计算中间值
        mid = (start + end) // 2
        print(mid)
        # 比较 要查找的元素 和中值
        if my_list[mid] == target:
            return True
        elif target < my_list[mid]:
            # 如果要查找的元素比中值小，去前半段（中值前）查找 end
            end = mid - 1
        else:
            start = mid + 1
    # 走到此处，说明都遍历完了，还没有找到，返回False
    return False



if __name__ == '__main__':
    my_list = [2, 3, 4, 5, 6]
    print(binary_search_not_re(my_list, 2))

