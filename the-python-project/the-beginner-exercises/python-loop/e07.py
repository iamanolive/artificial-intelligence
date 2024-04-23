def solution(count):
    for i in range(count, 0, -1):
        for j in range(i, 0, -1):
            print(j, end = " ")
        print()
        
counter = int(input())
solution(counter)