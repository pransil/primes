import pytest
from primes import is_prime, find_primes, validate_input_boundary, format_output


class TestIsPrime:
    """Test cases for the is_prime function."""
    
    def test_is_prime_less_than_2(self):
        """Test that numbers less than 2 are not prime."""
        assert is_prime(0) == False
        assert is_prime(1) == False
        assert is_prime(-1) == False
        assert is_prime(-10) == False
    
    def test_is_prime_2(self):
        """Test that 2 is prime."""
        assert is_prime(2) == True
    
    def test_is_prime_small_primes(self):
        """Test small prime numbers."""
        assert is_prime(3) == True
        assert is_prime(5) == True
        assert is_prime(7) == True
        assert is_prime(11) == True
        assert is_prime(13) == True
    
    def test_is_prime_small_composites(self):
        """Test small composite numbers."""
        assert is_prime(4) == False
        assert is_prime(6) == False
        assert is_prime(8) == False
        assert is_prime(9) == False
        assert is_prime(10) == False
        assert is_prime(12) == False
    
    def test_is_prime_larger_primes(self):
        """Test larger prime numbers."""
        assert is_prime(17) == True
        assert is_prime(19) == True
        assert is_prime(23) == True
        assert is_prime(97) == True
    
    def test_is_prime_larger_composites(self):
        """Test larger composite numbers."""
        assert is_prime(15) == False
        assert is_prime(21) == False
        assert is_prime(25) == False
        assert is_prime(100) == False


class TestFindPrimes:
    """Test cases for the find_primes function."""
    
    def test_find_primes_edge_case_0(self):
        """Test find_primes with input 0."""
        result = find_primes(0)
        assert result == []
    
    def test_find_primes_edge_case_1(self):
        """Test find_primes with input 1."""
        result = find_primes(1)
        assert result == []
    
    def test_find_primes_edge_case_2(self):
        """Test find_primes with input 2."""
        result = find_primes(2)
        assert result == [2]
    
    def test_find_primes_10(self):
        """Test find_primes with input 10."""
        result = find_primes(10)
        expected = [2, 3, 5, 7]
        assert result == expected
    
    def test_find_primes_100(self):
        """Test find_primes with input 100."""
        result = find_primes(100)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        assert result == expected
        assert len(result) == 25  # There are 25 primes up to 100


class TestValidateInputBoundary:
    """Test cases for the validate_input_boundary function."""
    
    def test_validate_input_boundary_valid_numbers(self):
        """Test valid numbers within boundary."""
        assert validate_input_boundary(0) == True
        assert validate_input_boundary(1) == True
        assert validate_input_boundary(100) == True
        assert validate_input_boundary(5000) == True
        assert validate_input_boundary(10000) == True
    
    def test_validate_input_boundary_invalid_negative(self):
        """Test negative numbers are invalid."""
        assert validate_input_boundary(-1) == False
        assert validate_input_boundary(-10) == False
        assert validate_input_boundary(-1000) == False
    
    def test_validate_input_boundary_invalid_too_large(self):
        """Test numbers above 10,000 are invalid."""
        assert validate_input_boundary(10001) == False
        assert validate_input_boundary(20000) == False
        assert validate_input_boundary(100000) == False


class TestFormatOutput:
    """Integration tests for expected output formats."""
    
    def test_format_output_no_primes_0(self):
        """Test output format for input 0 (no primes)."""
        primes = find_primes(0)
        output = format_output(primes, 0)
        assert output == "No prime numbers found up to 0"
    
    def test_format_output_no_primes_1(self):
        """Test output format for input 1 (no primes)."""
        primes = find_primes(1)
        output = format_output(primes, 1)
        assert output == "No prime numbers found up to 1"
    
    def test_format_output_single_prime_2(self):
        """Test output format for input 2 (single prime)."""
        primes = find_primes(2)
        output = format_output(primes, 2)
        assert output == "Prime numbers: 2"
    
    def test_format_output_multiple_primes_10(self):
        """Test output format for input 10 (multiple primes)."""
        primes = find_primes(10)
        output = format_output(primes, 10)
        assert output == "Prime numbers: 2, 3, 5, 7"
    
    def test_format_output_multiple_primes_20(self):
        """Test output format for input 20 (multiple primes)."""
        primes = find_primes(20)
        output = format_output(primes, 20)
        assert output == "Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19"