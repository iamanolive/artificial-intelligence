numbers = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, len(numbers)):
    print("Current Number " + str(numbers[i]), end = " ")
    print("Previous Number " + str(numbers[i - 1]), end = " ")
    print("Sum: " + str(numbers[i] + numbers[i - 1]))