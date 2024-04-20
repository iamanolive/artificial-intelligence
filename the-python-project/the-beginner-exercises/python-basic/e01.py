def solution(num1, num2):
    if (num1 * num2 <= 1000):
        return num1 * num2
    else:
        return num1 + num2
    
n1 = input("number1 = ")
n2 = input("number2 = ")

print("The result is " + str(solution(int(n1), int(n2))))