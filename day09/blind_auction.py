import os
from art import logo

def clear():
    os.system('cls')

print(logo)
print("\nWelcome to the secret auction program.")


auction_dict = {
#    name : bid
}

while(True):
    name = input("What is your name?: ")
    bid  = int(input("What is your bid? : $"))
    auction_dict[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "yes":
        clear()
    elif more_bidders == "no":
        break

usr_bid  = 0
usr_name = ""
max_bid  = {}
for key in auction_dict:
    if auction_dict[key] > usr_bid:
        usr_bid  = auction_dict[key]
        usr_name = key

print(f"The winning bid was made by {usr_name} of value ${usr_bid}.")


