"""number_guessing_game package

Expose package version and a small CLI entrypoint.
"""

__version__ = "0.1.0"

from .game import check_guess, generate_secret

__all__ = ["check_guess", "generate_secret"]
