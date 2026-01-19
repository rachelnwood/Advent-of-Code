def read_input(input_file_name):
    with open (input_file_name) as file:
        lines = [x. strip() for x in file.readlines()]

        return lines

def splitter_list(lines: list[str], y: int) -> list[int]:
    line = lines[y]
    all_splitters = [index for index, char in enumerate(line) if char == "^"]

    return all_splitters

def beam_tracker(splitter_locations: list[int], previous_beam_set: set[int]) -> set[int]:
    result = set()
    for x in splitter_locations:
        if x in previous_beam_set:
            result.add(x-1)
            result.add(x+1)

    return result

def beam_split_count(lines: list[str]) -> int:
    total = 0
    beam_tracker_above = set(index for index, char in enumerate(lines[0]) if char == "S")

    for y in range(2, len(lines), 2): # skipping every other line
        splitter_locations = splitter_list(lines, y)

        for x in splitter_locations:
            if x in beam_tracker_above:
                total += 1

        beam_tracker_current_row = beam_tracker(splitter_locations, beam_tracker_above)

        for x in beam_tracker_above:
            if x not in splitter_locations:
                beam_tracker_current_row.add(x)

        beam_tracker_above = beam_tracker_current_row

    return total

# main program
if __name__ == "__main__":
    lines = read_input("puzzle_input")
    result = beam_split_count(lines)
    print(f"The beam split {result} times")