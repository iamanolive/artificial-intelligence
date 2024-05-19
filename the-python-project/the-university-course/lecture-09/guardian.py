han = open("mbox.txt")

for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) > 2 or wds[0] != "from":
        continue
    print(wds[2])