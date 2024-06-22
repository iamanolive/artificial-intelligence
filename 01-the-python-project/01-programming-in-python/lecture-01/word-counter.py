name = input("enter file:") # sequential
handle = open(name) # sequential

counts = dict() # sequential
for line in handle: # repeated
    words = line.split() # repeated
    for word in words: # repeated
        counts[word] = counts.get(word, 0) + 1 # repeated

bigcount = None # sequential
bigword = None # sequential
for word, count in counts.items(): # repeated
    if bigcount is None or count > bigcount: # conditional
        bigword = word # conditional
        bigcount = count # conditional

print(bigword, bigcount) # sequential