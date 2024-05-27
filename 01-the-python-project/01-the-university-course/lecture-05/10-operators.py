# the "is" operator (equal in type and value)
smallest_so_far = None
print("before", smallest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None or num < smallest_so_far:
        smallest_so_far = num
    print(smallest_so_far, num)
print("after", smallest_so_far)


print(0 == 0.0) # true (conversion)
print(0 is 0.0) # false (no conversion)