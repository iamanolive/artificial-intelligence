s = "monty python"
# pulling out string chunks
print(s[0:4]) # mont
print(s[6:7]) # p
print(s[6:20]) # python
# eliminating indices
print(s[:2]) # mo
print(s[8:]) # thon
print(s[:]) # monty python


# concatenation
a = "hello"
b = a + "there"
print(b) # single word
# explicit space concatenation
c = a + " " + "there"
print(c)


# in as a logical operator
fruit = "banana"
print("n" in fruit)
print("m" in fruit)
print("nan" in fruit)
if "a" in fruit: # true/false
    print("found it!")


# string comparison
word = "banana"
if word == "bananas":
    print("all right, banana.")
if word < "banana":
    print("your word, " + word + ", comes before banana.")
elif word > "banana":
    print("your word, " + word + ", comes after banana.")
else:
    print("all right, bananas.")


# string library
greet = "hello bob"
zap = greet.lower() # method call
print(zap)
print(greet)
print("Hi There".lower())


stuff = "hello world"
print(type(stuff))
print(dir(stuff))