def solution(counter):
    for i in range(1, counter + 1):
        for j in range(1, i + 1):
            print(j, end = " ")
        print()

count = int(input())
solution(count)