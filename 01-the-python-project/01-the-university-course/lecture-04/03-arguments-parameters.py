big = max("hello world") # "hello world" = argument

def greet(lang): # lang = parameter (placeholder)
    if lang == "es": print("hola")
    elif lang == "fr": print("bonjour")
    else: print("hello")
greet("en"); greet("es"); greet("fr")