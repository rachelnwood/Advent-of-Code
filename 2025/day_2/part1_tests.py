from day_2.part1_solution import *

def test_valid_id():
    assert(valid_id(11) == False)
    assert(valid_id(12) == True)
    assert(valid_id(111) == True)
    assert(valid_id(1212) == False)

def test_for_reading_sample_file():
    assert(read_input("sample_input") == ['11-22', '95-115', '998-1012', '1188511880-1188511890', '222220-222224', '1698522-1698528', '446443-446449', '38593856-38593862', '565653-565659', '824824821-824824827', '2121212118-2121212124'])

def test_main_function():
    ranges = ['11-22', '95-115', '998-1012', '1188511880-1188511890', '222220-222224', '1698522-1698528', '446443-446449', '38593856-38593862', '565653-565659', '824824821-824824827', '2121212118-2121212124']
    assert(main_function(ranges) == 1227775554)

