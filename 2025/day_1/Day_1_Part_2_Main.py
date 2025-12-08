def read_input(input_file_name):
    with open (input_file_name) as file:
        lines = [x. strip() for x in file.readlines()]

    return lines

def process_dial_turns(dial_position, lines, zero_count):
    for line in lines:
        rotation = int(line[1:])
        direction = line[0]

        dial_started_at_zero = False
        if dial_position == 0:
            dial_started_at_zero = True

        if direction == "L":
            dial_position -= rotation
        else:
            dial_position += rotation

        while dial_position < 0 or dial_position > 99:
            if dial_position < 0:
                dial_position += 100

                if dial_started_at_zero == False:
                    zero_count += 1
                dial_started_at_zero = False

            if dial_position > 99:
                dial_position -= 100
                if dial_position != 0:
                    zero_count += 1

        if dial_position == 0:
             zero_count += 1

    return dial_position, zero_count
    # 5831 is the correct answer


if __name__ == "__main__":
    lines = read_input("Puzzle_Input")
    dial_position, zero_count = process_dial_turns(50, lines, 0)
    print(zero_count)
