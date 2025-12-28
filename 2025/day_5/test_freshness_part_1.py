from day_5.part_1 import build_list_of_ranges
from day_5.part_1 import fresh_ingredients_count

def test_freshness_range_set_builder():
    ranges = ["3-5", "9-11"]
    result = build_list_of_ranges(ranges)

    assert(result == [(3, 5), (9, 11)])

def test_fresh_ingredients_count():
    ranges = [(3, 5), (9, 11)]
    ingredients = ["5", "11", "12"]
    fresh_count = fresh_ingredients_count(ingredients, ranges)

    assert(fresh_count == 2)
