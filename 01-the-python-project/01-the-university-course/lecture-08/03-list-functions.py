# the length function
greet = "hello bob"
print(len(greet))
x = [1, 2, "joe", 99]
print(len(x))


# the range function
print(range(4))
friends = ["joseph", "glenn", "sally"]
print(len(friends))
print(range(len(friends)))


# changing friends to range()
friends = ["joseph", "glenn", "sally"]
# original code
for friend in friends:
    print("happy new year", friend)
# using the range() function
for i in range(len(friends)):
    friend = friends
    print("happy new year", friend)