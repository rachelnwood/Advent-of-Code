from day_2.part2_solution import *

def test_for_reading_sample_file():
    assert(read_input("sample_input") == ['11-22', '95-115', '998-1012', '1188511880-1188511890', '222220-222224', '1698522-1698528', '446443-446449', '38593856-38593862', '565653-565659', '824824821-824824827', '2121212118-2121212124'])

def test_for_valid_id():
    assert(valid_id(12) == True)
    assert(valid_id(95) == True)
    assert(valid_id(3334) == True)
    assert(valid_id(3593591) == True)
    assert(valid_id(1188511890) == True)

def test_for_invalid_id():
    assert(valid_id(11) == False)
    assert(valid_id(22) == False)
    assert(valid_id(99) == False)
    assert (valid_id(333) == False)
    assert (valid_id(999) == False)
    assert (valid_id(1010) == False)
    assert (valid_id(3434) == False)
    assert (valid_id(22222) == False)
    assert (valid_id(446446) == False)
    assert (valid_id(565656) == False)
    assert (valid_id(38593859) == False)
    assert (valid_id(824824824) == False)
    assert(valid_id(1188511885) == False)
    assert(valid_id(2121212121) == False)

def test_main_function():
    ranges = ['11-22', '95-115', '998-1012', '1188511880-1188511890', '222220-222224', '1698522-1698528', '446443-446449', '38593856-38593862', '565653-565659', '824824821-824824827', '2121212118-2121212124']
    assert(main_function(ranges) == 4174379265)