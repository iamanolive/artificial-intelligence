greet = "Hello Bob"
zap = greet.lower()
print(zap)
print(greet)
print("Hi There".lower())

stuff = "Hello World"
print(type(stuff))
print(dir(stuff))

fruit = "banana"
pos = fruit.find("na")
print(pos)
aa = fruit.find("z")
print(aa)

nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)

nstr = greet.replace("Bob", "Jane")
print(nstr)
nstr = greet.replace("o", "x")
print(nstr)

greet = "     Hello Bob   "
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

line = "please have a nice day"
print(line.startswith("please"))
print(line.startswith("P"))