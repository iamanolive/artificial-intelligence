han = open("mbox.txt")
for line in han:
    line = line.rstrip()
    wds = line.split()
    # guardian pattern
    if len(wds) < 3 or wds[0] != "From":
        continue
    print(wds[2])