#Hangman Game! 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(f"the chosen word is : {chosen_word}" )


display = []
for char in chosen_word:
  display.append("_")

game_over = False
while not game_over:
  guess = input("Guess a letter: ").lower()

  for position in range(len(chosen_word)):
    
    letter = chosen_word[position]
    if guess == letter:
      display[position] = letter
    
  if "_" not in display:
    game_over = True
  print("Yay! you WON!")
  print(display)