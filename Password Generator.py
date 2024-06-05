import random
import string

def Pass_Generator(length,uppercase=True,lowercase=True,digits=True):
    Passwrd= ''
    
    if uppercase:
        Passwrd += string.ascii_uppercase
    if lowercase:
        Passwrd += string.ascii_lowercase
    if digits:
        Passwrd += string.digits

    if not Passwrd:
        raise ValueError("At least one character type must be selected")
    
    password = ''.join(random.choice(Passwrd) for _ in range(length))
    return password


password_input=int(input("Enter number of characters: "))
print("Generated password: ", Pass_Generator(password_input,uppercase=True,lowercase=True,digits=True))
