smallest_so_far = 100000000
print("before", smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print("after", smallest_so_far)

smallest = None
print("before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("after", smallest)