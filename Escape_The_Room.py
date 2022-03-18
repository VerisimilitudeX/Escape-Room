"""
LESSON: 4.1 - Lists
EXERCISE: Code Your Own
----------------------------------------------------------
Choose Your Own Adventure
Welcome to Choose Your Own Adventure! I hope you enjoy it!
"""

# Import Libraries
import pygame
pygame.init()

# Define Variables
c = pygame.time.Clock()
playing = True
loop = 4
correct_answers = []

print("---------------------------------------------------------")
print("Welcome to Choose Your Own Adventure by Piyush Acharya. To move one from one scene to another, you have to correctly answer the question. It's a bit like Escape The Room. I hope you enjoy it!")
pygame.time.wait(5000)
while playing:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    # Intro Loop
    while loop == 4:
        intro_options = ['take mailbox', 'open mailbox', 'go east', 'open door', 'take boards', 'look at house', 'go southwest', 'read leaflet']
        if loop == 4:
            print("---------------------------------------------------------")
            print("You are standing in an open field west of a white house, with a boarded front door.")
            print("(A secret path leads southwest into the forest.)")
            print("There is a Small Mailbox.")
            second = input("What do you do? You can " + str(intro_options))

        if second.lower() == intro_options[0]:
            print("---------------------------------------------------------")
            print("It is securely anchored.")
            pygame.time.wait(2000)
        elif second.lower() == intro_options[1]:
            print("---------------------------------------------------------")
            print("Opening the small mailbox reveals a leaflet.")
            pygame.time.wait(2000)
        elif second.lower() == intro_options[2]:
            print("---------------------------------------------------------")
            print("The door is boarded and you cannot remove the boards.")
            pygame.time.wait(2000)
        elif second.lower() == intro_options[3]:
            print("---------------------------------------------------------")
            print("The door cannot be opened.")
            pygame.time.wait(2000)
        elif second.lower() == intro_options[4]:
            print("---------------------------------------------------------")
            print("The boards are securely fastened.")
            pygame.time.wait(2000)
        elif second.lower() == intro_options[5]:
            print("---------------------------------------------------------")
            print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
            pygame.time.wait(2000)
        elif second.lower() == intro_options[6]:
            correct_answers.append(intro_options[6])
            loop = 8
            pygame.time.wait(2000)
        elif second.lower() == intro_options[7]:
            print("---------------------------------------------------------")
            print("Welcome to the Choose Your Own Adventure by Piyush Acharya. Your mission is to find a Jade Statue.")
            pygame.time.wait(2000)
        else:
            print("You entered something that the program can't recognize. Please restart it. ")
            pygame.time.wait(4000)
            break    

    # Southwest Loop
    while loop == 8:
        if loop == 8:
            print("---------------------------------------------------------")
            print("This is a forest, with trees in all directions. To the east, there appears to be sunlight. Your options are 'go west', 'go north', 'go south', 'go east' ")
            forest_inp = input("What do you do? You can 'go west', 'go north', 'go south', 'go east' ")

        if forest_inp.lower() == ("go west"):
            print("---------------------------------------------------------")
            print("You would need a machete to go further west.")
        elif forest_inp.lower() == ("go north"):
            print("---------------------------------------------------------")
            print("The forest becomes impenetrable to the North.")
        elif forest_inp.lower() == ("go south"):
            print("---------------------------------------------------------")
            print("Storm-tossed trees block your way.")
        elif forest_inp.lower() == ("go east"):
            correct_answers.append("go east")
            loop = 9
        else:
            print("---------------------------------------------------------")
    
    # East Loop and Grating Input
    while loop == 9:
        if loop == 9:
            print("---------------------------------------------------------")
            print("You are in a clearing, with a forest surrounding you on all sides. A path leads south. Your options are 'go south', 'descend grating' ")
            print("There is an open grating, descending into darkness.")
            grating_inp = input("What do you do? You can 'go south' or 'descend grating' ")

        if grating_inp.lower() == ("go south"):
            print("---------------------------------------------------------")
            print("You see a large ogre and turn around.")
        elif grating_inp.lower() == ("descend grating"):
            correct_answers.append("descend grating")
            loop = 10
        else:
            print("---------------------------------------------------------")    

    # Grating Loop and Cave Input
    while loop == 10:
        if loop == 10:
            print("---------------------------------------------------------")
            print("You are in a tiny cave with a dark, forbidding staircase leading down.")
            print("There is a skeleton in one corner.")
            cave_inp = input("What do you do? You can 'descend staircase', 'take skeleton', 'smash skeleton', 'light up room', 'break skeleton', 'go down staircase', 'scale staircase' ")

        if cave_inp.lower() == ("descend staircase"):
            correct_answers.append("descend grating")
            loop = 11
        elif cave_inp.lower() == ("take skeleton"):
            print("---------------------------------------------------------")
            print("Why would you do that? Are you crazy?")
        elif cave_inp.lower() == ("smash skeleton"):
            print("---------------------------------------------------------")
            print("Really?")
        elif cave_inp.lower() == ("light up room"):
            print("---------------------------------------------------------")
            print("You would need a torch or lamp to do that.")
        elif cave_inp.lower() == ("break skeleton"):
            print("---------------------------------------------------------")
            print("I have two questions: Why and with what?")
        elif cave_inp.lower() == ("go down staircase"):
            correct_answers.append("go down staircase")
            loop = 11
        elif cave_inp.lower() == ("scale staircase"):
            correct_answers.append("scale staircase")
            loop = 11
        else:
            print("---------------------------------------------------------")

    # End of game
    while loop == 11:
        if loop == 11:
            print("---------------------------------------------------------")
            print("You have entered a mud-floored room.")
            print("Lying half buried in the mud is an old trunk, bulging with jewels.")
            last_inp = input("What do you do? There are no options, you only have one chance in this step. If you miss it you lose! ")
            if last_inp.lower() == ("open trunk"):
                print("---------------------------------------------------------")
                print("You have found the Jade Statue and have completed your quest! Good job!")
                print("*******************************************************************************")
                print("          |                   |                  |                     |       ")
                print(" _________|________________.=""_;=.______________|_____________________|_______")
                print("|                   |  ,-/_,=""     `\=.|                  |                   ")
                print("|___________________|__-=._o`,-._        `:=.______________|___________________")
                print("          |                `,=._o`,=._      _`,=._                     |       ")
                print(" _________|_____________________:=._o ,=._.,_.-=,,,=.__________________|_______")
                print("|                   |    __.--, , ; `,=._o., ,-"",-._ ,.   |                   ")
                print("|___________________|_._,  ,. .` ` `` ,  `,-._,-._   ,. '__|___________________")
                print("          |           |o`,=._` , ,` `; .,. ,  ,-._,-._; ;              |       ")
                print(" _________|___________| ;`-.o`,=._; ., ` '`.,\` . ,-._ /_______________|_______")
                print("|                   | |o;    `,-.o`,=._``  '` , ,__.--o;   |                   ")
                print("|___________________|_| ;     (#) `-.o `,=.`_.--,_o.-; ;___|___________________")
                print("____/______/______/___|o;._    ,      `,.o|o_.--,    ;o;____/______/______/____")
                print("/______/______/______/_,=._o--._        ; | ;        ; ;/______/______/______/_")
                print("____/______/______/______/__,=._o--._   ;o|o;     _._;o;____/______/______/____")
                print("/______/______/______/______/____,=._o._; | ;_.--,o.--,_/______/______/______/_")
                print("____/______/______/______/______/_____,=.o|o_.--,,___/______/______/______/____")
                print("/______/______/______/______/______/______/______/______/______/______/______/ ")
                print("*******************************************************************************")
                correct_answers.append("open trunk")
                loop = 11
        else:
            print("---------------------------------------------------------")
        
        # Exit loop at the end of game
        exit_inp = input("Play again? y/n ")
        if exit_inp.lower() == ("n"):
            playing = False
            break
        if exit_inp.lower() == ("y"):
            loop = 4
print()
print("Thanks for playing my game! You completed the following options: " + str(correct_answers))
