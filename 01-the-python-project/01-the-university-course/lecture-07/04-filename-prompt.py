fname = input("enter the file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("there were", count, "subject lines in", fname)


# try-except blocks
fname = input("enter the file name: ")
try:
    fhand = open(fname)
except:
    print("file cannot be opened:", fname)
    quit() # stop executing
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("there were", count, "subject lines in", fname)