"""Core game logic for the number guessing game.

This module is small and written to be easily unit-tested.
"""
from typing import Literal
import random


def generate_secret(max_value: int = 100) -> int:
    """Return a secret number between 1 and `max_value` inclusive."""
    if max_value < 1:
        raise ValueError("max_value must be >= 1")
    return random.randint(1, max_value)


def check_guess(secret: int, guess: int) -> Literal[-1, 0, 1]:
    """Compare `guess` to `secret`.

    Returns:
    -1 if guess is lower than secret
     1 if guess is higher than secret
     0 if guess equals secret
    """
    if guess < secret:
        return -1
    if guess > secret:
        return 1
    return 0
