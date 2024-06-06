my_pets = ["zophie", "pooka", "fat-tail"]
print("enter a pet name:")
name = input()
if name not in my_pets:
    print("i do not have a pet named " + name)
else: 
    print(name + " is my pet")