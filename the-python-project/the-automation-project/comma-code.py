def solution(list_value):
    result = ""
    for i in range(len(list_value) - 1):
        result += list_value[i] + ", "
    result += "and " + list_value[len(list_value) - 1]
    return result

item_count = int(input("how many items would you like your list to contain? "))
input_list = []

for i in range(item_count):
    item = input("Enter item " + str(i + 1) + ": ")
    input_list.append(item)

print(solution(input_list))