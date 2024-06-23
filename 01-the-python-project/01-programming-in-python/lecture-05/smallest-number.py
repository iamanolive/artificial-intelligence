current_smallest = None
print("before", current_smallest)
for the_num in [9, 41, 12, 3, 74, 15]:
    if current_smallest is None or the_num < current_smallest:
        current_smallest = the_num
    print(current_smallest, the_num)
print("after", current_smallest)