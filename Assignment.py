# ==============================================================================
# Level #5 Assignment - Rock Paper Scissors
# IS 303 - Hilton
#
# Create a Python game of Rock Paper Scissors.
# 
# Welcome the user to the game. Ask them how many rounds they would like to play.
# Ensure that the number they enter is an odd number so there cannot be any ties.
# 
# For the game play, ask the user for their choice and then generate a random choice 
# for the computer. (NOTE: Make sure that the user’s choice is valid.) If there is 
# a tie, the game does not count, and we push to the next one. Keep track of the 
# number of wins and losses for both the player and the computer. When the game 
# play is over, determine the overall winner and print the results.
# 
# Build and use at least two custom functions:
# • get_player_choice: This function should prompt the player, convert the response 
#   to lowercase, validate the choice, and return the result.
# • determine_winner: This function should compare the two choices and return "win", 
#   "loss", or "tie".

"""
# Sample Session:
# Welcome to Rock Paper Scissors!
# 
# How many rounds would you like to play: 2
# Sorry, the number must be an odd number. Please try again: 3
# 
# Enter rock, paper, scissors: sandwich
# Sorry, “sandwich” is not a valid choice. Please try again.
# 
# Enter rock, paper, scissors: rock
# The computer chose scissors.
# You won!
# 
# Enter rock, paper, scissors: rock
# The computer chose rock.
# Tie! Play again.
# 
# Enter rock, paper, scissors: scissors
# The computer chose rock.
# You lost!
# 
# Enter rock, paper, scissors: paper
# The computer chose rock.
# You won!
# 
# -------------------------------------------
# Score — You: 2 | Computer: 1
# You win!!!
# Thanks for playing!
# 
# Submit your PUBLIC GitHub link via Canvas.
# ==============================================================================
"""

def start_game():
    # how many rounds, verify if its odd, if not ask again

    print("Welcome to Rock Paper Scissors!")
    print()
    input_rounds = input("How many rounds would you like to play: ")

    while not input_rounds.isdigit() or (int(input_rounds) % 2) == 0:
        input_rounds = input("Sorry, you must input a number and it must be odd. Please try again: ")
    return input_rounds


def get_player_choice():
# get_player_choice: This function should prompt the player, convert the response 
    #   to lowercase, validate the choice, and return the result.
    valid_input= ['rock', 'paper','scissors']
    print()
    while True:
        player_input = input("Enter rock, paper, scissors: ")
        if player_input.strip().lower() in valid_input:
            return player_input.strip().lower()
        print(f'Sorry, {player_input} is not a valid choice. Please try again.')   

def determine_winner(player_input,computer_input):
    # • determine_winner: This function should compare the two choices and return "win", 
    #   "loss", or "tie"
    choices = {
        "paper": 1,
        "scissors": 2,
        'rock': 3,
    }
    if player_input == computer_input:
        print(f'The computer chose {computer_input}')
        print("Tie! Play again.")
    elif choices[player_input] < choices[computer_input] or choices[computer_input] == 1 and choices[player_input] == 3:
        print(f'The computer chose {computer_input}')
        print('You Lost!') 
        return 'L'
    else:
        print(f'The computer chose {computer_input}')
        print('You Won!')
        return 'W'

def get_computer_choice():
    #computer chooses rock,paper, or scissors
    valid_input= ['rock', 'paper','scissors']
    return valid_input[randint(0,2)]

def score_write_up(wins,losses):
    # show score write up function
    print('-------------------------------------------')
    print(f'Score — You: {wins} | Computer: {losses}')
    print("You win!!!")
    print("Thanks for playing!)")



if __name__ == "__main__":
    from random import randint

    #start game function
    num_rounds = start_game()
    print(num_rounds)

    wins = 0
    losses = 0

    while wins + losses < int(num_rounds):

        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        score = determine_winner(player_choice, computer_choice)
        if score == 'W':
            wins += 1
        elif score == 'L':
            losses += 1

    score_write_up(wins,losses)
    




    
