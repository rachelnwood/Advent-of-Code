from day_4.part_1 import char_at_xy
from day_4.part_1 import adjacent_paper_rolls
from day_4.part_1 import count_accessible_paper_rolls

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


def test_accessible_paper_rolls():
    map = ["..@@.@@@@.", # 5 here
           "@@@.@.@.@@", # 1 here
           "@@@@@.@.@@"] # ????

    assert(count_accessible_paper_rolls(map) == 11)