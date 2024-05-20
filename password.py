import string
import random

length=int(input("Enter password length:"))

print('''choose character set for password from these:
                 1.Digits,
                 2.Letters,
                 3.Special characters,
                 4.Exit''')

characterList=" "

while(True):
    choice=int(input("Select a Number:"))
    if(choice==1):
        characterList += string.digits
    elif(choice==2):
        characterList += string.ascii_letters
    elif(choice==3):
        characterList += string.punctuation
    elif(choice==4):
        break
    else:
        print("Please select a valid option!!")

password=[]

for i in range(length):

    randomchar=random.choice(characterList)

    password.append(randomchar)

print("The Random Password Is " + "".join(password))

