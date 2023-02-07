import random

#using user-define function method
def guess(num,guess_num):
    if(num==guess_num):
        print("Cool guessed the right number")
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


"""
#using while loop method
while (num!=guess_num):         #infinte loop or when correct number you guess loop will end
    if(num!=guess_num):
        print("You guessed the wrong number ")
        guess_num = int(input("Enter the guessed number again: "))
    else:
        break

print("Cool guessed the right number")


"""

