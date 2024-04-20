def solution(size):
    for i in range(size, 0, -1):
        print("* " * i)


pattern_size = int(input())
solution(pattern_size)