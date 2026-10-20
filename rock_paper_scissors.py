import random


def play_rps():
  print("--- Welcome to Rock, Paper, Scissors! ---")
  print("Type 'rock', 'paper', or 'scissors' to play.")
  print("Type 'quit' at any time to end the game and see your final score.\n")

  choices = ["rock", "paper", "scissors"]
  user_score = 0
  computer_score = 0
  ties = 0

  while True:
    user_choice = input("Enter your choice (rock/paper/scissors/quit): ").lower().strip()

    if user_choice == "quit":
      print("\n" + "=" * 30)
      print("--- Final Score Summary ---")
      print(f"You wins: {user_score}")
      print(f"Computer wins: {computer_score}")
      print(f"Ties: {ties}")
      print("Thanks for playing!")
      print("=" * 30)
      break

    if user_choice not in choices:
      print("Invalid choice. Please type rock, paper, or scissors.\n")
      continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
      print("It's a tie!\n")
      ties += 1
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
      print("🎉 You win this round!\n")
      user_score += 1
    else:
      print("💻 Computer wins this round!\n")
      computer_score += 1

    # Display running scoreboard
    print(f"Scoreboard -> You: {user_score} | Computer: {computer_score} | Ties: {ties}")
    print("-" * 45)


if __name__ == "__main__":
  play_rps()