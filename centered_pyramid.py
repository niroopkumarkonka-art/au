#!/usr/bin/env python3
"""
centered_pyramid.py

Prints a centered number pyramid for n rows.

Example (n=5):
    1
   121
  12321
 1234321
123454321
Usage:
    python centered_pyramid.py 5

The script exposes a function `build_centered_pyramid(n)` that returns a list of strings
(one per row) which makes unit testing easy.
"""
import sys
from typing import List


def build_centered_pyramid(n: int) -> List[str]:
    """Return a list of strings representing a centered number pyramid with n rows.

    Each row i (1-based) contains increasing numbers from 1 to i and then decreasing
    numbers back to 1, centered with spaces so the last row has no leading spaces.
    """
    if n <= 0:
        return []
    # width of the last row: numbers count = 2*n-1, but each number is printed without spaces
    # we just use leading spaces to center; compute leading spaces for row i as n-i
    lines: List[str] = []
    for i in range(1, n + 1):
        left_nums = ''.join(str(k) for k in range(1, i + 1))
        right_nums = ''.join(str(k) for k in range(i - 1, 0, -1))
        line = left_nums + right_nums
        # center by padding on the left with (n - i) spaces
        padded = ' ' * (n - i) + line
        lines.append(padded)
    return lines


def print_centered_pyramid(n: int) -> None:
    for row in build_centered_pyramid(n):
        print(row)


def _cli(argv: List[str]) -> int:
    if len(argv) < 2:
        print("Usage: python centered_pyramid.py N")
        return 1
    try:
        n = int(argv[1])
    except ValueError:
        print("N must be an integer")
        return 2
    print_centered_pyramid(n)
    return 0


if __name__ == '__main__':
    raise SystemExit(_cli(sys.argv))
