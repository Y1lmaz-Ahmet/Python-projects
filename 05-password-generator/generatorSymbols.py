import random


symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
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

