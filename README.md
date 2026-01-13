# Simple Python Utilities Project

A simple Python project demonstrating utility functions for mathematical and string operations.

## Project Structure

```
.
├── math_utils.py      # Mathematical utility functions
├── string_utils.py    # String manipulation utility functions
└── README.md          # This file
```

## Files and Functions

### math_utils.py

1. **calculate_factorial(n)** - Calculates the factorial of a non-negative integer
   - Takes an integer `n` as input
   - Returns the factorial of `n`
   - Raises `ValueError` for negative numbers

2. **find_prime_numbers(limit)** - Finds all prime numbers up to a given limit
   - Uses the Sieve of Eratosthenes algorithm
   - Takes an integer `limit` as input
   - Returns a list of all prime numbers up to the limit

### string_utils.py

1. **is_palindrome(text)** - Checks if a string is a palindrome
   - Takes a string `text` as input
   - Returns `True` if palindrome, `False` otherwise
   - Ignores spaces and case

2. **count_word_frequency(text)** - Counts word frequency in text
   - Takes a string `text` as input
   - Returns a dictionary with words and their frequencies
   - Handles basic punctuation removal

## Usage

You can run each file independently to see example outputs:

```bash
python math_utils.py
python string_utils.py
```

Or import the functions in your own code:

```python
from math_utils import calculate_factorial, find_prime_numbers
from string_utils import is_palindrome, count_word_frequency

# Calculate factorial
result = calculate_factorial(5)
print(f"5! = {result}")

# Find primes
primes = find_prime_numbers(50)
print(f"Primes up to 50: {primes}")

# Check palindrome
is_pal = is_palindrome("racecar")
print(f"Is 'racecar' a palindrome? {is_pal}")

# Count words
text = "hello world hello"
freq = count_word_frequency(text)
print(f"Word frequencies: {freq}")
```

## Requirements

- Python 3.6 or higher
- No external dependencies required
