def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
    
input_number = int(input())
    
while True:
    input_number = collatz(input_number)
    print(input_number)
    if input_number == 1:
        break