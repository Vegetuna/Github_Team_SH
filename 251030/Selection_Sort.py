def selection_sort(data_list, descending=False):
    n = len(data_list)

    for i in range(n-1):
        target_index = i

        for j in range(i+1, n):
            if descending:
                if data_list[j] > data_list[target_index]:
                    target_index = j
                else:
                    if data_list[j] < data_list[target_index]:
                        target_index = j

        data_list[i], data_list[target_index] = data_list[target_index], data_list[i]

    return data_list
