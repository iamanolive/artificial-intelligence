fname = input("enter file: ")
if len(fname) < 1:
    fname = "clown.txt"
handle = open(fname)




di = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        print("**", word, di.get(word, -99))
        if word in di:
            di[word] = di[word] + 1
            print("**EXISTING**")
        else:
            di[word] = 1
            print("**NEW**")
        print(word, di[word])

print(di)




di = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        oldcount = di.get(word, 0)
        print(word, "old", oldcount)
        newcount = oldcount + 1
        di[word] = newcount
        print(word, "new", newcount)
print(di)




largest = -1
theword = None
for k, v in di.items():
    if v > largest:
        largest = v
        theword = k
print(theword, largest)

print("done")