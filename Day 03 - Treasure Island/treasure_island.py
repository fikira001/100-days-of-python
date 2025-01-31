print ('''
       *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
       
       ''')
# first trial 
# print ("Welcome to the treasure island, your mission is to find the treasure")

# direction = input("You going left or Right: ")

# direction = direction.lower()

# if direction == "right":
#     print("Game Over")
# else:
#     if direction == "left": 
#         move = input ("wait or swim").lower()
#         if move == "wait": 
#             print ("game over")
#         else: 
#             if move == "swim":
#                 door = input ("red or blue or yellow ").lower()
#                 if door == "red": 
#                     print ("Game Over ")
#                 elif door == "blue":
#                     print ("Game Over ")
#                 else: 
#                     print ("You win ")

print("Welcome to the treasure island, your mission is to find the treasure!")

# First choice: Left or Right
direction = input("You are at a crossroad. Do you go left or right? ").lower()

if direction == "right":
    print("You fell into a pit. Game Over!")
elif direction == "left":
    # Second choice: Wait or Swim
    move = input("You come to a lake. There is an island in the middle. Do you wait for a boat or swim across? (wait/swim) ").lower()
    
    if move == "wait":
        print("A boat arrives and takes you to the island safely.")
        # Third choice: Door color
        door = input("You arrive at the island unharmed. There is a house with 3 doors: red, blue, and yellow. Which door do you choose? ").lower()
        
        if door == "red":
            print("You enter a room full of fire. Game Over!")
        elif door == "blue":
            print("You enter a room full of beasts. Game Over!")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    elif move == "swim":
        print("You were attacked by a giant trout. Game Over!")
    else:
        print("Invalid choice. Game Over!")
else:
    print("Invalid choice. Game Over!")