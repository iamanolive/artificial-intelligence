# evaluating expressions
print((5 > 4) and (3 == 5)) # false
print(not(5 > 4)) # false
print((5 > 4) or (3 == 5)) # true
print(not((5 > 4) or (3 == 5))) # false
print((True and True) and (True == False)) # false
print((not False) or (not True)) # true


# spam contains numbers
spam = int(input("what does spam contain? "))
if spam == 1: print("hello")
elif spam == 2: print("howdy")
else: print("greetings!")


# printing numbers using for loops
for i in range(1, 11):
    print(i)
# printing numbers using while loops
i = 1
while i < 11: 
    print(i)
    i = i + 1


# the absolute function
print(abs(75))
print(abs(-75))
print(abs(8.37))
print(abs(-8.3))