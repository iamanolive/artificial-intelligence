def solution1(number):
    return len(number)

def solution2(number):
    counter = 0
    number = int(number)
    while number > 0:
        counter += 1
        number //= 10
    return counter


input_number = input()
print(solution1(input_number))
print(solution2(input_number))