"""
Unit tests for math_utils module.
"""

import unittest
import sys
import os

# Add parent directory to path to import math_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from math_utils import calculate_factorial, find_prime_numbers


class TestCalculateFactorial(unittest.TestCase):
    """Test cases for the calculate_factorial function."""
    
    def test_factorial_zero(self):
        """Test factorial of 0 should return 1."""
        self.assertEqual(calculate_factorial(0), 1)
    
    def test_factorial_one(self):
        """Test factorial of 1 should return 1."""
        self.assertEqual(calculate_factorial(1), 1)
    
    def test_factorial_small_numbers(self):
        """Test factorial of small positive numbers."""
        self.assertEqual(calculate_factorial(2), 2)
        self.assertEqual(calculate_factorial(3), 6)
        self.assertEqual(calculate_factorial(4), 24)
        self.assertEqual(calculate_factorial(5), 120)
    
    def test_factorial_larger_number(self):
        """Test factorial of a larger number."""
        self.assertEqual(calculate_factorial(10), 3628800)
    
    def test_factorial_negative_number(self):
        """Test that negative numbers raise ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate_factorial(-1)
        self.assertIn("negative", str(context.exception).lower())
    
    def test_factorial_negative_large(self):
        """Test that large negative numbers raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_factorial(-10)


class TestFindPrimeNumbers(unittest.TestCase):
    """Test cases for the find_prime_numbers function."""
    
    def test_primes_below_two(self):
        """Test that numbers below 2 return empty list."""
        self.assertEqual(find_prime_numbers(0), [])
        self.assertEqual(find_prime_numbers(1), [])
        self.assertEqual(find_prime_numbers(-5), [])
    
    def test_primes_up_to_two(self):
        """Test primes up to 2."""
        self.assertEqual(find_prime_numbers(2), [2])
    
    def test_primes_up_to_ten(self):
        """Test primes up to 10."""
        expected = [2, 3, 5, 7]
        self.assertEqual(find_prime_numbers(10), expected)
    
    def test_primes_up_to_twenty(self):
        """Test primes up to 20."""
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(find_prime_numbers(20), expected)
    
    def test_primes_up_to_thirty(self):
        """Test primes up to 30."""
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(find_prime_numbers(30), expected)
    
    def test_primes_up_to_fifty(self):
        """Test primes up to 50."""
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(find_prime_numbers(50), expected)
    
    def test_primes_count(self):
        """Test that we get the correct count of primes."""
        primes = find_prime_numbers(100)
        self.assertEqual(len(primes), 25)  # There are 25 primes up to 100
    
    def test_all_returned_are_prime(self):
        """Test that all returned numbers are actually prime."""
        primes = find_prime_numbers(30)
        for p in primes:
            # Check that p is only divisible by 1 and itself
            if p > 1:
                for i in range(2, int(p ** 0.5) + 1):
                    self.assertNotEqual(p % i, 0, f"{p} should be prime but is divisible by {i}")


if __name__ == "__main__":
    unittest.main()
