def read_input(input_file_name):
    with open (input_file_name) as file:
        lines = [x.strip('\n') for x in file.readlines()]
        return lines

def find_starting_columns(lines: list[str]) -> list[int]:
    line_of_operators = lines[len(lines)-1]
    result = []

    for x, char in enumerate(line_of_operators):
        if char == "*" or char == "+":
            result.append(x)

    return result

def lines_to_cephalopod_numbers(lines, col_start, col_end):
    result = []

    for x in range(col_start, col_end+1):
        string_of_a_number = ""

        for y in range(len(lines)-1):
            char = char_at_X_Y(x, y, lines)
            if char == " ":
                continue

            string_of_a_number += char

        number = int(string_of_a_number)
        result.append(number)

    return result

def find_last_column_index(lines: list[str]) -> int:
    result = 0

    for line in lines:
        length = len(line)
        result = max(length, result)

    return result-1+2 # add two to get to where the "next" column would be.

def do_all_the_little_problems(lines: list[str]) -> int:
    total = 0
    starting_columns = find_starting_columns(lines)

    last_column_index = find_last_column_index(lines)
    starting_columns.append(last_column_index)

    for index in range(len(starting_columns)-1):
        col_start = starting_columns[index]
        col_end = starting_columns[index+1]-2
        numbers = lines_to_cephalopod_numbers(lines, col_start, col_end)

        y = len(lines)-1
        operator = char_at_X_Y(col_start, y, lines)

        if operator == "*":
            problem_total = 1
            for number in numbers:
                problem_total *= number

            total += problem_total
        else:
            problem_total = sum(numbers)
            total += problem_total

    return total

def char_at_X_Y(x: int, y: int, map: list[list[str]]) -> str:
    if x < 0 or x >= len(map[y]):
        return " "

    return map[y][x]

# main program
if __name__ == '__main__':
    lines = read_input('puzzle_input')
    total_number = do_all_the_little_problems(lines)
    print(f"The total number is {total_number}")