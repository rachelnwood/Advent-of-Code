def read_input(input_file_name) -> list[str]:
    with (open (input_file_name) as file):
        ranges = file.readline().split(",")
        return ranges

def valid_id(id: int) -> bool:
    number_as_string = str(id)
    length = len(number_as_string)
    components_set = set()

    for digit_count in range(1, (length//2)+1):

        if (length % digit_count) != 0:
            continue

        for char_index in range(0, length//digit_count):
            computed_index = char_index * digit_count
            new_string = number_as_string[computed_index: computed_index + digit_count]

            components_set.add(new_string)

        if len(components_set) == 1:
            return False

        components_set.clear()

    return True

def main_function(ranges: list[str]) -> int:
    total = 0

    for item in ranges:
        numbers = item.split("-")
        starting_number, ending_number = int(numbers[0]), int(numbers[1])

        for id_to_check in range(starting_number, ending_number+1):
            if not valid_id(id_to_check):
                total += id_to_check

    return total

if __name__ == "__main__":
    ranges = read_input("puzzle_input")
    result = main_function(ranges)
    print(f"The sum of the invalid ids is {result}")