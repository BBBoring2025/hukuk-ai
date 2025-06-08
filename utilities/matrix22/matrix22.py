"""Matrix22 Numerology Utility

This script calculates a simple numerology value based on the Matrix22 method.
Each letter is converted to a number between 1 and 22. Digits are counted as
is. The final sum is reduced modulo 22 with 22 replacing 0.
"""

import argparse
from typing import Iterable


def numerology(text: str) -> int:
    """Return the Matrix22 numerology value for the given text."""
    total = 0
    for char in text:
        if char.isdigit():
            total += int(char)
        elif char.isalpha():
            total += (ord(char.upper()) - ord('A')) % 22 + 1
    value = total % 22
    return value if value != 0 else 22


def main(argv: Iterable[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Matrix22 numerology tool")
    parser.add_argument("text", help="Text to evaluate")
    args = parser.parse_args(argv)
    result = numerology(args.text)
    print(result)


if __name__ == "__main__":
    main()
