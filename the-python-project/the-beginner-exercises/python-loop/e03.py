def solution1(number):
    result = (number * (number + 1)) / 2
    return int(result)

def solution2(number):
    result = 0
    for i in range(number + 1):
        result += i
    return result

def solution3(number):
    return sum(range(1, number + 1))

input_number = int(input())
print(solution1(input_number))
print(solution2(input_number))
print(solution3(input_number))