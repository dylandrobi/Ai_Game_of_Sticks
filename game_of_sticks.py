# Name: Dylan Robichaud
# Class: CS106 Fall 2022
# Project 3, Game of Sticks: Ai vs. Human
#
# Program "game of sticks" so that two AI's play eachother in game of sticks at leasst 100 times, where after each round, both
# AI's have learned from their previous moves. If they make a move that causes them to win, their odds of choosing that move
# at the given scenario (amount of sticks on the table), increases. If they lose, then their odds of choosing each move at the
# given scenario decreases or remains the same. Once the AI is trained, a human plays against it and is challenged because
# the AI makes the best moves possible.

import random


def get_yn_input():
    """Get a yes/no answer from the user."""
    yes_no = input("Do you want to play again? Type y or n.    ")
    while yes_no not in ["y", "n"]:
        print("Please input 'y' or 'n'.")
        yes_no = input("Do you want to play again? Type y or n.    ")
    return yes_no


def introduction():
    """Print a welcome message and determine how many sticks should be used."""
    print("Welcome to the game of sticks!")
    total_sticks = int(input("How many sticks are there on the table initially (10-100)?"))
    print("Training AI, please wait...")
    while total_sticks not in range(10, 101):
        print("Please input a number 10-100")
        total_sticks = int(input("How many sticks are there on the table initially (10-100)?"))
    return total_sticks
    print("")


def one_round_of_sticks(total_sticks, player1, player2, hats):
    """player1 and player2 (trained AI) play one round of sticks against each other.
    They start with a pile of total_sticks sticks."""
    current_player = player1
    other_player = player2
    initial_total_sticks = total_sticks
    print("")
    print("There are ", total_sticks, " sticks on the board.")
    while total_sticks > 0:
        take_1 = int(input("Player 1: How many sticks do you take? (1-3)"))
        while take_1 not in [1, 2, 3]:
            print("Please input a number 1-3 ")
            take_1 = int(input("Player 1: How many sticks do you take? (1-3)"))
        total_sticks = total_sticks - take_1
        if total_sticks <= 0:
            print("Player 1, you lose.")
        else:
            print(" ")
            print("There are ", total_sticks, " sticks on the board.")
            ai_rand_choice = random.choice(hats[total_sticks - 1])
            total_sticks = total_sticks - ai_rand_choice
            print("AI selects " + str(ai_rand_choice) + ".")
            if total_sticks <= 0:
                print("AI loses")
            else:
                print(" ")
                print("There are ", total_sticks, " sticks on the board.")


def train_ai(total_sticks, player2, player3, hats, besides_hats, hats2, besides_hats2):
    """Player 2 (trained AI) plays a game of sticks with player 3 (other AI) and every round, both player's hats are updated """
    current_player = player2
    other_player = player3
    initial_total_sticks = total_sticks

    while total_sticks > 0:
        # Player 3 randomly chooses an amount of sticks to take based off the contents of their hat at that given index.
        ai_rand_choice2 = random.choice(hats2[total_sticks - 1])
        if ai_rand_choice2 in hats2[total_sticks - 1]:
            hats2[total_sticks - 1].remove(ai_rand_choice2)
            besides_hats2[total_sticks - 1] += [ai_rand_choice2]
        total_sticks = total_sticks - ai_rand_choice2
        if total_sticks <= 0:
            # Player 3 loses, meaning Player 3's besides hats contents are added back to the hats if they don't already exist in each
            # corresponding hat, and two of Player 3's besides hats contents are added back to the hats at the corresponding indices.
            for i in range(1, len(hats)):
                if len(besides_hats[i]) >= 1:
                    hats[i].insert(-1, besides_hats[i][0])
                    hats[i].insert(-1, besides_hats[i][0])
                    besides_hats[i].pop(0)
                for ball in besides_hats2[i - 1]:
                    if ball not in hats2[i - 1]:
                        hats2[i - 1].append(besides_hats2[i - 1][0])
                        besides_hats2[i - 1].pop(0)
                    else:
                        besides_hats2[i - 1].pop(0)
        # Player 2 randomly chooses an amount of sticks to take based off the contents of their hat at that given index.
        ai_rand_choice = random.choice(hats[total_sticks - 1])
        if ai_rand_choice in hats[total_sticks - 1]:
            hats[total_sticks - 1].remove(ai_rand_choice)
            besides_hats[total_sticks - 1] += [ai_rand_choice]
        total_sticks = total_sticks - ai_rand_choice
        if total_sticks <= 0:
            # Player 2 loses, meaning Player 2's besides hats contents are added back to the hats if they don't already exist in each
            # corresponding hat, and two of Player 2's besides hats contents are added back to the hats at the corresponding indices.
            for i in range(1, len(hats)):
                if len(besides_hats2[i]) >= 1:
                    hats2[i].insert(-1, besides_hats2[i][0])
                    hats2[i].insert(-1, besides_hats2[i][0])
                    besides_hats2[i].pop(0)

                for ball in besides_hats[i - 1]:
                    if ball not in hats[i - 1]:
                        hats[i - 1].append(besides_hats[i - 1][0])
                        besides_hats[i - 1].pop(0)
                    else:
                        besides_hats[i - 1].pop(0)


def initialize_ai(player_num, total_sticks):
    """Create a new AI player represented as a 4-tuple of the form
    (player_num, "ai", hats, besides_hats)."""
    hats = []
    hats2 = []

    # Initiate the contents in each hat
    for count in range(0, total_sticks):
        hats.append([1, 2, 3])
        hats2.append([1, 2, 3])

    # Initiate empty besides hats
    besides_hats = []
    besides_hats2 = []
    for count in range(0, total_sticks):
        besides_hats.append([])
        besides_hats2.append([])
    return (player_num, "trained_ai", "ai2", hats, besides_hats, hats2, besides_hats2)


def sticks():
    """Main function for the game of sticks"""
    total_sticks = introduction()
    player1 = (1, "human")
    player2 = initialize_ai(2, total_sticks)
    player3 = initialize_ai(3, total_sticks)
    keep_playing = 'y'

    # Set an amount of rounds the two AI's play for
    for count in range(100):
        train_ai(total_sticks, player2, player3, player2[3], player2[4], player3[5], player3[6])
        keep_playing = 'y'
    print("HATS:", player2[3])
    print("HATS2:", player3[5])
    while keep_playing == 'y':
        one_round_of_sticks(total_sticks, player1, player3, player3[5])
        keep_playing = get_yn_input()
        if keep_playing == 'y':
            print("Great!")
    print("Ok. See you next time. Bye, bye!")


### DO NOT DELETE THIS LINE: beg testing

sticks()