# except block is triggered
astr = "hello bob"
try: istr = int(astr)
except: istr = -1
print("first", istr)

# except block is ignored
astr = "123"
try: istr = int(astr)
except: istr = -1
print("second", istr)


astr = "bob"
try:
    print("hello")
    istr = int(astr)
    print("there") # doesn't execute
except: istr = -1
print("done", istr)


rawstr = input("enter a number: ")
try: ival = int(rawstr)
except: ival = -1
if ival > 0: print("nice work!")
else: print("not a number")