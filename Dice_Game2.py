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
rounds = int(input("How many rounds would you like to play?"))


# Initialize variables


player_dice = (0, 0, 0)
cpu_dice = (0, 0, 0)
player_score = 0
cpu_score = 0
final_score = 0
cpu_final_score = 0
# Represents the sides of the dice.
sides = [1,2,3,4,5,6]


# Test the random dice
# dice1 = random.choice(sides)
# dice2 = random.choice(sides)
# dice3 = random.choice(sides)
# print( dice1, "\n", dice2, "\n", dice3)


response = input("Are you ready!!!\nType 'R' to roll dice")
# player
if response.casefold() == "r":
   while rounds > 0:
       dice1 = random.choice(sides)
       dice2 = random.choice(sides)
       dice3 = random.choice(sides)
       print("End of Round 1\nPlayer Score: ",final_score,"\nCPU score: ",cpu_final_score )
       rounds -= 1
else:
   print("U didnt type 'R' please type 'R' to roll the dice")   


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