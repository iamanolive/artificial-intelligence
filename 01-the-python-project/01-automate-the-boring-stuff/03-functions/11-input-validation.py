def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


print("enter number")

while True:
    try: number = int(input()); break
    except: print("enter an integer value")

while True:
    number = collatz(number)
    if number == 1: break