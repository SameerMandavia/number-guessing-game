import builtins
from unittest.mock import patch

from number_guessing_game.game import check_guess, generate_secret


def test_check_guess_lower():
    assert check_guess(10, 5) == -1


def test_check_guess_higher():
    assert check_guess(10, 20) == 1


def test_check_guess_equal():
    assert check_guess(7, 7) == 0


def test_generate_secret_bounds():
    # patch random.randint to return a predictable value
    with patch("random.randint", return_value=42):
        assert generate_secret(100) == 42


def test_generate_secret_invalid():
    try:
        generate_secret(0)
    except ValueError:
        return
    raise AssertionError("generate_secret should raise ValueError for max_value < 1")
