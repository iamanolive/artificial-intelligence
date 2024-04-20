def solution1(input_list):
    print("The given list is " + str(input_list))
    print("Divisible by 5")
    for i in range(len(input_list)):
        if input_list[i] % 5 == 0:
            print(input_list[i])

def solution2(input_list):
    print("The given list is " + str(input_list))
    print("Divisible by 5")
    for item in given_list:
        if not item % 5:
            print(item)

given_list = [10, 20, 33, 46, 55]
solution1(given_list)
solution2(given_list)