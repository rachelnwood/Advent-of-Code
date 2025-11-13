class Maze:
    def __init__(self, file_name):

        with open(file_name) as file:
            self.maze = [x.strip() for x in file.readlines()]

        for line in self.maze:
            print(line)

    def find_start(self):
        return self.__location_for_character("S")

    def find_end(self):
        return self.__location_for_character("E")

    def character_at_xy(self, x, y):
        return self.maze[y][x]

    def __location_for_character(self, character):
        line_count = len(self.maze)
        row_length = len(self.maze[0])

        for y in range(line_count):
            for x in range(row_length):
                if self.character_at_xy(x, y) == character:
                    return (x, y)

    cardinal_directions = {'west': (-1, 0), 'north': (0, -1), 'east': (1, 0), 'south': (0, 1)}
    opposite_direction = {"north": "south", "south": "north", "east": "west", "west": "east"}

    def next_states(self, x, y, facing_direction):
        result = []
        direction_to_skip = self.opposite_direction.get(facing_direction)

        # Calculate where we can move to
        for key in self.cardinal_directions.keys():
            if key == direction_to_skip:
                continue

            dx, dy = self.cardinal_directions[key]
            new_x = x + dx
            new_y = y + dy
            char = self.character_at_xy(new_x, new_y)

            if char == '.' or char == 'E':
                new_facing = key
                if new_facing == facing_direction:
                    cost = 1
                else:
                    cost = 1000 + 1

                result.append((cost, (new_x, new_y, new_facing)))

        return result