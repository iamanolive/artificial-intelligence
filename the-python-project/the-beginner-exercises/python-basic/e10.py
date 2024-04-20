def solution(input_list_1, input_list_2):
    result_list = []
    for item in input_list_1:
        if item % 2:
            result_list.append(item)
    for item in input_list_2:
        if not item % 2:
            result_list.append(item)
    return result_list


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list: " + str(solution(list1, list2)))