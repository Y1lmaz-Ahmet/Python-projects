print('''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("left of right?\n").lower()
if left_or_right == "left":
    swim_or_wait = input("swim or wait?\n").lower()
    if swim_or_wait == "wait":
        which_door = input("which door? red, blue, or yellow\n").lower()
        if which_door == "red":
            print("Burned by fire.\nGame Over.")
        elif which_door == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif which_door == "yellow\nGame Over.":
            print("You Win!")
        else:
            print("Game Over.")
    elif swim_or_wait == "swim" or swim_or_wait == "else":
        print("Attacked by trout.\nGame Over.")
elif left_or_right == "right":
    print("Fall into a hole.\nGame Over.")
else:
    print("Invalid choice.\nGame Over.")