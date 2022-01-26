"""Test for logic function in logic.py module"""


from leetcode_even_digit_count.leetcode_even_digit_count_logic import event_digit_count

def test_event_digit_count() -> None:
    arr = [12, 345, 2, 7896]
    assert event_digit_count(arr) == 2