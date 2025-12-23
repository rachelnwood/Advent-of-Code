from day_4.part_2 import *


def test_char_at_XY():
    map = ["..@@.@@@@.",
           "@@@.@.@.@@",
           "@@@@@.@.@@"]

    assert(char_at_xy(0, 0, map) == ".")
    assert(char_at_xy(6, 2, map) == "@")
    assert(char_at_xy(0, 1000, map) is None)
    assert(char_at_xy(-100, 0, map) is None)

def test_surrounding_8_spaces():
    map = ["..@@.@@@@.",
           "@@@.@.@.@@",
           "@@@@@.@.@@"]

    assert(adjacent_paper_rolls(2, 0, map) == 3)
    assert(adjacent_paper_rolls(0, 1, map) == 3)
    assert(adjacent_paper_rolls(6, 2, map) == 1)
    assert(adjacent_paper_rolls(9, 1, map) == 4)

def test_list_accessible_paper_rolls():
    map = ["..@@.@@@@.",
           "@@@.@.@.@@",
           "@@@@@.@.@@"]

    assert(list_accessible_paper_rolls(map) == [(2,0), (3,0), (5,0), (6,0), (8,0), (0,1), (0,2), (4,2), (6,2), (8,2), (9,2)])

def test_copy_map():
    map = ["..@@.@@@@.",
           "@@@.@.@.@@",
           "@@@@@.@.@@"]

    second_map = copy_map(map)
    assert(second_map == map)

    second_map[0] = 'X' + second_map[0][1:]
    assert(second_map != map)

def test_replace_paper_rolls():
    map = ["..@@.@@@@.",
           "@@@.@.@.@@",
           "@@@@@.@.@@"]

    removal_list = [(2, 0), (3, 0), (5, 0), (6, 0), (8, 0), (0, 1), (0, 2), (4, 2), (6, 2), (8, 2), (9, 2)]
    replace_paper_rolls(map, removal_list)


    assert(map == ['..xx.xx@x.', 'x@@.@.@.@@', 'x@@@x.x.xx'])

def test_main_function():
    map = ["..@@.@@@@.",
           "@@@.@.@.@@",
           "@@@@@.@.@@"]
    removal_list = [(2, 0), (3, 0), (5, 0), (6, 0), (8, 0), (0, 1), (0, 2), (4, 2), (6, 2), (8, 2), (9, 2)]

    assert(removed_paper_rolls_number(map) == 21)