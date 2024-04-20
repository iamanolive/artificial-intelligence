def solution1(string, n):
    result = ""
    for i in range(len(string)):
        if i >= n:
            result += string[i]
    return result

def solution2(string, n):
    return string[n:]

print(solution1("pynative", 2))
print(solution2("pynative", 4))