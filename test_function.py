from functions import is_prime, get_primes

def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(5) is True
    assert is_prime(10) is False

def test_get_primes():
    assert get_primes(6, 10) == [7]

