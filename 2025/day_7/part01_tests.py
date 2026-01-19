from day_7.part01_solution import *

def test_splitter_list():
    lines = [".......S.......", "...............", ".......^.......", "...............", "......^.^......", "...............", ".....^.^.^....."]
    y = 6 # index

    result = splitter_list(lines, y)
    assert(result == [5, 7, 9])

def test_beam_tracker():
    previous_beam_set = {6,8}
    splitter_locations = [6,8]

    beam_set = beam_tracker(splitter_locations, previous_beam_set)
    assert(beam_set == {5,7,9})


def test_beam_split_count_keeps_unsplit_beams():
    lines = [".......S.......",
    ".......|.......",
    "......|^|......",
    "......|.|......",
    ".....|^||......",
    ".....|.||......",
    "....|^||^|....."]

    answer = beam_split_count(lines)
    assert(answer == 4)

def test_final_boss():
    lines = [".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "..............."]

    answer = beam_split_count(lines)
    assert(answer == 21)
