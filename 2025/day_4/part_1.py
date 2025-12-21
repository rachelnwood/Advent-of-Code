def read_input(input_file_name):
    with open (input_file_name) as file:
        lines = [x. strip() for x in file.readlines()]

    return lines

def char_at_xy(x: int, y: int, map: list[str]) -> str | None:
    if x < 0 or y < 0:
        return None
    if x >= len(map[0]):
        return None
    if y >= len(map):
        return None

    return map[y][x]


def adjacent_paper_rolls(x: int, y: int, map: list[str]) -> int:
    adjacent_count = 0

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:  # Skip the center cell
                continue
            if char_at_xy(x + dx, y + dy, map) == "@":
                adjacent_count += 1

    return adjacent_count

def count_accessible_paper_rolls(map: list[str]) -> int:
    paper_roll_total = 0

    for y in range(len(map)):
        for x in range(len(map[0])):
            if char_at_xy(x, y, map) == '@':
                neighbor_count = adjacent_paper_rolls(x, y, map)
                if neighbor_count < 4:
                    paper_roll_total += 1

    return paper_roll_total


# main program
if __name__ == "__main__":
    lines = read_input("puzzle_input")
    total = count_accessible_paper_rolls(lines)
    print(f"Total movable paper rolls: {total}")



# helper: check the entire map (one loop inside another loop)
# if paper rolls < 4, accumulate efficient paper roll counter
