x = 0 
# ordered checking
if x < 2: print("small")
elif x < 10: print("Medium")
else: print("LARGE")
print("all done")


x = 5
# without an else-block
if x < 2: print("small")
elif x < 10: print("medium")
print("all done")


x = 20
# multiple elif blocks
if x < 2: print("Small")
elif x < 10: print("Medium")
elif x < 20: print("Big")
elif x < 40: print("Large")
elif x < 100: print("Huge")
else: print("Ginormous")


if x < 2: print("below 2")
elif x >= 2: print("two or more")
else: print("something else") # never executes


# order of elif blocks matters
if x < 2: print("below 2")
elif x < 20: print("below 20")
# everything below 10 is also below 20
elif x < 10: print("below 10") # never executes
else: print("something else")