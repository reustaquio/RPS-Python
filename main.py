import random


def getChoices():
    player_choice = input("Enter your choice (rock, paper or scissors): ")

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {"computer": computer_choice, "player": player_choice}

    return choices


def check_win(computer, player):
    print(f"you chose {player} and computer chose {computer}")

    if computer == player:
        return "It's a tie. :-)"
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors. You win!"
        if computer == "paper":
            return "paper covers rock. You lose."
    elif player == "paper":
        if computer == "scissors":
            return "scissors cuts paper. You lose."
        if computer == "rock":
            return "paper covers rock. You win!"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper. You win!"
        if computer == "rock":
            return "rock smashes scissors. You lose."
    else:
        return "your choice is invalid."


choices = getChoices()

result = check_win(choices["computer"], choices["player"])
print(result)
