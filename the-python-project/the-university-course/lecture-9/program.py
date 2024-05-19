han = open("mbox.txt")

for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) > 0 and wds[0] != "from":
        continue
    print(wds[2])