#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(f"the chosen word is : {chosen_word}" )

#TODO: Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for char in chosen_word:
  display.append("_")

#TODO: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO: Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#TODO: Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if guess == letter:
    display[position] = letter

#TODO: Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)