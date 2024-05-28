# the split() function
abc = "With three words"
stuff = abc.split()
print(stuff) # list of individual pieces
print(len(stuff))
print(stuff[0])

print(stuff)
for w in stuff:
    print(w)

# a bunch of spaces = single space
line = "a lot          of spaces"
etc = line.split()
print(etc)
# string without spaces
line = "first;second;third"
thing = line.split()
print(thing); print(len(thing))
# split based on semi-colons
thing = line.split(";")
print(thing); print(len(thing))

fhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From:"): continue
    words = line.split()
    print(words[2])


# the double split pattern
line = "From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008"
words = line.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])