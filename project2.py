import string
import random

charposi = string.ascii_letters + string.digits + string.punctuation

passlength = int(input("Enter the length of password you want:"))

password = []
i = 0
while (i < passlength):
    password.insert(i,random.choice(charposi))
    i = i + 1

newpassword = ''.join(password)
print(newpassword)




