import heapq

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze

    def set_maze(self, maze):
        self.maze = maze

    def solver(self, starting_location, goal_location):
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

            places_to_go = self.maze.next_states(x, y, facing)
            for next_cost, next_state in places_to_go:
                # print (f"cost: {next_cost}, state: {next_state}")
                new_cost = cost + next_cost

                if new_cost < best_cost.get(next_state, float('inf')):
                    best_cost[next_state] = new_cost
                    heapq.heappush(pq, (new_cost, next_state))

        return None