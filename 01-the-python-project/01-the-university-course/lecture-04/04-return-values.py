def greet():
    return "hello" # end of invocation
print(greet(), "glenn")
print(greet(), "sally")


# return value = residual value
def greet(lang):
    if lang == "es": return "hola"
    elif lang == "fr": return "bonjour"
    else: return "hello"
print(greet("en"), "glenn")
print(greet("es"), "sally")
print(greet("fr"), "michael")


def addtwo(a, b):
    added = a + b
    return added
x = addtwo(3, 5)
print(x)