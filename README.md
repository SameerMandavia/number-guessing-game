# number-guessing-game

Small, testable Python implementation of a number guessing game.

Project structure created to separate source, tests and CI.

Quickstart
---------

- Install (recommended in a venv):

```
python -m venv .venv; .\.venv\Scripts\Activate.ps1; python -m pip install -r requirements.txt
```

- Run tests:

```
pytest -q
```

- Run the interactive CLI:

```
python -m number_guessing_game
```

What's included
----------------

- `src/number_guessing_game` : package with game logic and CLI.
- `tests/` : unit tests for core logic.
- `.github/workflows/ci.yml` : GitHub Actions to run tests.
- `requirements.txt` : test/runtime dependencies.

If you'd like a different layout (packaging with `pyproject.toml`, additional CLI options, or a web UI), tell me and I can iterate.
Computer generates random number, User keeps guessing until correct, Show number of attempts

**App Flow**

- **Start / entry point**: Users run the app with `python -m number_guessing_game` from the project root. This executes `src/number_guessing_game/__main__.py`, which calls `cli.main()`.
- **CLI startup**: `cli.main()` calls `cli.run()` (default `max_value=100`). `run()` calls `generate_secret(max_value)` to pick a random secret number between `1` and `max_value`.
- **Interactive loop**: `run()` prints instructions and enters a loop where it:
	- Prompts the user with `input("Your guess: ")`.
	- Attempts to parse the input to an `int` with `guess = int(user.strip())`.
	- If parsing fails (`ValueError`) or input is closed (`EOFError`), the code prints `Please enter a valid integer.` and continues the loop.
	- If parsing succeeds, it calls `check_guess(secret, guess)` which returns `-1` (guess too low), `1` (guess too high), or `0` (correct).
	- Based on the return value, the CLI prints a hint (`Too low — try again.` or `Too high — try again.`) or the success message `Correct! You guessed it in {attempts} attempts.` and breaks the loop.

- **Core logic (pure functions)**:
	- `generate_secret(max_value: int) -> int` lives in `src/number_guessing_game/game.py`. It validates `max_value >= 1` and returns `random.randint(1, max_value)` (easy to patch in tests).
	- `check_guess(secret: int, guess: int) -> Literal[-1,0,1]` compares values and returns the comparison code. Keeping this logic pure (no I/O) makes unit testing simple.

- **Data flow summary**:
	- `secret` (int) is created once by `generate_secret` at startup.
	- `user` (str) is read from stdin each loop iteration.
	- `guess` (int) is derived from `user` after parsing.
	- `result` (int) is produced by `check_guess(secret, guess)` and drives the printed response.

- **Error handling**:
	- Non-integer inputs and unexpected EOF are handled by catching `ValueError` and `EOFError`; the program prompts again instead of crashing.
	- `generate_secret` raises `ValueError` for invalid `max_value` (e.g., `0`) so callers can surface or test that behavior.

- **Attempts counting**:
	- `attempts` is incremented at the start of every loop iteration (current implementation counts invalid inputs as attempts). You can change this behavior so only valid numeric guesses increase the counter.

- **Testing**:
	- Unit tests in `tests/test_game.py` exercise `generate_secret` and `check_guess` directly. `random.randint` is patched during tests to make `generate_secret` deterministic.
	- Run tests locally with:

```powershell
pytest -q
```

- **CI**:
	- The GitHub Actions workflow in `.github/workflows/ci.yml` runs on pushes and pull requests to `main`.
	- It checks out the repo, sets up Python 3.11, installs `-r requirements.txt`, and runs `pytest -q`.

- **Development tips**:
	- To make debugging easier you can temporarily print the `secret` value after generation.
	- Consider adding `argparse` to `cli.py` so users can pass `--max` and `--seed` (for reproducible secrets) from the command line.
	- If you plan to expand types or use forward references in annotations, uncomment `from __future__ import annotations` in `cli.py` to postpone evaluation of annotations.
	- For a distributable package, add a `pyproject.toml` and a `console_scripts` entry point.

If you'd like, I can update `cli.py` to only count valid numeric guesses, add `argparse` options, or convert the project to an installable package. Tell me which change you prefer.
