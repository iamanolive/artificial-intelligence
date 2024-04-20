def solution(income):
    if income <= 10000:
        return 0
    elif income <= 20000:
        return (income - 10000) * 0.1
    else:
        return 1000 + (income - 20000) * 0.2

taxable_income = int(input())
print(solution(taxable_income))