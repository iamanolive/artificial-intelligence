# the index() method
spam = ["hello", "hi", "howdy", "heyas"]
print(spam.index("hello"))


# the append() method
spam = ["cat", "dog", "bat"]
spam.append("moose"); print(spam)


# the insert() method
spam = ["cat", "dog", "bat"]
spam.insert(1, "chicken"); print(spam)


# the remove() method
spam = ["cat", "bat", "rat", "elephant"]
spam.remove("bat"); print(spam)
spam = ["cat", "bat", "rat", "cat", "hat", "cat"]
spam.remove("cat"); print(spam)


# the sort() method
spam = [2, 5, 3.14, 1, -7]
spam.sort(); print(spam)
spam = ["ants", "cats", "dogs", "badgers", "elephants"]
spam.sort(); print(spam)
spam.sort(reverse = True); print(spam)

spam = ["Alice", "ants", "Bob", "badgers", "Carol", "cats"]
spam.sort(); print(spam)
spam = ["a", "z", "A", "Z"]
spam.sort(key = str.lower); print(spam)


# the reverse() method
spam = ["cat", "dog", "moose"]
spam.reverse(); print(spam)