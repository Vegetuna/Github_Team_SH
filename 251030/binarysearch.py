def binary_search(data_list, target):
    low = 0
    high = len(data_list) - 1

    while low <= high:
        mid = (low+high) // 2

        if data_list[mid] == target:
            return mid
        elif data_list < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

my_list = [1, 4, 8, 9, 11, 15 ,20]
target_1 = 11
target_2 = 10

index_1 = binary_search(my_list, target_1)
print(f"리스트 : {my_list}")
print(f"타겟 데이터 : {target_1}, 인덱스 : {index_1}")

index_2 = binary_search(my_list, target_2)
print(f'목표값 {target_2}의 인덱스 : {index_2}')