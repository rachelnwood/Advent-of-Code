def read_input(input_file_name):
    with open (input_file_name) as file:
        lines = [x. strip() for x in file.readlines()]

    return lines

def build_list_of_ranges(ranges: list[str]) -> list[tuple[int, int]]:
    result = []

    for input_range in ranges:
        number_strings = input_range.split("-")
        start_number = int(number_strings[0])
        end_number = int(number_strings[1])

        result.append((start_number, end_number))

    return result

def fresh_ingredients_count(ingredients_list: list[str], ranges_list: list[tuple[int, int]]) -> int:
    fresh_ingredient_count = 0

    for string_id in ingredients_list:
        ingredient_id = int(string_id)
        for start, end in ranges_list:
            if start <= ingredient_id <= end:
                fresh_ingredient_count += 1
                break

    return fresh_ingredient_count

# main program
if __name__ == "__main__":
    ingredients = read_input("puzzle_input_IDs")
    fresh_ranges = read_input("puzzle_input_ranges")

    list_of_ranges = build_list_of_ranges(fresh_ranges)

    total = fresh_ingredients_count(ingredients, list_of_ranges)
    print(f"valid id count: {total}")