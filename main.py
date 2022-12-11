import random


def play_game(player_move: str) -> str:
    # Choose a random move for the computer
    computer_move = random.choice(["rock", "paper", "scissors"])

    # Determine the outcome of the game
    if player_move == "rock" and computer_move == "scissors":
        outcome = "Player wins"
    elif player_move == "rock" and computer_move == "paper":
        outcome = "Computer wins"
    elif player_move == "paper" and computer_move == "rock":
        outcome = "Player wins"
    elif player_move == "paper" and computer_move == "scissors":
        outcome = "Computer wins"
    elif player_move == "scissors" and computer_move == "rock":
        outcome = "Computer wins"
    elif player_move == "scissors" and computer_move == "paper":
        outcome = "Player wins"
    else:
        outcome = "Tie"

    # Print the outcome of the game
    print("Player chose", player_move)
    print("Computer chose", computer_move)
    print("Outcome:", outcome)

    # Return the outcome
    return outcome


# Play a game of rock-paper-scissors
play_game("rock")
