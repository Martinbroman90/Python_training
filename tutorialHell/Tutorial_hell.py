import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_score = 0
    computer_score = 0
    rounds_to_win = 2

    while user_score < rounds_to_win and computer_score < rounds_to_win:
        print("\nCurrent score - You:", user_score, "Computer:", computer_score)

        while True:
            user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
            if user_choice in ['rock', 'paper', 'scissors']:
                break
            print("Invalid input. Please try again.")

        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == 'user':
            print("You win this round!")
            user_score += 1
        elif winner == 'computer':
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

    print("\nFinal score - You:", user_score, "Computer:", computer_score)
    if user_score > computer_score:
        print("Congratulations! You win the game!")
    else:
        print("Computer wins the game. Better luck next time!")

if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors!")
    print("Best of 3 rounds. First to win 2 rounds wins the game.")
    play_game()
