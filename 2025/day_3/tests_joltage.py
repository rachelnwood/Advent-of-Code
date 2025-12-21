from day_3.part_1 import greatest_two_numbers

from day_3.part_2 import greatest_twelve_numbers


# Part 1 tests

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

# Part 2 tests

def test_one_twelve_numbers():
    bank = '987654321111111'
    answer = greatest_twelve_numbers(bank)
    assert answer == 987654321111

def test_two_twelve_numbers():
    bank = '811111111111119'
    answer = greatest_twelve_numbers(bank)
    assert answer == 811111111119

def test_three_twelve_numbers():
    bank = '234234234234278'
    answer = greatest_twelve_numbers(bank)
    assert answer == 434234234278

def test_four_twelve_numbers():
    bank = '818181911112111'
    answer = greatest_twelve_numbers(bank)
    assert answer == 888911112111
