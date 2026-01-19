from day_7.part02_solution import *
from part02_solution import BeamMap

def test_first_splitter():
    lines = [".......S.......",
             "...............",
             ".......^......."]
    map = BeamMap.from_lines(lines)
    answer = map.first_splitter()
    assert(answer == 7)

def test_beam_map_from_lines():
    lines = [".......S.......",
             "...............",
             ".......^......."]
    map = BeamMap.from_lines(lines)

    assert(map.char_at_x_y(7,0) == "S")
    assert(map.char_at_x_y(7,2) == "^")

def test_beam_map_from_file_name():
    map = BeamMap("sample_input")

    assert (map.char_at_x_y(7, 0) == "S")
    assert (map.char_at_x_y(7, 2) == "^")

def test_bottom_map_index():
    map = BeamMap("sample_input")

    assert(map.bottom_map_index() == 15)

def test_recursive_beams():
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
    map = BeamMap.from_lines(lines)

    answer = recursive_beams(map, 7, 1)
    assert(answer == 40)
