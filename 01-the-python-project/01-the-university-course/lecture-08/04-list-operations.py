# list concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b # object-oriented approach
print(c); print(a)


# list slicing
t = [9, 41, 12, 3, 74, 15]
print(t[1:3]) # 1 to 3 (not included)
print(t[:4]) # upto not including 4
print(t[3:]) # three onwards
print(t[:]) # the whole list


# the "in" operator
some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)