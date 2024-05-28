# lists with three strings
friends = ["joseph", "glenn", "sally"]
carryon = ["socks", "shirt", "perfume"]


# square-bracket containers
print([1, 24, 76]) # integer list
print(["red", "yellow", "blue"]) # string list
print(["red", 24, 98.6]) # mixed data types
print([1, [5, 6], 7]) # nested list
print([]) # empty list


# looking inside lists
friends = ["joseph", "glenn", "sally"]
print(friends[1]) # zero-based index


# strings are immutable
fruit = "banana"
x = fruit.lower() # store return value
print(x) # fruit remains unchanged
# lists are mutable
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28 # item assignment
print(lotto)