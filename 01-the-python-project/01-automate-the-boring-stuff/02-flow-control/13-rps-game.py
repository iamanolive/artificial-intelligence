import random, sys

print("ROCK, PAPER, SCISSORS")

# these variables keep track of the number of wins, losses and ties
wins = 0
losses = 0
ties = 0

while True: # the main game loop
    print("%s wins, %s losses, %s ties" % (wins, losses, ties))
    while True: # the player input loop
        print("enter your move:")
        print("(r)ock (p)aper (s)cissors or (q)uit")
        player_move = input()
        if player_move == "q":
            sys.exit() # quit the program
        if player_move == "r" or player_move == "p" or player_move == "s":
            break # break out of the player input loop
        print("type one of r, p, s, or q")

    # display what the player chose
    if player_move == "r":
        print("ROCK versus...", end = " ")
    elif player_move == "p":
        print("PAPER versus...", end = " ")
    elif player_move == "s":
        print("SCISSORS versus...", end = " ")
    
    # display what the computer chose
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = "r"
        print("ROCK")
    elif random_number == 2:
        computer_move = "p"
        print("PAPER")
    elif random_number == 3:
        computer_move = "s"
        print("SCISSORS")

    # display and record the win/loss/tie
    if player_move == computer_move:
        print("it is a tie!")
        ties = ties + 1
    elif player_move == "r" and computer_move == "s":
        print("you win!")
        wins = wins + 1
    elif player_move == "p" and computer_move == "r":
        print("you win!")
        wins = wins + 1
    elif player_move == "s" and computer_move == "p":
        print("you win!")
        wins = wins + 1
    elif player_move == "r" and computer_move == "p":
        print("you lose!")
        losses = losses + 1
    elif player_move == "p" and computer_move == "s":
        print("you lose!")
        losses = losses + 1
    elif player_move == "s" and computer_move == "r":
        print("you lose!")
        losses = losses + 1