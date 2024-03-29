import random

# Rock
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Win
win = """
                                                                                                    
                                                                                                    
          @@@.   @@@   &@@@/,#@@@*  .@@.    /@@       &@@   &@@@    @@  %@@  *@@@,   /@@            
            @@@/@@.   @@@       @@( .@@.    /@@        @@* .@@.@@  %@@  %@@  *@@@@@  /@@            
             %@@@     @@@       @@& .@@.    /@@        #@@ @@, &@@ @@   %@@  *@@ /@@,/@@            
              @@.     #@@,     %@@   @@/    #@@         @@@@@   @@@@@   %@@  *@@   @@@@@            
              @@.       @@@@@@@@%     @@@@@@@@          *@@@    .@@@    %@@  *@@    (@@@            
                                                                                                    
                                                                                                    """
# Lose
lose = """
                                                                                                    
                                                                                                    
   ,@@&    @@@   (@@@@@@@@%   (@@     @@@        @@,         @@@@@@@@@.   /@@@@@@@@   %@@@@@@@@@    
     @@@ *@@,   @@@      &@@  (@@     @@@        @@,        @@(      @@@  @@&         %@@           
       @@@@     @@*      .@@* (@@     @@@        @@,       @@@       @@@   *@@@@@@@   %@@@@@@@@%    
       (@@      @@@      %@@  *@@     @@@        @@,       .@@*      @@@         %@@  %@@           
       (@@       @@@@@@@@@@    @@@@@@@@@.        @@@@@@@@@   @@@@@@@@@(   @@@@@@@@@%  %@@@@@@@@@,   
                                                                                                    
                                                                                                    """
# Draw
draw = """
                                                                                                    
                                                                                                    
                     ,@@@@@@@@@    @@@@@@@@@@      @@@@     @@(   @@@@    @@.                       
                     ,@@     /@@.  @@,    ,@@.    @@(@@@    (@@  %@@%@@  @@@                        
                     ,@@      @@#  @@@@@@@@@     @@&  @@@    @@& @@  @@**@@                         
                     ,@@     (@@   @@,  ,@@@    @@@@@@@@@@    @@@@(   @@@@(                         
                     ,@@@@@@@@@    @@,    &@@/ @@@      @@@   @@@@    %@@@                          
                                                                                                    
                                                                                                    """

list = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n>>"))
comp_choice = random.randint(0,2)
if(user_choice > 2 or user_choice < 0):
    print("Please enter a valid option. You lose.")
else:
    diff = user_choice - comp_choice
    print(f"You chose: \n\n{list[user_choice]}")
    print(f"Computer chose:\n\n{list[comp_choice]}")

    if   (diff == 1 or diff == -2):
        print(f"\n{win}")
    elif (diff == -1 or diff == 2):
        print(f"\n{lose}")
    elif (diff == 0):
        print(f"\n{draw}")

