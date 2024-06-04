password_file = open("SecretPasswordFile.txt")
secret_password = password_file.read()
print("enter your password")
typed_password = input()
if typed_password == secret_password:
    print("access granted")
    if typed_password == "12345":
        print("that password is one that an idiot puts on their luggage")
else:
    print("access denied")