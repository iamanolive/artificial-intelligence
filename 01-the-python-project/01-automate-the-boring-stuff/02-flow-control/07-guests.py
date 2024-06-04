name = ""
while not name:
    print("enter your name:")
    name = input()
    print("how many guests will you have?")
    num_of_guests = int(input())
    if num_of_guests:
        print("be sure to have room for all your guests")
print("done")