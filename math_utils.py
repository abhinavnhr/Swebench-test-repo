"""
Math utility functions for common mathematical operations.
"""


def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def find_prime_numbers(limit):
    """
    Find all prime numbers up to a given limit using the Sieve of Eratosthenes.
    
    Args:
        limit (int): The upper limit to find primes (inclusive)
        
    Returns:
        list: A list of all prime numbers up to the limit
    """
    if limit < 2:
        return []
    
    # Create a boolean array and initialize all entries as true
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    
    # Collect all numbers that are still marked as prime
    primes = [num for num in range(limit + 1) if is_prime[num]]
    
    return primes


if __name__ == "__main__":
    # Example usage
    print("Factorial of 5:", calculate_factorial(5))
    print("Prime numbers up to 30:", find_prime_numbers(30))
