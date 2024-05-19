def greet(lang):
    if lang == "es": print("hola")
    elif lang == "fr": print("bonjour")
    else: print("hello")

greet("en")
greet("es")
greet("fr")

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)