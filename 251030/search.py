def linearSearch(data_list, target):
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    return -1

test_list = [5,2,8,1,9,4]
target1 = 8
index1 = linearSearch(test_list, target1)
target2 = 10
index2 = linearSearch(test_list, target2)

print(f"target1:{target1}, index1: {index1}")
print(f"target2: {target2}, index2: {index2}")