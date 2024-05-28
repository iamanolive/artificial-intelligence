# summing the numbers as they appear
total = 0; count = 0
while True: # uses less memory
    inp = input("enter a number: ")
    if inp == "done": break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print("average:", average)


# appending numbers to a list
numlist = list()
while True: # uses more memory
    inp = input("enter a number: ")
    if inp == "done": break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print("average:", average)