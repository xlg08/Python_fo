import time
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        # 找到最小值的索引
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_index][0]:  # 只比较第一个元素
                min_index = j
                time.sleep(1)
        # 如果发现更小的值，则交换
        if min_index != i:
            print(f'交换 i={i} 最小值索引={min_index} ', arr[min_index], arr[i], i)
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print('交换后', arr)
    return arr


if __name__ == '__main__':
    arr = [(1, 'c'), (3, 'a'), (2, 'c'), (3, 'e'), (2, 'd')]
    print('原始数组:', arr)
    sorted_arr = selection_sort(arr)
    print('最终结果:', sorted_arr)

    print("♥"*50)

    arr = [(1, 'c'), (3, 'a'), (1, 'b'), (2, 'c'), (1, 'd'), (5, 'e'), (2, 'd'), (4, 'e')]
    print('原始数组:', arr)
    sorted_arr = selection_sort(arr)
    print('最终结果:', sorted_arr)

