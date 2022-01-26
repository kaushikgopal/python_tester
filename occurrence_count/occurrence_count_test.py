"""Test for logic function in logic.py module"""

from occurrence_count.occurrence_count_logic import occurrence_count


def test_occurrence_count() -> None:
    assert occurrence_count(300, 0) == 2