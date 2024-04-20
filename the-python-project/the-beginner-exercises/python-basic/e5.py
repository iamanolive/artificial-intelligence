def solution(numbers):
    print("Given list: " + str(numbers))
    if numbers[0] == numbers[len(numbers) - 1]: 
        return True
    else:
        return False
    
numbers_x = [10, 20, 30, 40, 10]
print("The result is " + str(solution(numbers_x)))

numbers_y = [75, 65, 35, 75, 30]
print("The result is " + str(solution(numbers_y)))