# declare empty list
x = list() # constructor form
print(type(x)); print(dir(x))


# the append() method
stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)
stuff.append("cookie")
print(stuff)


# the sort() function
friends = ["joseph", "glenn", "sally"]
friends.sort() # sorts the list in place
print(friends) # lists are ordered
print(friends[1])


# other built-in functions
nums = [3, 41, 12, 9, 74, 15]
# lists as arguments
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums) / len(nums)) # average