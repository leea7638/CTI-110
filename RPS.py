import random

FIGHTERS = ["Crusher", "Phantom", "Reaper"]
MOVES = ["rock", "paper", "scissors"]
STARTING_COINS = 100


def choose_move():
    return random.choice(MOVES)


def find_winners(results):
    # If everyone picks the same move, nobody wins.
    if len(set(results.values())) == 1:
        return []

    # If all three moves appear, the round is a cycle.
    if len(set(results.values())) == 3:
        return []

    beats = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    # With two different moves, the winning move beats
    # the losing move. All computers playing the winning
    # move are considered co-winners.
    moves = set(results.values())
    winning_move = next(
        move for move in moves
        if beats[move] in moves
        and beats[beats[move]] not in moves
    )

    return [
        fighter for fighter, move in results.items()
        if move == winning_move
    ]


def get_bet(balance):
    while True:
        try:
            amount = int(input(
                f"Your balance is {balance} coins. "
                "Enter your wager: "
            ))

            if 1 <= amount <= balance:
                return amount

            print(f"Choose between 1 and {balance}.")

        except ValueError:
            print("Please enter a whole number.")


def play():
    balance = STARTING_COINS
    wins = 0
    losses = 0

    print("\n===================================")
    print("       ROCK PAPER SCISSORS")
    print("            FATE ARENA")
    print("===================================")

    print("\nChoose your fighter:")
    for i, fighter in enumerate(FIGHTERS, start=1):
        print(f"{i}. {fighter}")

    while balance > 0:
        print(f"\nAvailable coins: {balance}")

        for i, fighter in enumerate(FIGHTERS, start=1):
            print(f"{i}. Bet on {fighter}")

        print("Q. Quit")

        choice = input("Select a fighter: ").strip().lower()

        if choice == "q":
            break

        if choice not in ("1", "2", "3"):
            print("Invalid selection.")
            continue

        selected = FIGHTERS[int(choice) - 1]
        bet = get_bet(balance)
        balance -= bet

        print(f"\nYou wagered {bet} coins on {selected}!")
        print("LET FATE DECIDE...")

        while True:
            results = {
                fighter: choose_move()
                for fighter in FIGHTERS
            }

            print("\n--- BATTLE ---")
            for fighter, move in results.items():
                print(f"{fighter:10} plays {move.upper()}")

            winners = find_winners(results)

            if winners:
                break

            print("No winner! The computers battle again...")
            input("Press Enter to reroll the moves.")

        print("\nWinner(s): " + ", ".join(winners))

        if selected in winners:
            winnings = bet * 3
            balance += winnings
            wins += 1
            print(f"YOU WON! {winnings} coins returned!")
            print(f"Net profit: +{bet * 2} coins")
        else:
            losses += 1
            print(f"Bad luck! You lost {bet} coins.")

        print("\n========== SCOREBOARD ==========")
        print(f"Winning bets: {wins}")
        print(f"Losing bets:  {losses}")
        print(f"Balance:      {balance} coins")

        if balance <= 0:
            print("You're out of coins!")

    print("\n========== FINAL RESULTS ==========")
    print(f"Winning bets: {wins}")
    print(f"Losing bets:  {losses}")
    print(f"Final balance: {balance} coins")
    print("Thanks for playing Fate Arena!")


if __name__ == "__main__":
    play()
