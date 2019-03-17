import random

char = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ`!@#$%^&*()_+=-|'

length = int(input("Give me the lenght of password: "))

number = int(input("Number of password?: "))

password = ''
for p in range(number):

    for c in range(length):
        password += random.choice(char)
    print(password)
    password = ''
