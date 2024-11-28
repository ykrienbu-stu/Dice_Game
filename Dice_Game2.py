
#import necessary modules
import random

#Introduce the dice Game and display the rules
print('''
Hello! Welcome to the 'Tuple Out' Dice Game!!!
This is a game where you roll dice to get the hightest score.
You will be playing against a computer to see who gets the highest score
after a set amount of rounds.
''')
# Ask for the amount of rounds the user would like to play
try:
   rounds = int(input("How many rounds would you like to play?: "))
except ValueError:
   print("Invalid input. Exiting program.")
   exit()


# Load previous save file if there is one 
# Need to work on this feature
# with open("scores.txt", "r") as file:


# Represents the sides of the dice.
sides = [1,2,3,4,5,6]
# Initialize final scores
player_total_score = 0
cpu_total_score = 0


# Main game loop
# Will loop for set amount of rounds
for round_num in range(1, rounds + 1):
   # Start of each round
   print(f"\n------ Round {round_num} ------")

   # Player Turn
   response = input("Are you ready!!!\nType 'R' to roll dice: ")
   if response.casefold() == "r":
      dice1 = random.choice(sides)
      dice2 = random.choice(sides)
      dice3 = random.choice(sides)

      #Tuple out condition
      # Need to add if 2 values == each other
      if dice1 == dice2 == dice3:
            player_round_score = 0
            print(f"\nYou rolled {dice1}, {dice2}, {dice3}.\nCurrent score: {player_round_score}")
      else:
         player_round_score = dice1 + dice2 + dice3
         print(f"\nYou rolled {dice1}, {dice2}, {dice3}.\nCurrent score: {player_round_score}")

      # Add round score to total score   
      player_total_score += player_round_score   
   else: 
      print("U didnt type 'R' Exiting program") 
      exit()

   #########################################################################################################
   #Cpu Turn
   cpu_dice1 = random.choice(sides)
   cpu_dice2 = random.choice(sides)
   cpu_dice3 = random.choice(sides)

   # Tuple out condition
   # Need to add if 2 values == each other
   if cpu_dice1 == cpu_dice2 == cpu_dice3: 
      print(f"\nThe CPU rolled {cpu_dice1}, {cpu_dice2}, {cpu_dice3}. Tuple Out! No points this round.")
      cpu_round_score = 0
   else:
      cpu_round_score = cpu_dice1 + cpu_dice2 + cpu_dice3
      print(f"\nThe CPU rolled {cpu_dice1}, {cpu_dice2}, {cpu_dice3}.\nCurrent score: {cpu_round_score}")
   
   # Add round score to total score
   cpu_total_score += cpu_round_score
   
print(f"{player_total_score} {cpu_total_score}")   


########################################################################################
#Game End
#Declare winner when set amount of rounds has been reached

print("\n--- Game Over ---")
if player_total_score > cpu_total_score:
   print(f"Congratulations! You won with a score of {player_total_score} to {cpu_total_score}.")
elif cpu_total_score > player_total_score:
   print(f"CPU wins with a score of {cpu_total_score} to {player_total_score}. Better luck next time!")
else:
   print(f"It's a tie! Both scored {player_total_score}. Well played!")

# Save scores to file
with open("scores.txt", "w") as file:
   file.write(f"Final Player Score: {player_total_score}\n")
   file.write(f"Final Opponent Score: {cpu_total_score}\n")
   file.write(f"Rounds played: {rounds}\n")
# Thank you message to player
print("\n\nThanks for playing my game!!!\n-Young-Do Krienbuehl")