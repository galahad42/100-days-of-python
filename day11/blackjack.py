########################## Our Blackjack House Rules ############################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################################################################################

import random
from art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


##################################FUNCTIONS########################################

def clear():
    os.system('cls')


def ace(hand):
    for card in hand:
        if card == 11:
            card = 1
            break
    return hand


def computer_total(computer_hand):
    
    while sum(computer_hand) < 17:
        computer_hand.append(random.choice(cards))

        if sum(computer_hand) > 21:
            computer_hand = ace(computer_hand)

    return computer_hand


def display(player_hand, computer_hand, hit_or_pass):
    if hit_or_pass == "hit":
        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"Computer's first card: {computer_hand}")

    elif hit_or_pass == "pass":
        print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
        print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")


def win(player_hand, computer_hand):
    win = "You win."
    lose = "You lose."

    if player_hand == 21:
        print(win)
    elif player_hand > 21:
        print(lose)
    elif player_hand < 21:
        if computer_hand == 21:
            print(lose)
        elif computer_hand > 21:
            print(win)
        elif computer_hand < 21:
            if player_hand > computer_hand:
                print(win)
            elif player_hand < computer_hand:
                print(lose)
            elif player_hand == computer_hand:
                print("Its a draw.")


def start_game():
    print(logo)
    print("")

    player_hand = random.sample(cards, 2)
    computer_hand = random.sample(cards, 1)

    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer's first card: {computer_hand}")

    continue_game = True
    while continue_game:
        hit_or_pass = input("Type 'hit' to get another card, type 'pass' to pass: ").lower()
        
        if hit_or_pass == "hit":
            player_hand.append(random.choice(cards))
            display(player_hand, computer_hand, hit_or_pass)

            if sum(player_hand) > 21:
                player_hand = ace(player_hand)

            if sum(player_hand) >= 21:
                continue_game = False

        elif hit_or_pass == "pass":
            continue_game = False

    computer_hand = computer_total(computer_hand)
    print(f"\nYour final hand: {player_hand}, final score: {sum(player_hand)}")
    print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")

    win(sum(player_hand), sum(computer_hand))

###########################################################################################


# driver code
play_game = True
while play_game:
    if input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
        clear()
        start_game()
    else:
        play_game = False