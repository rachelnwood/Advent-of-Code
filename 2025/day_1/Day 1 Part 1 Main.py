# input_file_name = "Sample Input"
input_file_name = "Puzzle_Input"

with open (input_file_name) as file:
    lines = [x. strip() for x in file.readlines()]


dial_position = 50
zero_count = 0

for line in lines:
    print(f'dial rotation:', line)
    rotation = int(line[1:])

    if line[0] == "L":
        dial_position -= rotation
    if line[0] == "R":
        dial_position += rotation

    dial_position = dial_position % 100
    print(dial_position)

    if dial_position == 0:
        zero_count += 1

print(f'There are', zero_count, 'zeros')

