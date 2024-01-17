####### START IMPORTS #######
## Import Random 
import random 
## Import list as data from game_data
from game_data import data
## Import ASCII  as logo from art
from art import logo, vs
####### END IMPORTS #######

####### START #######
## Starting game print ASCII: Logo
print(logo)
## Compare A : function(name,job,country)
def pick_person_from_list(person_list): ## this can be used twice: Compare A & Compare B 
	"""
    Choose a random person from the provided list.

    Parameters:
    - person_list (list): A list of dictionaries representing individuals.

    Returns:
    - dict: A dictionary representing the chosen person.
    """
	chosen_person = random.choice(person_list)
	return chosen_person

def print_person_information(person):
	"""
    Print information about the chosen person.

    Parameters:
    - person (dict): A dictionary representing an individual with 'name', 'description', and 'country' attributes.
    """
	print(f"{person['name']}, {person['description']}, from {person['country']}.")

print(logo)

person_a = pick_person_from_list(data)
print_person_information(person=person_a)

print(vs)

person_b = pick_person_from_list(data)
print_person_information(person=person_b)

user_answer = str(input(f"Who has more followers? 'Type' 'a' or 'b': "))




####### END #######

