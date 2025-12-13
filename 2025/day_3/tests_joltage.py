from day_3.part_1 import greatest_two_numbers

def test_one():
    bank = '987'
    answer = greatest_two_numbers(bank)
    assert answer == 98

def test_two():
    bank = '8193'
    answer = greatest_two_numbers(bank)
    assert answer == 93

def test_three():
    bank = '1119'
    answer = greatest_two_numbers(bank)
    assert answer == 19





