import os
import random

AllCharacters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                 "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                 "$","#","@","!","&","+","-","_",
                 "0","1","2","3","4","5","6","7","8","9"
                 ]

answer = []
lengthPassword = input("enter the length of your password:    ")
i = 0
if int(lengthPassword) < 50:
    while i < int(lengthPassword) :
        x = random.randrange(0 , len(AllCharacters))
        answer.append(AllCharacters[x])
        i+=1

    os.system('cls')
    print("Your password:" + "\t")
    print(end=" ")
    if(answer):
        for z in answer :
            print( z , end='')
    else:
        os.system('cls')
        print("your length must be between 1 and 50!")
elif int(lengthPassword) < 0 :
    os.system('cls')
    print("you'r length must be between 1 and 50!")

else:
    os.system('cls')
    print("your length must be between 1 and 50!")