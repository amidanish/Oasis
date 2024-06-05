import random
import string

def Pass_Generator(length, uppercase=True, lowercase=True, digits=True):
    if not isinstance(length, int) or length <= 0:
        return "Error: Enter a valid positive integer for password length."
    
    Passwrd = ''
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

while True:
    try:
        password_input = input("Enter number of characters: ")
        if password_input.strip() == "":
            print("No input detected. Please enter a number.")
            continue
        password_input = int(password_input)
        if password_input <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

generated_password = Pass_Generator(password_input, uppercase=True, lowercase=True, digits=True)
print("Generated password: ", generated_password)
