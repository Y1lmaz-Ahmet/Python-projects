#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO: -1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word_int = random.randint(0,len(word_list) -1)
chosen_word_str = word_list[chosen_word_int]
print(chosen_word_str)
#TODO:-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
#TODO:-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
location = 0
for char in chosen_word_str:
  if guess == char:
    print(f"found: {location} letter: {chosen_word_str[location]}")
  elif guess != char:
    print("nothing")
  else:
    print("ERROR")
  location += 1