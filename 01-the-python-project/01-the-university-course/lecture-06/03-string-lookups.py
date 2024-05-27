# indeterminate loop
fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1


# determinate loop
fruit = "banana"
for letter in fruit:
    print(letter)