rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import cheater
import random
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0, 2)

# deciding which figure the computer has chosen
computer_figure = ""
if computer_choice == 0:
    computer_figure = rock
if computer_choice == 1:
    computer_figure = paper
if computer_choice == 2:
    computer_figure = scissors

# deciding which figure the human has chosen
human_figure = ""
if human_choice == 0:
    human_figure = rock
if human_choice == 1:
    human_figure = paper
if human_choice == 2:
    human_figure = scissors

# comparing and looking who has won!
print(f"{human_figure}\n---------VS----------\n{computer_figure}")

if human_figure == rock and computer_figure == scissors:
    print("HUMAN wins!")
elif human_figure == paper and computer_figure == rock:
    print("HUMAN wins!")
elif human_figure == scissors and computer_figure == paper:
    print("HUMAN WINS")
elif computer_figure == rock and human_figure == scissors:
    print("COMPUTER wins!")
elif computer_figure == paper and human_figure == rock:
    print("COMPUTER wins!")
elif computer_figure == scissors and human_figure == paper:
    print("COMPUTER wins!")
elif human_figure == computer_figure:
    print("DRAW!!")
else:
    print(f"You typed: {human_choice} which is INVALID!\nCheating is not allowed, so you LOSE!")
    print(cheater.face)
