def read_input(input_file_name):
    with open (input_file_name) as file:
        map = [x. strip() for x in file.readlines()]

    return map

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

def list_accessible_paper_rolls(map:list[str]) -> list[tuple[int, int]]:
    accessible_paper_rolls = []

    for y in range(len(map)):
        for x in range(len(map[0])):
            if char_at_xy(x, y, map) == '@':
                neighbor_count = adjacent_paper_rolls(x, y, map)
                if neighbor_count < 4:
                    accessible_paper_rolls.append((x, y))

    return accessible_paper_rolls

def copy_map(map: list[str]) -> list[str]:
    copied_map = map.copy()

    return copied_map

def replace_paper_rolls(map: list[str], removal_list: list[tuple[int, int]]):
    for removal in removal_list:
        x = removal[0]
        y = removal[1]

        map[y] = map[y][:x] + "x" + map[y][x + 1:]

def removed_paper_rolls_number(map: list[tuple[int, int]]) -> int:
    total_removed = 0

    working_map = copy_map(map)

    while True:
        removal_list = list_accessible_paper_rolls(working_map)

        if not removal_list:
            break

        replace_paper_rolls(working_map,removal_list)
        total_removed += len(removal_list)

    return total_removed


# main program
if __name__ == "__main__":
    map = read_input("puzzle_input")
    total = removed_paper_rolls_number(map)
    print(f"Total movable paper rolls: {total}")
