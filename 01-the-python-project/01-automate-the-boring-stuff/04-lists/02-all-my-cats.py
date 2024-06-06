catnames = []
while True:
    print("enter the name of cat", end = " ")
    print(str(len(catnames) + 1), end = " ")
    print("(or enter nothing to stop)")
    name = input()
    if name == "": break
    catnames = catnames + [name] # list concatenation
print("the cat names are")
for name in catnames:
    print(" " + name)