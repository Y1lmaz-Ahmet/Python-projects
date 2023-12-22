import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Generating random letters 
amount_of_letters_in_password = int(input("How many letters would you like in your password?\n"))
random_chosen_letters_from_letters_list = []
for letter in range(1,amount_of_letters_in_password+1):
	#setting a value for the letter generator
	random_letter_generator_range = random.randint(0,10)
	#picking random letters from the letters list
	found_letter_on_index_of_list_letters = letters[random_letter_generator_range]
	random_chosen_letters_from_letters_list.append(found_letter_on_index_of_list_letters)