#Project Number 1
import random

elements = ["rock" , "paper" , "scissors"]
loop = True

while loop:
    Computer = (random.choice(elements))
    Player = None

    while Player not in elements:
        Player = input("Enter your choice (rock, paper, or scissors): ")
    print('Player: ' + Player)
    print('computer: ' + Computer)

    if Player == Computer:
        print("You Both Won! C'mon shake hands now. Bleh :p computer don't have hands")

    elif Player == "rock" and Computer == "scissors":
        print("Computer Won!")

    elif Player == "paper" and Computer == "scissors":
        print ("Computer Won!")

    elif Player == "scissors" and Computer == "rock":
        print("Computer Won!")

    else:
        print("You Won!")

    ask = input("Want to play again? y/n: ")
    if ask == "y":
        loop = True

    else:
        loop = False

print("Thanks for Playing!!!")

#Thanks @brocodz for teaching
#https://youtu.be/fn68QNcatfo?si=8F2RteKUqTyJPqXI
