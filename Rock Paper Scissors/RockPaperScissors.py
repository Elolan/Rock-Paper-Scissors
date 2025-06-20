#RockPaperScissors

import random
import os

print("Welcome to Rock-Paper-Scissors")
print("Rules:")
print("1 is Rock")
print("2 is Paper")
print("3 is Scissors")
print("0 if you want to quit")
print("You know how it works ;)")

while True:
   player = int(input("Please type the number of your choice (1-3): "))
   os.system("cls")
   
   if player == 0:
      print("Thanks for playing!")
      break
   if player not in [1, 2, 3]:
      print("Invalid input. Try again.")
      continue
   
   computer = random.randint(1, 3)

   if player == computer:
    print("It's a tie!")
    print("Try again?")
   elif player == 1 and computer == 2:
    print("Paper beats Rock! You lose!")
    print("Try again?")
   elif player == 1 and computer == 3:
    print("Rock beats Scissors! You win!")
    print("Try again?")
   elif player == 2 and computer == 1:
    print("Paper beats Rock! You win!")
    print("Try again?")
   elif player == 2 and computer == 3:
    print("Scissors beat Paper! You lose!")
    print("Try again?")
   elif player == 3 and computer == 1:
    print("Rock beats Scissors! You lose!")
    print("Try again?")
   elif player == 3 and computer == 2:
    print("Scissors beat Paper! You win!")
    print("Try again?")