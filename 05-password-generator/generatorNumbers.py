import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Generating random numbers
amount_of_numbers_in_password = int(input("How many numbers would you like?\n"))
random_chosen_numbers_from_numbers_list = []
for number in range(0,amount_of_numbers_in_password):
	#setting a value for the number generator
	random_number_generator_range = random.randint(0,len(numbers) - 1)
	#picking random number from the numbers list
	found_number_on_index_of_list_numbers = numbers[random_number_generator_range]
	random_chosen_numbers_from_numbers_list.append(found_number_on_index_of_list_numbers)