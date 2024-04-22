def solution1(number):
    return oct(number)

def solution2(number):
    return("%o" %(number))

input_decimal = int(input())
print(solution1(input_decimal))
print(solution2(input_decimal))