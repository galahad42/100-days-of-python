# TODO:
# - Generate a random account from the game data.
# - Format account data into printable format.
# - Ask user for a guess.
# - # Check if user is correct.
# - # Get follower count.
# - # If Statement
# - Feedback.
# - Score Keeping.
# - Make game repeatable.
# - Make B become the next A.
# - Add art.
# - Clear screen between rounds.

import os
import random
from art import logo
from art import vs
from game_data import data

score = 0

def clear():
    os.system('cls')

def get_random_account():
  return random.choice(data)

def followers(a, b, user_choice):
    global score
    a_followers = a['follower_count']
    b_followers = b['follower_count']

    if user_choice == "a" and a_followers > b_followers:
        score += 1
        print(logo)
        print(f"You're right! Current score: {score}")
        return a

    elif user_choice == "b" and b_followers > a_followers:
        score += 1
        print(logo)
        print(f"You're right! Current score: {score}")
        return b

    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score {score}")
        return 0


def game():
    print(logo)
    global score
    score = 0
    continue_game = True
    a = get_random_account()
    while continue_game:
        b = get_random_account()

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        user_choice = input("Who has more folower? Type 'A' or 'B': ").lower()

        clear()
        a = followers(a, b, user_choice)
        if a == 0:
            continue_game = False
    

game()