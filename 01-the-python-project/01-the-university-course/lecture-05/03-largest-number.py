largest_so_far = None
print("before", largest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if largest_so_far == None or num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)
print("after", largest_so_far)