
from prime_number_logic import is_prime


def test_prime() -> None:
    assert is_prime(9) == False
    assert is_prime(7) == True
    assert is_prime(13) == True
    assert is_prime(12908340918201) == False