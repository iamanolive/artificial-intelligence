def solution1(string):
    print("Original string is " + string)
    print("Printing only even index chars")
    for i in range(0, len(string), 2):
        print(string[i])

def solution2(string):
    print("Original string is " + string)
    print("Printing only even index chars")
    for i in range(len(string)):
        if i % 2 == 0:
            print(string[i])

original_string = input()
solution1(original_string)
solution2(original_string)