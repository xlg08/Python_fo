def insert_sort(my_list):
    n = len(my_list)
    for i in range(n-1, 0, -1):
        for j in range(i-1, n-1, 1):
            # 具体的比较过程
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            else:
                # 走到次数，说明元素已经找到了自己的位置
                break

if __name__ == '__main__':
    # my_list = [5, 3, 4, 7, 2]
    my_list = [11,33,22,7,55,77,99,6]
    insert_sort(my_list)
    print(my_list)




