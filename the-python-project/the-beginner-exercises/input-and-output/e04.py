def solution1(number):
    return "{0:.2f}".format(number)

def solution2(number):
    return("%.2f" %(number))

number = float(input())
print(solution1(number))
print(solution2(number))