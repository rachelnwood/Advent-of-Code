from day_6.part_2 import *

def test_part_input_sample():
    input_list = ["123 328  51 64", " 45 64  387 23", "  6 98  215 314", "*   +   *   +"]

    result = read_input("sample_input")
    assert(result == input_list)

def test_starting_columns():
    input_list = ["123 328  51 64", " 45 64  387 23", "  6 98  215 314", "*   +   *   +"]

    result = find_starting_columns(input_list)
    assert(result == [0,4,8,12])

def test_lines_to_cephalopod_numbers_left_end():
    input_list = ["123 328  51 64", " 45 64  387 23", "  6 98  215 314", "*   +   *   +"]
    col_start = 0
    col_end = 2

    result = lines_to_cephalopod_numbers(input_list, col_start, col_end)
    assert(result == [1, 24, 356])

def test_lines_to_cephalopod_numbers_right_end():
    input_list = ["123 328  51 64", " 45 64  387 23", "  6 98  215 314", "*   +   *   +"]
    col_start = 12
    col_end = 14

    result = lines_to_cephalopod_numbers(input_list, col_start, col_end)
    assert(result == [623, 431, 4])

def test_find_last_column_index():
    input_list = ["123 328  51 64", " 45 64  387 23", "  6 98  215 314", "*   +   *   +"]

    result = find_last_column_index(input_list)
    assert(result == 16) # 16 is where the next column would begin

def test_do_all_the_little_problems():
    input_list = ["123 328  51 64", " 45 64  387 23", "  6 98  215 314", "*   +   *   +"]
    result = do_all_the_little_problems(input_list)
    assert(result == 3263827)






# def test_process_string_list_to_int():
#     input_list = [["123",  "328", "51", "64"], ["45", "64", "387", "23"], ["6", "98", "215", "314"], ["*", "+", "*", "+"]]
#     result = process_string_list_to_int(input_list)
#     assert(result==[[4, 431, 623], [175, 581, 32], [8, 248, 369], [356, 24, 1]])


# def test_part_do_math():
#     input_list = [["123",  "328", "51", "64"], ["45", "64", "387", "23"], ["6", "98", "215", "314"], ["*", "+", "*", "+"]]
#     result = do_math(input_list)
#     assert(result == 3263827)
