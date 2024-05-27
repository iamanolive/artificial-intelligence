name = input("Enter file:") # sequential
handle = open(name) # sequential

counts = dict() # sequential
for line in handle: # repeated
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None # sequential
bigword = None # sequential
for word, count in counts.items(): # repeated
    if bigcount is None or count > bigcount: # conditional
        bigword = word
        bigcount = count

print(bigword, bigcount) # sequential