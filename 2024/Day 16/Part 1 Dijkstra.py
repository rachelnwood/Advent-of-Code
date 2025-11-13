import heapq

inputFileName = "Puzzle Input"

with open (inputFileName) as file:
    map = [x. strip() for x in file.readlines()]

for line in map:
    print(line)

cardinal_directions = {'west':  (-1,  0), 'north': ( 0, -1), 'east':  ( 1,  0), 'south': ( 0,  1)}
opposite_direction = {"north": "south", "south": "north", "east": "west", "west": "east"}

def character_at_xy(x,y):
    return map[y][x]

def location_for_character(character):
    line_count = len(map)
    row_length = len(map[0])

    for y in range(line_count):
        for x in range(row_length):
          if character_at_xy(x, y) == character:
              return (x, y)

def calculate_score(facingDirection, newFacingDirection):
    if facingDirection == newFacingDirection:
        return 1
    else:
        return 1000 + 1

def next_states(x, y, facing_direction):
    result = []
    direction_to_skip = opposite_direction.get(facing_direction)

    # Calculate where we can move to
    for key in cardinal_directions.keys():
        if key == direction_to_skip:
            continue

        dx, dy = cardinal_directions[key]
        new_x = x + dx
        new_y = y + dy
        char = character_at_xy(new_x, new_y)

        if char == '.' or char == 'E':
            new_facing = key
            if new_facing == facing_direction:
                cost = 1
            else:
                cost = 1000 + 1

            result.append((cost, (new_x, new_y, new_facing)))

    return result

def dijkstra(starting_location, goal_location):
    pq = []
    heapq.heappush(pq, (0, starting_location))
    best_cost = {starting_location: 0}

    while pq:
        cost, (x, y, facing) = heapq.heappop(pq)
        print(f'cost: {cost}, state: {x}, {y}, {facing}')

        # If we've reached the goal position (any direction counts)
        if (x, y) == goal_location:
            return cost

        # Skip outdated entries
        if cost > best_cost[(x, y, facing)]:
            continue

        places_to_go = next_states(x, y, facing)
        for next_cost, next_state in places_to_go:
            # print (f"cost: {next_cost}, state: {next_state}")
            new_cost = cost + next_cost

            if new_cost < best_cost.get(next_state, float('inf')):
                best_cost[next_state] = new_cost
                heapq.heappush(pq, (new_cost, next_state))

    return None

# main program
start_x, start_y = location_for_character('S')
start = (start_x, start_y, 'east')
end_x, end_y = location_for_character('E')
end = (end_x, end_y)

print(dijkstra(start, end))