import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("⚠️ Invalid choice!")
        choice = input("Please enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

def main():
    print("==== Rock-Paper-Scissors Game ====")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\n🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("⚖️ It's a tie!")
        elif result == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😞 Computer wins this round.")
            computer_score += 1

        print(f"\n🔢 Scores => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("👋 Thanks for playing! Final Scores:")
            print(f"🏁 You: {user_score} | 💻 Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()
