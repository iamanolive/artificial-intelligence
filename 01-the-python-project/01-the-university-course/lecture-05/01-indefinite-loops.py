# the while loop
n = 5 # iteration variable
while n > 0: # until not false
    print(n)
    n = n - 1
print("blastoff!")
print(n)


# an infinite loop
n = 5
while n > 0: # always true
    print("lather")
    print("rinse")
print("dry off!")


n = 0 # false condition
while n > 0:
    # while loop never entered
    print("lather")
    print("rinse")
print("dry off!")


# breaking out of loops
while True:
    line = input("> ")
    if line == "done":
        break # no going back
    print(line)
print("done!")


# continue
while True:
    line = input("> ")
    if line[0] == "#":
        continue # stop this iteration
        # go back to top
    if line == "done":
        break
    print(line)
print("done!")