import random

# =========================================
# ROCK PAPER SCISSORS GAME
# =========================================

print("===================================")
print("   ROCK PAPER SCISSORS GAME")
print("===================================")

# Game loop
while True:

    # Choices list
    choices = ["rock", "paper", "scissors"]

    # Computer chooses randomly
    computer = random.choice(choices)

    # User input
    user = input("\nEnter rock, paper, or scissors: ").lower()

    # Check valid input
    if user not in choices:
        print("❌ Invalid Choice")
        continue

    print("\nYou Chose:", user)
    print("Computer Chose:", computer)

    # ---------------- GAME LOGIC ----------------

    # Draw condition
    if user == computer:
        print("🤝 It's a Draw")

    # Winning conditions
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("🎉 You Win!")

    # Losing condition
    else:
        print("💻 Computer Wins")

    # ---------------- PLAY AGAIN ----------------
    play_again = input("\nDo You Want to Play Again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n👋 Thanks For Playing!")
        break