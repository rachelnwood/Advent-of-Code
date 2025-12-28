from day_5.part_2 import sort_ranges
from day_5.part_2 import merge_ranges
from day_5.part_2 import len_of_ranges

def test_sort_ingredient_ranges():
    ranges = [(10, 14), (3, 5)]
    sort_ranges(ranges)

    assert(ranges == [(3, 5), (10, 14)])

def test_merge_ranges():
    ranges = [(3, 5), (10, 17), (16, 20), (17, 23)]
    merged_ranges = merge_ranges(ranges)

    assert(merged_ranges == [(3,5), (10,23)])


def test_len_of_ranges():
    ranges = [(3, 5), (10, 20)]
    result = len_of_ranges(ranges)

    assert(result == 14)