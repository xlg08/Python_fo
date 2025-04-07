def insert_sort(my_list):
    n = len(my_list)
    for i in range(1, n):
        for k in range(1, i+1):
            j = i - k + 1
            if my_list[j] < my_list[j-1]:
                my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
            else:
                break


if __name__ == '__main__':
    my_list = [5, 3, 4, 7, 2]
    insert_sort(my_list)
    print(my_list)