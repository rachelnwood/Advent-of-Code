def read_input(input_file_name):
    result = []

    with open(input_file_name) as file:
        for line in file:
            tokens = line.split()
            if not tokens:
                continue

            # numeric line
            if all(token.lstrip("-").isdigit() for token in tokens):
                result.append([int(token) for token in tokens])
            else:
                # operator / symbol line
                result.append(tokens)

    return result

def do_math(lines: list[list]) -> int:
    row_count = len(lines)
    overall_total = 0

    for column_index in range(len(lines[0])):
        is_adding = lines[row_count-1][column_index] == '+'
        column_total = 0 if is_adding else 1

        for row_index in range(row_count-1):
            if is_adding:
                column_total += lines[row_index][column_index]
            else:
                column_total *= lines[row_index][column_index]

        overall_total += column_total

    return overall_total

# main program
if __name__ == '__main__':
    lines = read_input("sample_input")
    total = do_math(lines)
    print(total)