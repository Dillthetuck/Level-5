

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
    elif choices[computer_input] == 3 and choices[player_input] == 1:
        print(f'The computer chose {computer_input}')
        print('You Won!')
        return 'W'
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
    print()
    print('-------------------------------------------')
    print(f'Score — You: {wins} | Computer: {losses}')
    if wins > losses:
        print("You win!!!")
    else:
        print("You lose!!!")
    print("Thanks for playing!")
    print()



if __name__ == "__main__":
    from random import randint

    #start game function
    num_rounds = start_game()

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
    




    
