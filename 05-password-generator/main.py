import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



#Greet user
print("Welcome to the PyPassword Generator!")

#Generating random letters 
amount_of_letters_in_password = int(input("How many letters would you like in your password?\n"))
random_chosen_letters_from_letters_list = []
for letter in range(1,amount_of_letters_in_password+1):
	#setting a value for the letter generator
	random_letter_generator_range = random.randint(0,10)
	#picking random letters from the letters list
	found_letter_on_index_of_list_letters = letters[random_letter_generator_range]
	random_chosen_letters_from_letters_list.append(found_letter_on_index_of_list_letters)

#Generating random symbols
amount_of_symbols_in_password = int(input("How many symbols would you like?\n"))
random_chosen_symbols_from_symbols_list = []
#only asks once if the user asks for a number out of range.
if amount_of_symbols_in_password > len(symbols):
	print(f"Sorry, the symbols list only contains: {len(symbols)}\nPlease choose again")
	user_chosen_again_symbol = int(input("How many symbols would you like?\n"))
	for char in range(1,user_chosen_again_symbol+1):
		#setting a value for the symbol generator
		random_char_generator_range = random.randint(0,len(symbols) -1)
		#picking random symbol from the symbol list
		found_symbol_on_index_of_symbol_list = symbols[random_char_generator_range]
		random_chosen_symbols_from_symbols_list.append(found_symbol_on_index_of_symbol_list)
else: 
	for char in range(1,amount_of_symbols_in_password+1):
		#setting a value for the symbol generator
		random_char_generator_range = random.randint(0,len(symbols) -1)
		#picking random symbol from the symbol list
		found_symbol_on_index_of_symbol_list = symbols[random_char_generator_range]
		random_chosen_symbols_from_symbols_list.append(found_symbol_on_index_of_symbol_list)

# Generating random numbers
amount_of_numbers_in_password = int(input("How many numbers would you like?\n"))
random_chosen_numbers_from_numbers_list = []
for number in range(0,amount_of_numbers_in_password):
	#setting a value for the number generator
	random_number_generator_range = random.randint(0,len(numbers) - 1)
	#picking random number from the numbers list
	found_number_on_index_of_list_numbers = numbers[random_number_generator_range]
	random_chosen_numbers_from_numbers_list.append(found_number_on_index_of_list_numbers)

# password generator finish
letters_symbols_numbers_lists_combined_filled = random_chosen_letters_from_letters_list + random_chosen_symbols_from_symbols_list + random_chosen_numbers_from_numbers_list

password=""
for letter in letters_symbols_numbers_lists_combined_filled:
	password+=letter
print(f"generated password: {password}")