import os
import art

# Prints a logo
print(art.logo)
# Boolean for the while loop
is_bid_running = True
# Dictionary to keep data of the bidders (name,bid_amount)
bidders_dictionary = {}

# function to find the highest bidder in the dictionary
def find_highest_bidder(bidding_record):
  highest_bid = 0
  highest_bidder = ""
  for key in bidding_record:
    amount = bidding_record[key]
    if highest_bid < amount:
      highest_bid = amount
      highest_bidder = key
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
  
# function that prompts question to the bidder untill the bidding is closed
def take_bid():
  name = input("What is your name?: ")
  amount  = int(input("What's your bid?: $"))
  bidders_dictionary[name] = amount

while is_bid_running:
  print("Welcome to the secret auction program.")
  take_bid()
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

  # if no bidders, stop the loop and select the winner with the amount he/she bids
  if other_bidders == "no":
    is_bid_running = False
    find_highest_bidder(bidders_dictionary)
  # if more bidders, clear the console so that the next person doesnt see the bidders name + the bid amount
  elif other_bidders == "yes":
    os.system("cls" if os.name == "nt" else "clear")
  # if something unexpected happens, finish the bidding
  else:
    print("error,ask for help")