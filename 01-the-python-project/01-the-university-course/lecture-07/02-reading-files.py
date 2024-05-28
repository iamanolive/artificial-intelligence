# counting lines
fhand = open("mbox.txt")
count = 0
for line in fhand:
    count = count + 1
print("line count:", count)


# the whole file
fhand = open("mbox.txt")
inp = fhand.read()
print(len(inp)) # character count
print(inp[:20])