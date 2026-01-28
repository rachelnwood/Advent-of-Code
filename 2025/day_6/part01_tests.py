from day_6.part01_solution import *

def test_part_1_do_math():
    lines = [[123, 328, 51, 64], [45, 64, 387, 23], [6, 98, 215, 314], ['*', '+', '*', '+']]
    result = do_math(lines)
    assert(result == 4277556)
