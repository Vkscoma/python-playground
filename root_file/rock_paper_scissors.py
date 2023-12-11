from random import choice

computer_choice = choice(["rock", "paper", "scissors"])
user_choice = input("Do you want - rock, paper, or scissors?\n")

if user_choice == computer_choice:
    print(f"Tie! Player chose {user_choice} and computer chose {computer_choice}")
elif computer_choice == "rock" and user_choice == "scissors":
    print(
        f"Computer wins! Player chose {user_choice} and computer chose {computer_choice}"
    )
elif computer_choice == "paper" and user_choice == "rock":
    print(
        f"Computer wins! Player chose {user_choice} and computer chose {computer_choice}"
    )
elif computer_choice == "scissors" and user_choice == "paper":
    print(
        f"Computer wins! Player chose {user_choice} and computer chose {computer_choice}"
    )
else:
    print(
        f"Player wins! Player chose {user_choice} and computer chose {computer_choice}"
    )
