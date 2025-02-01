import random 

print("Welcome to Rock Paper Scissors!")

# Rock, Paper, Scissors ASCII Art
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)_______
           _________)
          __________)
         __________)
---._____________)
""")

scissors = ("""
    _______
---'   ____)______
          ________)
       ____________)
      (____)
---.__(___)
""")

# List of choices
game_images = [rock, paper, scissors]

# User input
option = int(input("Choose 0 for Rock, 1 for Paper, and 2 for Scissors: "))

if option >= 0 and option <= 2:
    print(f"You chose:\n{game_images[option]}")
else:
    print("Invalid Choice! You must pick 0, 1, or 2.")
    exit()

# Computer choice
computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{game_images[computer_choice]}")

# Determining the winner
if option == computer_choice:
    print("It's a tie!")
elif (option == 0 and computer_choice == 2) or \
     (option == 1 and computer_choice == 0) or \
     (option == 2 and computer_choice == 1):
    print("You win! 🎉")
else:
    print("You lose! ")
