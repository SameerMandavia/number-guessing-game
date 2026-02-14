"""Command-line interface for the number guessing game."""
from .game import generate_secret, check_guess


def run(max_value: int = 100) -> None:
    secret = generate_secret(max_value)
    attempts = 0
    print(f"I've picked a number between 1 and {max_value}. Try to guess it!")
    while True:
        attempts += 1
        try:
            user = input("Your guess: ")
            guess = int(user.strip())
        except (ValueError, EOFError):
            print("Please enter a valid integer.")
            continue

        result = check_guess(secret, guess)
        if result == -1:
            print("Too low — try again.")
        elif result == 1:
            print("Too high — try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


def main() -> None:
    run()
