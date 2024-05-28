# fixed file search
fhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)


# skipping with continue
fhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    print(line)


# selecting lines with "in"
fhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    if not "@utc.ac.za" in line:
        continue
    print(line)