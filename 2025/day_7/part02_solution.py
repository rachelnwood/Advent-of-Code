from functools import lru_cache

class BeamMap:
    # constructor to establish map in BeamMap obj
    def __init__(self, file_name):
        self.lines = read_input(file_name)

    # constructor to build objects for testing
    @classmethod
    def from_lines(cls, lines: list[str]):
        obj = cls.__new__(cls)
        obj.lines = lines
        return obj

    def bottom_map_index(self) -> int:
        index = len(self.lines) - 1
        return index

    def char_at_x_y(self, x: int, y: int) -> str:
        return self.lines[y][x]

    def first_splitter(self) -> int:
        line = self.lines[2]
        all_splitters = [index for index, char in enumerate(line) if char == "^"]
        x_to_return = all_splitters[0]

        return x_to_return

def read_input(file_name):
    with open (file_name) as file:
        lines = [x. strip() for x in file]

    return lines

@lru_cache(maxsize=None)
def recursive_beams(map: BeamMap, x: int, y: int) -> int:
    if y == map.bottom_map_index():
        return 1

    if map.char_at_x_y(x,y) == "^":
        return (
            recursive_beams(map, x-1, y+1) + recursive_beams(map, x+1, y+1)
        )
    else:
        return recursive_beams(map, x, y+1)

# main program
if __name__ == "__main__":
    map = BeamMap("puzzle_input")
    starting_x = map.first_splitter()

    total_timelines = recursive_beams(map, starting_x, 2)
    print(f"There are {total_timelines} total timelines")