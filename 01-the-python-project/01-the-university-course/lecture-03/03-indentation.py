x = 5
if x > 2:
    print("bigger than 2")
    print("still bigger")
print("done with 2")

for i in range(5):
    print(i)
    if i > 2: # nested indentation
        print("bigger than 2")
    print("done with i", i)
print("all done")


x = 42
if x > 1:
    print("more than 1")
    if x < 100: # nested if-block
        print("less than 100")
print("all done") # double deindent