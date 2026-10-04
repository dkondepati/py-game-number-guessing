# PY Game Number Guessing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.7+](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/webkolog/py-game-number-guessing/actions/workflows/python-tests.yml/badge.svg)](https://github.com/webkolog/py-game-number-guessing/actions)

**Version:** 1.0

**Created Date:** 2026-07-24

**Last Updated:** 2026-07-24

**Compatibility:** Python 3.x

**Created By:** Ali Candan ([@webkolog](https://github.com/webkolog))

**Website:** [http://webkolog.net](http://webkolog.net)

**Copyright:** (c) 2026 Ali Candan

**License:** MIT License ([http://mit-license.org](http://mit-license.org))

---

**PY Game Number Guessing** is a lightweight, terminal-based number guessing game written in Python. Unlike standard guessing games, it features a progressive difficulty system where the number range expands and your maximum allowed attempts increase as you successfully clear each level.

## Features
- **Dynamic Scaling:** The secret number range increases by 10 with every level (Level 1: 1-10, Level 2: 1-20, etc.).
- **Progressive Attempts:** Clearing a level rewards you by adding 1 extra attempt to your maximum pool for the next stage.
- **Input Validation:** Built-in error handling prevents the game from crashing if a user accidentally types a non-integer value.
- **Zero Dependencies:** Runs natively using Python's standard library.

## Installation
To run this game locally, ensure you have Python 3 installed. Clone the repository or download the source file directly:

```bash
git clone https://github.com/webkolog/py-game-number-guessing.git
cd py-game-number-guessing

```

## Usage

Simply execute the Python script from your terminal:

```bash
python py-game-number-guessing.py

```

## How It Works

### Game Mechanics

* **Level 1 Mechanics:** You must guess a number between **1 and 10** within **5 attempts**.
* **Level Scaling Formula:**
* `Upper Limit = Level * 10`
* `Max Attempts = 5 + (Level - 1)`



### High-Level Flow Chart

1. The game initializes at **Level 1** with **5 attempts**.
2. A random secret number is generated within the level's boundary.
3. The user inputs a guess:
* If the guess is correct, the level is cleared, rewards are applied, and the next level begins.
* If the guess is wrong, the game gives a hint ("Too low!" or "Too high!") and consumes an attempt.


4. If the user runs out of attempts before guessing correctly, it is **Game Over**.

## Example Gameplay

```text
Welcome to the Number Guessing Game!

--- Level 1 ---
Guess a number between 1 and 10.
You have 5 attempts.
Attempt 1/5: 5
Too low!
Attempt 2/5: 8
Too high!
Attempt 3/5: 7
Congratulations! You guessed it right!
Level cleared! Moving to level 2...

--- Level 2 ---
Guess a number between 1 and 20.
You have 6 attempts.
Attempt 1/6: 

```

## Error Handling

The script handles non-integer entries gracefully using a `try-except` block targeting `ValueError`. If an invalid character is entered, the application prompts the user without wasting an explicit game attempt.

```python
try:
    guess = int(input(f"Attempt {attempts + 1}/{max_guesses}: "))
except ValueError:
    print("Please enter a valid number.")
    continue

```

## License

This project is open-source software licensed under the [MIT license](https://mit-license.org/).

```text
MIT License

Copyright (c) 2026 Ali Candan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

## Contributing

Contributions are welcome! If you find any bugs, want to add features (like a high-score tracking system or GUI implementation), please feel free to open an issue or submit a pull request on the GitHub repository.

## Support

For any questions, bug reports, or feedback regarding the game, you can refer to the project's GitHub repository issues page or contact the author directly via [Webkolog](http://webkolog.net).
