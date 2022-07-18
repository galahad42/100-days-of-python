import random
from hangman_art import stages, logo
from hangman_words import word_list


################################### FUNCTIONS ###############################################
def play_again():
    global play_game
    play_game = int(input("Do you want to play? Type 1 for yes and 0 for no:\n>> "))


def replace_blank(user_guess):
    for i in range(0, word_length):
        if user_guess == choose_word[i]:
            blank_word_list[i] = user_guess

        else:
            continue


def check_win():
    global win
    global lives
    if "_" in blank_word_list:
        win = False
        
    else:
        win = True
        lives = 0


def correct_output():
    print("")
    print(*blank_word_list, sep=" ")
    print(f"\n{stages[len(stages)-lives-1]}")


def wrong_output():
    print("")
    print(*blank_word_list, sep= " ")
    print(f"\nYou guessed {user_guess}, that's not in the word. You lose a life.")
    print(f"\n{stages[len(stages)-lives-1]}")

##########################################################################################

print(logo)
play_again()

while play_game:
    choose_word = random.choice(word_list)
    word_length = len(choose_word)

    blank_word_list = ["_"]*word_length

    lives = len(stages)-1
    win = False

    while lives:
        user_guess = input("\nGuess a letter: ").lower()

        if user_guess in choose_word:
            replace_blank(user_guess)
            correct_output()
            check_win()
            
        else:
            lives -= 1
            wrong_output()

    if win == True:
        print("You win.")
        play_again()
    elif win == False:
        print("You lose.")
        play_again()