import random

Quit = False
user_points = 0
computer_points = 0



while Quit == False :
    options = ["Rock", "Paper", "scissors", "Quit"]
    user_input = input("choose rock,paper,scissor or quit")
    computer_input = random.choice(options)

    if user_input.capitalize() == "Quit":
        print("Game ended")
        Quit = True

    if user_input.capitalize() == 'Rock':
        if computer_input == "Rock":
            print("your input is Rock")
            print("computer's input is Rock")
            print("its a tie")
        elif computer_input == "Paper":
            print("your input is Rock")
            print("computer's input is Paper")

            computer_points += 1
            print("you lose Computer score " + str(computer_points) + " points")
        elif computer_input == "Scissor":
            print("your input is Rock")
            print("computer's input is Scissor")

            computer_points += 1
            print("you win you score " + str(user_points)+' points')

    elif user_input.capitalize() == "Paper":
        if computer_input == "Rock":
            print("your input is Paper")
            print("computer's input is Rock")

            user_points += 1
            print("you win you score "+str(user_points)+" points")
        elif computer_input == "Paper":
            print("your input is Paper")
            print("computer's input is Paper")
            print("its a tie")
        elif computer_input == "Scissor":
            print("your input is Rock")
            print("computer's input is Rock")

            computer_points += 1
            print("you lose Computer score " + str(computer_points) + " points")

    elif user_input.capitalize() == "Scissor":
        if computer_input == "Rock":
            print("your input is Scissor")
            print("computer's input is Rock")

            computer_points += 1
            print("you lose Computer score " + str(computer_points) + " points")
        elif computer_input == "Paper":
            print("your input is Scissor")
            print("computer's input is Paper")

            user_points += 1
            print("you win you score " + str(user_points) + ' points')
        elif computer_input == "Scissor":
            print("your input is Scissor")
            print("computer's input is Scissor")
            print("its a tie")

    elif user_input.capitalize() != 'Rock' or user_input.capitalize() != 'Paper' \
            or user_input.capitalize() != 'Scissor':
        print('invalid input')



















