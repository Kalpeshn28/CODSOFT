import random as rm
import string as str



def generatedPassword( passwordLen):
    characters = str.ascii_uppercase + str.digits + str.ascii_lowercase 
    password = ''.join(rm.choice(characters) for _ in range(passwordLen))
    return password



passwordLen= int(input('Enter the length of password'))

if passwordLen<=0:
    print("Password length must be greater than zero")

else:
    password= generatedPassword(passwordLen)
    print(password)


