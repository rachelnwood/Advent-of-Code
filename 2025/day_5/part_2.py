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

def sort_ranges(list_of_ranges: list[tuple[int, int]]):
    list_of_ranges.sort()

def merge_ranges(sorted_ranges_list: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged_ranges = []
    current_start, current_end = sorted_ranges_list[0]

    for next_start, next_end in sorted_ranges_list[1:]:
        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = next_start, next_end

    merged_ranges.append((current_start, current_end))

    return merged_ranges

def len_of_ranges(merged_ranges: list[tuple[int, int]]) -> int:
    fresh_ingredient_IDs = 0

    for start, end in merged_ranges:
        range_length = len(range(start,end+1))
        fresh_ingredient_IDs += range_length

    return fresh_ingredient_IDs


# main program
if __name__ == "__main__":
    fresh_ranges = read_input("puzzle_input_ranges")

    list_of_ranges = build_list_of_ranges(fresh_ranges)
    sort_ranges(list_of_ranges)
    merged_ranges = merge_ranges(list_of_ranges)


    total = len_of_ranges(merged_ranges)
    print(f"Total fresh ingredient id count: {total}")