print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************

''')

print("Welcome to Treasure Island\nYour mission is to find the treasure.\n")
print("You walk along the trail until you find youreself in front of a crossroad.")
print("The road on the left is grassy and less trodden.")
print("The road on the right is more trodden but darker.")
error_msg = "\nPlease type the correct option."

choice1 = input("Which road do you choose to travel further. Type 'left' or 'right': ")

if (choice1 == "right"):
    print("\nYou walk into a beartrap on this road and die due to blood loss.\nGame over.")
elif (choice1 == "left"):
    print("\nYou continue your journey safely until you find yourself in front of a river")
    choice2 = input("Do you want to swim across the river or wait for a boat? Type 'swim' or 'wait' ")

    if (choice2 == "swim"):
        print("\nThe is river is filled with hungry crocodiles and you die instantly.\nGame over.")
    elif (choice2 =="wait"):
        print("\nA fisherman comes along in an hour and agrees to give you passage across the river for gold")
        print("After crossing the river you find the temple of the son god Leto where the fabled lost treasure is said to burried in.")
        print("Inside the temple you find 3 doors looking exactly the same but with 3 different coloured emaralds attached to them:red, blue and yellow")
        choice3 = input("Which door do you choose to go in first? Type 'red' or 'yellow' or 'blue' ")

        if (choice3 == "red"):
            print("\nYou open the door with the red emarald and its dark inside. You carefully walk inside but the door locks behind you.")
            print("You panic and run towards the end of the room which is shining only to find out that the room is filled with poisonous snakes")
            print("Game over.")
        elif (choice3 == "blue"):
            print("\nYou open the door with the blue emarald and walk inside. All seems natural until the heat in the room starts increasings.")
            print("You find the walls are all burning hot and the temperature is increasing rapidly. You faint.")
            print("Game over")
        elif (choice3 == "yellow"):
            print("\nYou open the door with the yellow emarald and walk inside. You can see the staue of the sun god Leto in the other end of the room")
            print("You make your way to the staue and find its made of gold and stands on a treasure box.")
            print("Congratulations young adventurer! You have found the lost treasure!")
        else:
            print(error_msg)
    else:
        print(error_msg)
else:
    print(error_msg)
