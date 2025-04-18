import random

def get_user_choice():
    while True:
        user_choice = input("Choose Rock (R), Paper (P), or Scissors (S): ").upper()
        if user_choice in ['R', 'P', 'S']:
            return user_choice
        print("Invalid choice! Try again.")

def get_computer_choice():
    return random.choice(['R', 'P', 'S'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    if (user == 'R' and computer == 'S') or (user == 'P' and computer == 'R') or (user == 'S' and computer == 'P'):
        return "You win!"
    return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
