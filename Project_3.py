import random

def guess(num,guess_num):
    if(num==guess_num):
        print("Cool guessed number is right! ")
    else:
        print("You guessed the wrong number")
        print("If you want to continue press 1 or press 0")
        con=int(input())
        if(con==1):
            guess_num = int(input("Enter the guessed number again: "))
            guess(num, guess_num)
        else:
            print("Bye, Have a good day")



num= random.randrange(0,9)                               #Generate a random number between(0 to 9)
guess_num= int(input("Enter the guessed number: "))      #entered number
guess(num, guess_num)


