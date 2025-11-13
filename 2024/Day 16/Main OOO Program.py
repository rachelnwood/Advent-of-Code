from Maze import Maze
from MazeSolver import MazeSolver

if __name__ == "__main__":
    initial_facing_direction = "east"

    maze_object = Maze("Test Input")
    maze_solver_object = MazeSolver(maze_object)

    start_location = maze_object.find_start()
    start_location_for_solver = (start_location[0], start_location[1], initial_facing_direction)

    end_location = maze_object.find_end()

    maze1_score = maze_solver_object.solver(start_location_for_solver, end_location)

    # maze 2
    maze2 = Maze("Test Input 2")
    maze_solver_object.set_maze(maze2)
    start_location = maze2.find_start()
    start_location_for_solver = (start_location[0], start_location[1], initial_facing_direction)

    end_location = maze2.find_end()

    maze2_score = (maze_solver_object.solver(start_location_for_solver, end_location))

    # maze 3
    maze3 = Maze("Puzzle Input")
    maze_solver_object.set_maze(maze3)
    start_location = maze3.find_start()
    start_location_for_solver = (start_location[0], start_location[1], initial_facing_direction)

    end_location = maze3.find_end()

    maze3_score = (maze_solver_object.solver(start_location_for_solver, end_location))

    print(f'Maze 1: {maze1_score}\nMaze 2: {maze2_score}\nMaze 3: {maze3_score}')