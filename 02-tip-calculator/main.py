#greeting the user
print("Welcome to the tip calculator.")
#asking for string values and converting them to numbers
total_bill = float(input("What was the total bill? "))
chosen_percentage_tip = int(input("What percentage tip would you like to give? 10, 12, ore 15? "))
amount_of_people = int(input("How many people to split the bill? "))
#printing the current values from the user
print(f"bill:${total_bill}\npercentage:{chosen_percentage_tip}\npeople:{amount_of_people}")
#calculating the values received from the user
totall_bill_percentage = float((total_bill / 100) * chosen_percentage_tip)
totall_bill_with_tip = total_bill + totall_bill_percentage
pay_per_person = round(totall_bill_with_tip / amount_of_people,2)
print(f"Each person should pay ${pay_per_person}")


