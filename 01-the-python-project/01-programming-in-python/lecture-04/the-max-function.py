print(max("hello world"))

def max(input):
    current_largest = input[0]
    for x in input:
        if x > current_largest:
            current_largest = x
    return current_largest

print(max("hello world"))