"""
String utility functions for common string operations.
"""


def is_palindrome(text):
    """
    Check if a given string is a palindrome (reads the same forwards and backwards).
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for comparison
    cleaned_text = text.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]


def count_word_frequency(text):
    """
    Count the frequency of each word in a given text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: A dictionary with words as keys and their frequencies as values
    """
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Remove common punctuation from words
    puntuation = ".!?;:\""
    cleaned_words = []
    for word in words:
        cleaned_word = word.strip(punctuation)
        if cleaned_word:  # Only add non-empty words
            cleaned_words.append(cleaned_word)
    
    # Count word frequencies
    word_freq = {}
    for word in cleaned_words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    return word_freq


if __name__ == "__main__":
    # Example usage
    print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
    print("Is 'A man a plan a canal Panama' a palindrome?", is_palindrome("A man a plan a canal Panama"))
    
    sample_text = "Hello world! Hello everyone. This is a test text."
    print("\nWord frequencies in sample text:")
    print(count_word_frequency(sample_text))
