def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
    
while True:
    try:
        input_number = int(input())
        break
    except:
        print("Enter an integer value as input")
    
while True:
    input_number = collatz(input_number)
    print(input_number)
    if input_number == 1:
        break