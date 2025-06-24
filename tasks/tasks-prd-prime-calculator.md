## Relevant Files

- `primes.py` - Main application file containing all functionality for the prime calculator
- `test_primes.py` - Unit tests for the prime calculator functionality

### Notes

- Unit tests should be placed alongside the main code file
- Use `python -m pytest test_primes.py` to run tests
- Use `python primes.py` to run the application

## Tasks

- [x] 1.0 Create core prime calculation functionality
  - [x] 1.1 Implement is_prime() function using trial division algorithm
  - [x] 1.2 Implement find_primes() function to generate list of primes up to given limit
  - [x] 1.3 Add input boundary validation (upper limit of 10,000)
- [x] 2.0 Implement user input validation and error handling
  - [x] 2.1 Create get_user_number() function with try/except for numeric validation
  - [x] 2.2 Add error message display and re-prompting for invalid input
  - [x] 2.3 Implement get_continue_choice() function for Y/N validation
- [x] 3.0 Build interactive user interface and main application loop
  - [x] 3.1 Create main() function with primary application loop
  - [x] 3.2 Implement initial user prompt: "I will calculate prime numbers for you. How high should I go?"
  - [x] 3.3 Add continuation prompt: "Do you want to calculate again? (Y/N)"
  - [x] 3.4 Handle program termination logic
- [x] 4.0 Add output formatting and edge case handling
  - [x] 4.1 Implement format_output() function for "Prime numbers: x, y, z" format
  - [x] 4.2 Add special case handling for inputs 0 and 1 (no primes message)
  - [x] 4.3 Add special case handling for input 2 (single prime result)
- [x] 5.0 Create comprehensive unit tests and validation
  - [x] 5.1 Write tests for is_prime() function with various inputs
  - [x] 5.2 Write tests for find_primes() function with edge cases (0, 1, 2, 10, 100)
  - [x] 5.3 Write tests for input validation functions
  - [x] 5.4 Write integration tests for expected output formats