print("Welcome to the Love Calaculator!\n")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
l_name1 = name1.lower()
l_name2 = name2.lower()

# TRUE
t1 = l_name1.count("t") + l_name1.count("r") + l_name1.count("u") + l_name1.count("e")
t2 = l_name2.count("t") + l_name2.count("r") + l_name2.count("u") + l_name2.count("e")
t  = t1 + t2

# LOVE
l1 = l_name1.count("l") + l_name1.count("o") + l_name1.count("v") + l_name1.count("e")
l2 = l_name2.count("l") + l_name2.count("o") + l_name2.count("v") + l_name1.count("e")
l  = l1 + l2

score = 10*t + l
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like code and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")