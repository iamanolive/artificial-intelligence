# the find() method
fruit = "banana"
pos = fruit.find("na")
print(pos) # 2
aa = fruit.find("z")
print(aa) # -1


# the upper() method
greet = "Hello Bob"
nnn = greet.upper()
# does not change the original
print(nnn) # HELLO BOB
# the lower() method
www = greet.lower()
print(www) # hello bob


# the replace() method
greet = "hello bob"
nstr = greet.replace("bob", "jane")
print(nstr) # hello jane
nstr = greet.replace("o", "X")
print(nstr) # hellX bXb


# stripping whitespace (\t, \n)
greet = "    hello bob         "
print(greet.lstrip()) # left strip
print(greet.rstrip()) # right strip
print(greet.strip()) # strip both sides


# the startswith() method
line = "please have a nice day"
print(line.startswith("please")) # true
print(line.startswith("P")) # false