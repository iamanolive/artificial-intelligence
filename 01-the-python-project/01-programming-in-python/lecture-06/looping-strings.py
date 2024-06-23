# looping using the while loop
fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# looping using the for loop
fruit = "banana"
for letter in fruit:
    print(letter)