"""
Unit tests for string_utils module.
"""

import unittest
import sys
import os

# Add parent directory to path to import string_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from string_utils import is_palindrome, count_word_frequency


class TestIsPalindrome(unittest.TestCase):
    """Test cases for the is_palindrome function."""
    
    def test_simple_palindrome(self):
        """Test simple palindromes."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("noon"))
    
    def test_single_character(self):
        """Test single character is a palindrome."""
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))
    
    def test_empty_string(self):
        """Test empty string is considered a palindrome."""
        self.assertTrue(is_palindrome(""))
    
    def test_palindrome_with_spaces(self):
        """Test palindromes with spaces."""
        self.assertTrue(is_palindrome("a man a plan a canal panama"))
        self.assertTrue(is_palindrome("race car"))
    
    def test_palindrome_mixed_case(self):
        """Test palindromes with mixed case."""
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("Level"))
        self.assertTrue(is_palindrome("A"))
    
    def test_not_palindrome(self):
        """Test strings that are not palindromes."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))
    
    def test_palindrome_numbers_as_string(self):
        """Test numeric palindromes as strings."""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("1001"))
        self.assertFalse(is_palindrome("12345"))
    
    def test_two_character_palindrome(self):
        """Test two character palindromes."""
        self.assertTrue(is_palindrome("aa"))
        self.assertFalse(is_palindrome("ab"))


class TestCountWordFrequency(unittest.TestCase):
    """Test cases for the count_word_frequency function."""
    
    def test_single_word(self):
        """Test counting a single word."""
        result = count_word_frequency("hello")
        self.assertEqual(result, {"hello": 1})
    
    def test_repeated_words(self):
        """Test counting repeated words."""
        result = count_word_frequency("hello hello hello")
        self.assertEqual(result, {"hello": 3})
    
    def test_multiple_different_words(self):
        """Test counting multiple different words."""
        result = count_word_frequency("hello world")
        self.assertEqual(result, {"hello": 1, "world": 1})
    
    def test_mixed_case(self):
        """Test that counting is case-insensitive."""
        result = count_word_frequency("Hello hello HELLO")
        self.assertEqual(result, {"hello": 3})
    
    def test_with_punctuation(self):
        """Test that punctuation is removed."""
        result = count_word_frequency("Hello, world! Hello.")
        self.assertEqual(result, {"hello": 2, "world": 1})
    
    def test_complex_sentence(self):
        """Test counting in a complex sentence."""
        text = "The quick brown fox jumps over the lazy dog. The dog was very lazy."
        result = count_word_frequency(text)
        self.assertEqual(result["the"], 3)
        self.assertEqual(result["dog"], 2)
        self.assertEqual(result["lazy"], 2)
        self.assertEqual(result["quick"], 1)
    
    def test_empty_string(self):
        """Test empty string returns empty dict."""
        result = count_word_frequency("")
        self.assertEqual(result, {})
    
    def test_only_punctuation(self):
        """Test string with only punctuation."""
        result = count_word_frequency("... !!! ???")
        self.assertEqual(result, {})
    
    def test_words_with_numbers(self):
        """Test words containing numbers."""
        result = count_word_frequency("test123 test123 hello")
        self.assertEqual(result, {"test123": 2, "hello": 1})
    
    def test_multiple_spaces(self):
        """Test handling of multiple spaces."""
        result = count_word_frequency("hello    world   hello")
        self.assertEqual(result, {"hello": 2, "world": 1})


if __name__ == "__main__":
    unittest.main()
