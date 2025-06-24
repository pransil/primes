def is_prime(n):
    """
    Check if a number is prime using trial division algorithm.
    
    Args:
        n (int): Number to check for primality
        
    Returns:
        bool: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def find_primes(limit):
    """
    Generate a list of all prime numbers up to and including the given limit.
    
    Args:
        limit (int): Upper limit for prime number search
        
    Returns:
        list: List of prime numbers up to limit
    """
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def validate_input_boundary(number):
    """
    Validate that the input number is within acceptable bounds.
    
    Args:
        number (int): Number to validate
        
    Returns:
        bool: True if number is valid, False otherwise
    """
    return 0 <= number <= 10000


def get_user_number():
    """
    Get a valid number from the user with input validation.
    
    Returns:
        int: Valid number within bounds
    """
    while True:
        try:
            user_input = input("I will calculate prime numbers for you. How high should I go? ")
            number = int(user_input)
            
            if not validate_input_boundary(number):
                print(f"Error: Please enter a number between 0 and 10,000.")
                continue
                
            return number
            
        except ValueError:
            print("Error: Please enter a valid number.")
            continue


def get_continue_choice():
    """
    Ask user if they want to continue and validate Y/N response.
    
    Returns:
        bool: True if user wants to continue (Y/y), False otherwise
    """
    response = input("Do you want to calculate again? (Y/N) ")
    return response.lower() == 'y'


def format_output(primes, number):
    """
    Format the prime numbers output according to specifications.
    
    Args:
        primes (list): List of prime numbers
        number (int): The input number used for calculation
        
    Returns:
        str: Formatted output string
    """
    if not primes:
        return f"No prime numbers found up to {number}"
    else:
        return f"Prime numbers: {', '.join(map(str, primes))}"


def main():
    """
    Main application loop for the prime number calculator.
    """
    while True:
        # Get number from user
        number = get_user_number()
        
        # Calculate and display primes
        primes = find_primes(number)
        
        # Format and display output
        output = format_output(primes, number)
        print(output)
        
        # Ask if user wants to continue
        if not get_continue_choice():
            break


if __name__ == "__main__":
    main()