current_largest = None
print("before", current_largest)
for the_num in [9, 41, 12, 3, 74, 15]:
    if current_largest is None or the_num > current_largest:
        current_largest = the_num
    print(current_largest, the_num)
print("after", current_largest)