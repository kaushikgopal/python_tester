"""Test for logic function in logic.py module"""

from logic import total

def test_total_empty() -> None:
    assert total([]) == 0.0
