
#import necessary modules
import random

#Introduce the dice Game and display the rules
'''
Hello! Welcome to the 'Tuple Out' Dice Game!!!
This is a game where you roll dice to get the hightest score.
You will be playing against a computer to see who gets the highest score
after a set amount of rounds.
'''
# Ask for the amount of rounds the user would like to play
try:
   rounds = int(input("How many rounds would you like to play?"))
except ValueError:
   print("Invalid input. Please input a number.")
   exit()


# Load previous save file if there is one 
# with open("scores.txt", "r") as file:


# Initialize variables
player_dice = (0, 0, 0)
cpu_dice = (0, 0, 0)
player_score = 0
cpu_score = 0

# Represents the sides of the dice.
sides = [1,2,3,4,5,6]


# Test the random dice
# dice1 = random.choice(sides)
# dice2 = random.choice(sides)
# dice3 = random.choice(sides)
# print( dice1, "\n", dice2, "\n", dice3)


def play_game(rounds):

   for round_num in range(1, rounds):
      print(f"\n------ Round {round_num} ------")

      # Player Turn
      response = input("Are you ready!!!\nType 'R' to roll dice")
      if response.casefold() == "r":
         dice1 = random.choice(sides)
         dice2 = random.choice(sides)
         dice3 = random.choice(sides) 
         current_player_score = dice1 + dice2 + dice3
         print(f"You rolled {dice1},{dice2},{dice3}.\nCurrent score: {current_player_score}")
      else: 
         print("U didnt type 'R' please type 'R' to roll the dice") 
         exit()
      #Cpu Turn
      cpu_dice1 = random.choice(sides)
      cpu_dice2 = random.choice(sides)
      cpu_dice3 = random.choice(sides)
      current_cpu_score = cpu_dice1 + cpu_dice2 + cpu_dice3
      print(f"The CPU rolled {cpu_dice1},{cpu_dice2},{cpu_dice3}.\nCurrent score: {current_cpu_score}")
      #End of Round, display current scores
      print(f"End of Round 1\nPlayer Score: {player_score}\nCPU score: {cpu_score}")


   return player_score, cpu_score #return with player scores



########################################################################################
#Game End
#Declare winner when set amount of rounds has been reached


# Declare the winner
print("\n--- Game Over ---")
if player_score > cpu_score:
   print(f"Congratulations! You won with a score of {player_score} to {cpu_score}.")
elif cpu_score > player_score:
   print(f"CPU wins with a score of {cpu_score} to {player_score}. Better luck next time!")
else:
   print(f"It's a tie! Both scored {player_score}. Well played!")

# Save scores to file
with open("scores.txt", "w") as file:
   file.write()