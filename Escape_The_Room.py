"""
LESSON: 2.4 - While Loops
EXERCISE: Code Your Own

TITLE: [Choose Your Own Adventure]
DESCRIPTION: [Welcome to Choose Your Own Adventure! I hope you enjoy it!]
"""
import datetime
e = datetime.datetime.now()
minute1 = e.minute
hour1 = e.hour
second1 = e.second
# Introduction narration of game
playing = True

loop = 4
print("---------------------------------------------------------")
print("Welcome to Choose Your Own Adventure by Piyush Acharya. To move one from one scene to another, you \nhave to correctly answer the question. It's a bit like Escape The Room. If you're stuck on a \nquestion, just try all of the options to view all of the clever responses I have made. I hope you enjoy it!")
anothergame = input("Ad: Do you want to play another game after this? y/n ")
while playing:
    # First Input Loop
    while loop == 4:
        if loop == 4:
            print("---------------------------------------------------------")
            print("You are standing in an open field west of a white house, with a boarded front door.")
            print("(A secret path leads southwest into the forest.)")
            print("There is a Small Mailbox.")
            second = input("What do you do? You can 'take mailbox', 'open mailbox', 'go east', 'open door', 'take boards', 'look at house', 'go southwest', 'read leaflet' ")

        if second.lower() == ("take mailbox"):
            print("---------------------------------------------------------")
            print("It is securely anchored.")
        elif second.lower() == ("open mailbox"):
            print("---------------------------------------------------------")
            print("Opening the small mailbox reveals a leaflet.")
        elif second.lower() == ("go east"):
            print("---------------------------------------------------------")
            print("The door is boarded and you cannot remove the boards.")
        elif second.lower() == ("open door"):
            print("---------------------------------------------------------")
            print("The door cannot be opened.")
        elif second.lower() == ("take boards"):
            print("---------------------------------------------------------")
            print("The boards are securely fastened.")
        elif second.lower() == ("look at house"):
            print("---------------------------------------------------------")
            print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
        elif second.lower() == ("go southwest"):
            loop = 8
        elif second.lower() == ("read leaflet"):
            print("---------------------------------------------------------")
            print("Welcome to the Choose Your Own Adventure by Piyush Acharya. Your mission is to find a Jade Statue.")
        else:
            print("---------------------------------------------------------")
    

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
            loop = 11
        elif cave_inp.lower() == ("scale staircase"):
            loop = 11
        else:
            print("---------------------------------------------------------")


    # End of game
    while loop == 11:
        if loop == 11:
            print("---------------------------------------------------------")
            print("You have entered a mud-floored room.")
            print("Lying half buried in the mud is an old trunk, bulging with jewels.")
            last_inp = input("What do you do? I won't tell you what to type for this. You only have one chance in this step. If you miss it you lose! ")
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

e = datetime.datetime.now()
minute2 = e.minute
hour2 = e.hour
second2 = e.second

totalhour = hour2 - hour1
totalminute = minute2 - minute1

print("You played this game for " + str(totalhour) + " hour(s) and " + str(totalminute) + " minute(s)!")

print()

print("Thanks for playing my game! Your reward for playing this game is another game (Red Light, Green Light)")

# Red Light Green Light
e = datetime.datetime.now()
minute1 = e.minute
hour1 = e.hour
second1 = e.second

if anothergame == 'y':
    import random
    choice1 = random.randint(1, 2)
    if choice1 == 1:
        who = 'You got caught by the police for running a red light.'
    else:
        who = 'You caused someone to swerve to avoid crashing into you and crash into a street light.'
    print("The goal of this game is to drive your car 10 yards with out runnning a red light. Good Luck!")
    # Loop until the user reaches the goal
    distance = 10
    while distance > 0:

        # Get the user input
        print("You have " + str(distance) + " yards left to go.")
        move = input("Would you like to move (yes or no)? ")
        light = "Yellow"

        # Make a weighted random choice between 2 options:
        # - 25% chance of assigning light to be "Red"
        # - 75% chance of assigning light to be "Green"
        choice = random.randint(1, 100)
        if choice <= 25:
            light = 'Red'
        else:
            light = 'Green'

        # Print the results
        print(light + " Light!")
        if move == "yes":
            if light == "Red":
                print(who + " You have to go back to the start.")
                distance = 10
            if light == "Green":
                distance -= 2

    print("You made it!")

    e = datetime.datetime.now()
minute2 = e.minute
hour2 = e.hour
second2 = e.second

totalhour = hour2 - hour1
totalminute = minute2 - minute1

print("You played this game for " + str(totalhour) + " hour(s) and " + str(totalminute) + " minute(s)!")
print("Thanks for playing and I hope you have a great day!")
# Turn in your Coding Exercise.
