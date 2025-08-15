import string
import random

try:
    pass_length = int(input("Enter the length of password you want:"))
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    password = "" 
    
    for _ in range(pass_length):
        password += random.choice(all_characters) 
            
    print(password)

except ValueError:
    print("That's not a valid number! Please enter a number for the length.")
