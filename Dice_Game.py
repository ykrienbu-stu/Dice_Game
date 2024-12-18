# Older Version of DiceGame
# Made by: Young-Do Krienbuehl and Leslie for Pair Programming assignments

# Beginning the tuple game program
'''
This program is a dice game that you play against a cpu.
Rules:
'''




#importing modules necessary
import random








# This represents a 6 sided dice the program is rolling
chances = [1,2,3,4,5,6]




# This is the score variable that holds the user score
score = 0




# Creating rounds
rounds = 1




# These are the 3 dices the programm is rolling
dice1 = random.choice(chances)
dice2 = random.choice(chances)
dice3 = random.choice(chances)




# testing the random module
print(dice1, "\n", dice2, "\n", dice3)


# Get user input
reponse = input("Type Y to roll dice")




# Program is going to run for 5 rounds then end
while rounds <= 5:
  # dice1 = random.choice(chances)
  # dice2 = random.choice(chances)
  # dice3 = random.choice(chances)
  print("top of while loop")
  print("This is round: ", rounds)


   if reponse == "y":
      
       if rounds == 0:
           print("The game is starting here are dice 1,2,3 in the same order", dice1, dice2, dice3)
       if dice1 != dice2 & dice2 != dice3 & dice3 != dice1:
           dice1 = random.choice(chances)
           dice2 = random.choice(chances)
           dice3 = random.choice(chances)
           print("No Dice is equal")
       elif dice1 == dice2 == dice3:
           score = 0
           print(dice1, dice2, dice3)
           print(score)
           print("All dice are equal")
           print("The game ended at round: ", rounds)
           print("The score is: ", score)
           #break
       elif dice1 == dice2:
           dice3 = random.choice(chances)
           score = dice1 + dice2 + dice3
           print("Dice 1 and 2 are same the score is: ", score)
           print("Dice in 1,2,3 order", dice1, dice2, dice3)
           print("This is the current score: ", score)
           rounds = rounds+1
       elif dice2 == dice3:
           dice1 = random.choice(chances)
           score = dice1 + dice2 + dice3
           print("Dice 2 and 3 are same the score is: ", score)
           print("Dice in 1,2,3 order",dice1, dice2, dice3)
           print("This is the current score: ", score)
           rounds = rounds+1
       elif dice1 == dice3:
           dice2 = random.choice(chances)
           score = dice1 + dice2 + dice3
           print("Dice 1 and 3 are same the score is: ", score)
           print("Dice in 1,2,3 order",dice1, dice2, dice3)
           print("This is the current score: ", score)
           rounds = rounds+1




  #rounds = rounds+1
  # dice1 = random.choice(chances)
  # dice2 = random.choice(chances)
  # dice3 = random.choice(chances)
   print(dice1, dice2, dice3)
   print(score)
response = input("Do you want to roll again?")


print(score)
print(dice1, dice2, dice3)




# Problem
'''
The game keeps running when all dice are the same although it's supposed to break
It only breaks if they are al the same on the first round
Not sure what's causing this.
  maybe my if statement is wrong?
  not really sure
  Or maybe it's the loop causing the issue, cuz it runs for at least 1 more round than supposed to after testing more




'''
