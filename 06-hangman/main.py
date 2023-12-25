#Hangman Game! 
import random
import hangman_art
import words

lives = 6
#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(words.unique_words)
print(hangman_art.logo)
list_of_usen_letters = []
display = []
for char in chosen_word:
  display.append("_")

game_over = False
while not game_over:
  guess = input("Guess a letter: ").lower()

  for position in range(len(chosen_word)):
    
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(f"the mysterious word: {display}")
  print(f"the used letters till now: {list_of_usen_letters}")

  if guess not in chosen_word:
      if guess not in list_of_usen_letters:
        list_of_usen_letters.append(guess)
      lives -= 1
      if lives == 0:
        game_over = True
        print("You Lose!")
        print(f"The word was: {chosen_word}")
  print(hangman_art.stages[lives])
  if "_" not in display:
    game_over = True
    print("Yay! you WON!")