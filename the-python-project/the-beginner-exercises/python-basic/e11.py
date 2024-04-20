def solution():
    result = ""
    integer = input()
    for i in range(len(integer) - 1, -1, -1):
        result += integer[i] + " "
    return result

print(solution())