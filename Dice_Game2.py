# Based on Dice Game 1 by Young-Do Krienbuehl and Leslie from INST126
# Written by Young-Do Krienbuehl for INST126 Final Project

# Notes:
# Unable to add 'Tuple Out' when player rerolls and get same value as fixed dice
# 
# 

#import necessary modules
import random
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Introduce the Tuple Out Dice Game and display the rules
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
   raise SystemExit("Invalid input. Exiting program.")

# For testing
# rounds = 3

# Load results of previous game if there is one 
try:
   with open("scores.txt", "r") as file_connection:
      file_contents = file_connection.read()
      print("Last Game Results:\n" + file_contents)
except FileNotFoundError:
   print("No game found.\nContinuing with Game")
   
# Represents the sides of the dice.
sides = (1,2,3,4,5,6)

# Initialize final scores
player_total_score = 0
cpu_total_score = 0


# Get the current date and time
current_time = time.strftime("%Y-%m-%d %H:%M")
#print(current_time)

# Initialize a list to store round data
game_data = []

# Main game loop
# Will loop for set amount of rounds
for round_num in range(1, rounds + 1):

   # Start of each round
   print(f"\n------ Round {round_num} ------")

   # Player Turn
   response = input("Are you ready!!!\nType 'R' to roll dice: ")
   if response.casefold() == "r":
      # keeps track of round score then adds to total
      player_round_score = 0

      #Initial roll of all dice
      dice = {
         "dice1" : random.choice(sides),
         "dice2" : random.choice(sides),
         "dice3" : random.choice(sides)
      }

      #Test values
      # dice = {
      #    "dice1" : 2,
      #    "dice2" : 2,
      #    "dice3" : 3
      # }

      # Initial display of players dice and score
      player_round_score = dice["dice1"] + dice["dice2"] + dice["dice3"]
      print(f"\nYou rolled {dice['dice1']}, {dice['dice2']}, {dice['dice3']}.\nCurrent score: {player_round_score}")
      
      #Tuple out condition
      # All 3 dice equal each other and awards 0 points to player
      if dice["dice1"] == dice["dice2"] == dice["dice3"]:
            player_round_score = 0
            print(f"\nYou rolled {dice['dice1']}, {dice['dice2']}, {dice['dice3']}.\nSorry you 'Tupled Out'. No points this round")

      # Conditions when 2 dice values are the same.
      # This will 'Fix' the dice. (The fixed dice cant be rerolled)      
      else:
         
         fixed_dice = [] # List will contain 'Fixed' Dice
         if dice["dice1"] == dice["dice2"]:
            fixed_dice = [dice["dice1"], dice["dice2"]]
            print("Two dice have become fixed. You now only have one dice to roll.")
            reroll_response = ""
            # Loop that allows user to reroll remaining dice as much as they want
            while reroll_response.casefold() != "n":
               reroll_response = input("Do you want to reroll the remaining die?\nType 'R' to reroll the dice or 'N' to keep it at that value: ")
               if reroll_response.casefold() == "r":
                  dice["dice3"] = random.choice(sides)
                  print(f"New roll for the remaining die: {dice['dice3']}")
               elif reroll_response.casefold() == "n":
                  print(f"The value of the remaining die is: '{dice['dice3']}'")

         elif dice["dice2"] == dice["dice3"]:
            fixed_dice = [dice["dice2"], dice["dice3"]]
            print("Two dice have become fixed. You now only have one dice to roll.")
            reroll_response = ""
            # Loop that allows user to reroll remaining dice as much as they want
            while reroll_response.casefold() != "n":
               reroll_response = input("Do you want to reroll the remaining die?\nType 'R' to reroll the dice or 'N' to keep it at that value: ")
               if reroll_response.casefold() == "r":
                  dice["dice1"] = random.choice(sides)
                  print(f"New roll for the remaining die: {dice['dice1']}")
               elif reroll_response.casefold() == "n":
                  print(f"The value of the remaining die is: '{dice['dice1']}'")

         elif dice["dice1"] == dice["dice3"]:
            fixed_dice = [dice["dice1"], dice["dice3"]]
            print("Two dice have become fixed. You now only have one dice to roll.")
            reroll_response = ""
            # Loop that allows user to reroll remaining dice as much as they want
            while reroll_response.casefold() != "n":
               reroll_response = input("Do you want to reroll the remaining die?\nType 'R' to reroll the dice or 'N' to keep it at that value: ")
               if reroll_response.casefold() == "r":
                  dice["dice2"] = random.choice(sides)
                  print(f"New roll for the remaining die: {dice['dice2']}")
               elif reroll_response.casefold() == "n":
                  print(f"The value of the remaining die is: '{dice['dice2']}'")
            

      # Player: Add round score to total score   
      player_total_score += player_round_score
   else: 
      raise SystemExit("Exiting program due to invalid input.")
      
   #########################################################################################################
   #Cpu Turn
   #Keeps track of CPU round score
   cpu_round_score = 0

   #Initial roll of CPU dice
   cpu_dice = {
         "cpu_dice1" : random.choice(sides),
         "cpu_dice2" : random.choice(sides),
         "cpu_dice3" : random.choice(sides)
      }

   # Tuple out condition
   # All 3 dice equal each other and awards 0 points
   if cpu_dice["cpu_dice1"] == cpu_dice["cpu_dice2"] == cpu_dice["cpu_dice3"]: 
      print(f"\nThe CPU rolled {cpu_dice['cpu_dice1']}, {cpu_dice['cpu_dice2']}, {cpu_dice['cpu_dice3']}. Tuple Out! No points this round.")
      cpu_round_score = 0
   else:
      fixed_dice = [] # List will contain 'Fixed' Dice

      # Will trigger if 2 die values are equal
      if cpu_dice["cpu_dice1"] == cpu_dice["cpu_dice2"]:
         fixed_dice = [cpu_dice["cpu_dice1"], cpu_dice["cpu_dice2"]]
         print(f"\nYou rolled {cpu_dice['cpu_dice1']}, {cpu_dice['cpu_dice2']}, {cpu_dice['cpu_dice3']}.")
         print("Two dice have become fixed. You now only have one dice to roll.")
         # Cpu will reroll their die if value is under 4
         if cpu_dice["cpu_dice3"] < 4:
            cpu_dice["cpu_dice3"] = random.choice(sides) 
         print(f"The value of the remaining die is: '{cpu_dice['cpu_dice3']}'")

      elif cpu_dice["cpu_dice2"] == cpu_dice["cpu_dice3"]:
         fixed_dice = [cpu_dice["cpu_dice2"], cpu_dice["cpu_dice3"]]
         print(f"\nYou rolled {cpu_dice['cpu_dice1']}, {cpu_dice['cpu_dice2']}, {cpu_dice['cpu_dice3']}.")
         print("Two dice have become fixed. You now only have one dice to roll.")
         # Cpu will reroll their die if value is under 4
         if cpu_dice["cpu_dice1"] < 4:
            cpu_dice["cpu_dice1"] = random.choice(sides) 
         print(f"The value of the remaining die is: '{cpu_dice['cpu_dice1']}'")

      elif cpu_dice["cpu_dice1"] == cpu_dice["cpu_dice3"]:
         fixed_dice = [cpu_dice["cpu_dice1"], cpu_dice["cpu_dice3"]]
         print(f"\nYou rolled {cpu_dice['cpu_dice1']}, {cpu_dice['cpu_dice2']}, {cpu_dice['cpu_dice3']}.")
         print("Two dice have become fixed. You now only have one dice to roll.")
         # Cpu will reroll their die if value is under 4
         if cpu_dice["cpu_dice2"] < 4:
            cpu_dice["cpu_dice2"] = random.choice(sides) 
         print(f"The value of the remaining die is: '{cpu_dice['cpu_dice2']}'")
        
      # Display CPU round results
      cpu_round_score = cpu_dice["cpu_dice1"] + cpu_dice["cpu_dice2"] + cpu_dice["cpu_dice3"]
      print(f"\nThe CPU rolled {cpu_dice['cpu_dice1']}, {cpu_dice['cpu_dice2']}, {cpu_dice['cpu_dice3']}.\nCurrent score: {cpu_round_score}")

   # CPU Add round score to total score
   cpu_total_score += cpu_round_score
   # Round over
   # Save round records to Dataframe
   round_summary = {
         "Round": round_num,
         "Player_Score": player_round_score,
         "CPU_Score": cpu_round_score,
         "Winner": "Player" if player_round_score > cpu_round_score else "CPU" if cpu_round_score > player_round_score else "Tie"
      }
   game_data.append(round_summary)

# Test if scores are accurate   
#print(f"The player's total score is: {player_total_score}\nThe CPU's total score is: {cpu_total_score}")   

#################################################################################################################################################

#Game End
#Declare winner when set amount of rounds has been reached
print("\n--- Game Over ---")

# After the game ends, create a DataFrame
df = pd.DataFrame(game_data)

# Display win or lose message to player
if player_total_score > cpu_total_score:
   print(f"Congratulations! You won with a score of {player_total_score} to {cpu_total_score}.")
elif cpu_total_score > player_total_score:
   print(f"CPU wins with a score of {cpu_total_score} to {player_total_score}. Better luck next time!")
else:
   print(f"It's a tie! Both scored {player_total_score}. Well played!")

# Save scores to txt file
# includes time tracking feature
with open("scores.txt", "w") as file:
   if player_total_score > cpu_total_score:
      print("You Won The Game!!! ")
   else:
      print("Sorry You Lost This Game:(")
   file.write(f"Final Player Score: {player_total_score}\n")
   file.write(f"Final Opponent Score: {cpu_total_score}\n")
   file.write(f"Rounds played: {rounds}\n")
   file.write(f"Game played on: {current_time}\n")  # Adds current date and time

# Thank you message to player
print("\n\nThanks for playing my game!!!\n-Young-Do Krienbuehl")


# Save to a CSV file and display results
df.to_csv("game_results.csv", index=False)

print("\n--- Game Summary ---")
print(df)

# At the end of the game (after the DataFrame is created) Make the chart
plt.figure(figsize=(10, 6))
sns.barplot(x="Round", y="Player_Score", data=df, color="blue", label="Player")
sns.barplot(x="Round", y="CPU_Score", data=df, color="red", label="CPU")

plt.title("Player vs CPU Scores per Round")
plt.xlabel("Round")
plt.ylabel("Score")
plt.legend()
plt.show()


