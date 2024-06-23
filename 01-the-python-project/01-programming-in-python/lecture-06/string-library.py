# the lower() method
greet = "Hello, Bob"
zap = greet.lower()
print(zap)
print(greet)
print("Hi There".lower())

stuff = "Hello world"
print(dir(stuff))

# the find() method
fruit = "banana"
position = fruit.find("na")
print(position)
aa = fruit.find("z")
print(aa) # not found

# the upper() method
greet = "Hello World"
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)

# the replace() method
greet = "Hello Bob"
nstr = greet.replace("Bob", "Jane")
print(nstr)
nstr = greet.replace("o", "X")
print(nstr)

# stripping whitespace
greet = "    Hello Bob  "
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

# the startswith() method
line = "please have a nice day"
print(line.startswith("please"))
print(line.startswith("P"))