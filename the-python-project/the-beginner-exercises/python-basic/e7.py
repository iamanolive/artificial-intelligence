def solution1(string, substring):
    return string.count(substring)

def solution2(string, substring):
    result = 0
    for i in range(len(string)):
        if(string[i : i + len(substring)] == substring):
            result += 1
    return result
        

input_string = input()
input_substring = input()
substring_count1 = solution1(input_string, input_substring)
substring_count2 = solution2(input_string, input_substring)
print(input_substring + " appeared " + str(substring_count1) + " times")
print(input_substring + " appeared " + str(substring_count2) + " times")