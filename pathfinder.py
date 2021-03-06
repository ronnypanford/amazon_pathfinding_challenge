# PathFinder is a class that finds the shortest path between two points on a grid.
# The grid is a 2D array of integers.
# The pathfinder will find the shortest path between two points on the grid.
# The pathfinder will return the path as a list of coordinates.

from math import sqrt
import random
from collections import namedtuple
import time
from pathfinder_visualizer import PathFinderVisualizer


class PathFinder:
    """
    PathFinder is a class that finds the shortest path between two points on a grid.

    The grid is a 2D array of integers.
    The pathfinder will find the shortest path between two points on the grid.
    The pathfinder will return the path as a list of coordinates.

    The grid is represented by an array of 0s. Any obstacle on the grid is represented by a 1.

    """

    def __init__(self, visualize=False) -> None:
        self.visualize = visualize
        if self.visualize:
            self.pathfinder_visualizer = PathFinderVisualizer()
        self.grid = []
        self.all_paths = []
        self.obstacles = []
        self.starting_point = (0, 0)
        self.delivery_point = (0, 0)

    def create_grid_with_obstacles(self, grid_width: int, grid_height: int, obstacles: list[tuple]) -> list[list[int]]:
        """
        This function creates a grid of the specified width and height, and then adds obstacles to the
        grid

        :param grid_width: The width of the grid
        :type grid_width: int
        :param grid_height: The height of the grid
        :type grid_height: int
        :param obstacles: list[tuple]
        :type obstacles: list[tuple]
        :return: A list of lists of integers.
        """
        grid = self.create_grid(grid_width, grid_height)
        self.add_obstacles(obstacles)
        return grid

    def create_grid(self, width: int, height: int) -> list[list[int]]:
        """
        It creates a grid of zeros with the given width and height

        :param width: int - The width of the grid
        :type width: int
        :param height: int
        :type height: int
        :return: A list of lists of integers.
        """
        grid = []
        for row in range(height):
            grid.append([])
            for column in range(width):
                grid[row].append(0)
        self.grid = grid

        if self.visualize:
            self.pathfinder_visualizer.draw_grid(
                grid_width=width, grid_height=height
            )

        # Default the starting and delivery positions to both far corners of the grid
        self.starting_point = (0, 0)
        self.delivery_point = (len(self.grid)-1, len(self.grid[0])-1)
        return self.grid

    def add_obstacles(self, obstacles: list[tuple]) -> None:
        """
        This function takes in a list of tuples, and for each tuple in the list, it sets the value of
        the grid at that tuple to 1

        :param obstacles: list[tuple]
        :type obstacles: list[tuple]
        """
        existing_obstacles = list(
            set(self.obstacles).intersection(set(obstacles))
        )

        if len(set(obstacles)) < len(obstacles):
            print(
                "Obstacles Not Added: There are duplicate obstacles in the provided list")
        elif existing_obstacles:
            print("Obstacles Not Added: There are obstacles already at" + " ,".join(
                str(obstacle) for obstacle in existing_obstacles)
            )
        elif not set([self.starting_point, self.delivery_point]).isdisjoint(set(obstacles)):
            print(
                "Obstacles Not Added: An obstacle cannot be placed at the starting or delivery points")
        else:
            for obstacle in obstacles:
                self.grid[obstacle[0]][obstacle[1]] = 1
                self.obstacles.append(obstacle)
                if self.visualize:
                    self.pathfinder_visualizer.show_obstacle_point(
                        obstacle[0], obstacle[1]
                    )

    def add_random_obstacles(self, num_obstacles: int) -> None:
        """
        This function adds random obstacles to the grid.
        First check that the grid has enough space for the obstacles.
        The obstacles would not overlap existing ones.
        The obstacles would not be placed at the starting and delivery points.

        :param num_obstacles: int - The number of obstacles to add to the grid
        :type num_obstacles: int
        """

        free_spaces = []
        for row, columns in enumerate(self.grid):
            for column, _ in enumerate(columns):
                if (self.grid[row][column] == 0 and
                    (row, column) != self.starting_point and
                        (row, column) != self.delivery_point):
                    free_spaces.append((row, column))

        try:
            assert num_obstacles <= len(free_spaces)
        except AssertionError:
            print("The grid does not have enough free space for the obstacles")
            raise

        for i in range(num_obstacles):
            random_obstacle = random.choice(free_spaces)
            self.grid[random_obstacle[0]][random_obstacle[1]] = 1
            self.obstacles.append(random_obstacle)
            free_spaces.remove(random_obstacle)
            if self.visualize:
                self.pathfinder_visualizer.show_obstacle_point(
                    random_obstacle[0], random_obstacle[1]
                )

    def set_starting_point(self, starting_point: tuple) -> None:
        """
        The function takes in a tuple of two integers, and if the integers are within the grid, it sets
        the starting point to the tuple

        :param starting_point: The starting point of the grid
        :type starting_point: tuple
        """

        try:
            assert starting_point[0] >= 0 and starting_point[0] < len(
                self.grid)
            assert starting_point[1] >= 0 and starting_point[1] < len(
                self.grid[0])

            try:
                assert self.grid[starting_point[0]][starting_point[1]] == 0
            except AssertionError:
                print("The starting point must not be on an obstacle on the grid")

            self.starting_point = starting_point
            if self.visualize:
                self.pathfinder_visualizer.show_start_point(
                    starting_point[0], starting_point[1]
                )
        except AssertionError:
            print("The starting point must be within the grid")

    def set_delivery_point(self, delivery_point: tuple) -> None:
        """
        The function takes in a tuple of two integers, and if the integers are within the grid, it sets
        the delivery point to the tuple

        :param delivery_point: The delivery point of the grid
        :type delivery_point: tuple
        """
        try:
            assert delivery_point[0] >= 0 and delivery_point[0] < len(
                self.grid)
            assert delivery_point[1] >= 0 and delivery_point[1] < len(
                self.grid[0])

            try:
                assert self.grid[delivery_point[0]][delivery_point[1]] == 0
            except AssertionError:
                print("The delivery point must not be on an obstacle on the grid")

            try:
                assert self.starting_point != delivery_point
            except AssertionError:
                print("The delivery point cannot be the same starting location")

            self.delivery_point = delivery_point
            if self.visualize:
                self.pathfinder_visualizer.show_end_point(
                    delivery_point[0], delivery_point[1]
                )
        except AssertionError:
            print("The delivery point must be within the grid")

    def shortest_path(self, allow_obstacle_elimination: bool) -> list[list[tuple]]:
        """
        The function finds all paths from the start to the end, sorts them by least obstacles
        encountered, then by least steps taken, and returns the shortest path

        :param allow_obstacle_elimination: bool
        :type allow_obstacle_elimination: bool
        :return: The shortest path
        """
        start_time = time.time()
        self.find_all_paths(paths_with_obstacles=allow_obstacle_elimination)
        end_time = time.time()

        elapsed_time = end_time - start_time

        print(
            f"\nOf the many paths processed, found viable paths are: {len(self.all_paths)}")
        print(f"The time taken to find all viable paths is: {elapsed_time}s")

        if len(self.all_paths) == 0:
            print("\nNO PATH FOUND\n")
            selected_path = ()
            return selected_path

        # Sort by least obstacles encountered, then by least steps taken
        sorted_paths = sorted(
            self.all_paths, key=lambda path: (path[1], path[0]))

        selected_path = sorted_paths[0]

        if not allow_obstacle_elimination:
            if selected_path[1] > 0:
                print("\nUNABLE TO REACH DELIVERY POINT")
                selected_path = ()
                return selected_path

        if selected_path[1]:
            print("\nUNABLE TO REACH DELIVERY POINT")
            print(
                f"For the shortest potential path, remove obstacles at: {selected_path[2][-1].obstacles_eliminated}")
        else:
            print("\nSHORTEST PATH FOUND")
            print("The path is: " + str([(path_step.row, path_step.column)
                                         for path_step in selected_path[2]]))
            print(f"The path steps taken are: {selected_path[0]}")
            print(f"The path obstacles encountered are: {selected_path[1]}\n")

            if self.visualize:
                self.pathfinder_visualizer.show_path(selected_path[2], selected_path=True)
        return selected_path

    def find_all_paths(self, paths_with_obstacles: bool):
        """
        It finds all possible paths from the starting point to the delivery point
        :return: a list of tuples. Each tuple contains the following information:
        """
        step = namedtuple(
            "step",
            ["row",
             "column",
             "parent_row",
             "parent_column",
             "obstacles_eliminated",
             "steps"
             ]
        )

        start = step(
            self.starting_point[0], self.starting_point[1], None, None, [], 0)
        end = step(
            self.delivery_point[0], self.delivery_point[1], None, None, [], 0)

        visited_data = []
        visited_path = []
        path = []

        self.find_path(start, end, path, visited_data,
                       visited_path, paths_with_obstacles)

        return self.all_paths

    def find_path(self, start: tuple, end: tuple, path: list[tuple], visited_data: list[tuple], visited_path: list[tuple], paths_with_obstacles: bool) -> list[tuple]:
        """
        This function finds all possible paths from the starting point to the delivery point.
        The paths are represented as a list of tuples.
        """

        step = namedtuple(
            "step",
            ["row",
             "column",
             "parent_row",
             "parent_column",
             "obstacles_eliminated",
             "steps"
             ]
        )

        visited_data.append(start)
        visited_path.append((start.row, start.column))

        path.append(start)

        if (start.row, start.column) == (end.row, end.column):
            delivery_point_arrived = start

            steps_covered_by_path = delivery_point_arrived.steps
            obstacles_eliminated_by_path = len(
                delivery_point_arrived.obstacles_eliminated)

            path_summary = (
                steps_covered_by_path,
                obstacles_eliminated_by_path,
                path.copy()
            )
            self.all_paths.append(path_summary)

            if self.visualize:
                self.pathfinder_visualizer.show_path(path.copy())

        else:

            next_closest_to_end_steps = None
            next_with_obstacle_closest_to_end_steps = None

            for next_row, next_column in self._get_adjacent_spaces(start.row, start.column):

                if not paths_with_obstacles:
                    if self.grid[next_row][next_column] == 1:
                        continue

                steps_to_end = self._calculate_shortest_steps_between_points(
                    (next_row, next_column), (end.row, end.column))

                if self.grid[next_row][next_column] == 1:
                    if next_with_obstacle_closest_to_end_steps == None:
                        next_with_obstacle_closest_to_end_steps = steps_to_end
                    elif steps_to_end <= next_with_obstacle_closest_to_end_steps:
                        next_with_obstacle_closest_to_end_steps = steps_to_end
                    else:
                        # Do not go with that adjacent point as it is not optimum
                        continue
                else:
                    if next_closest_to_end_steps == None:
                        next_closest_to_end_steps = steps_to_end
                    elif steps_to_end <= next_closest_to_end_steps:
                        next_closest_to_end_steps = steps_to_end
                    else:
                        # Do not go with that adjacent point as it is not optimum
                        continue

                if self.grid[next_row][next_column] == 1:  # Next step is an obstacle
                    next_step = step(
                        row=next_row,
                        column=next_column,
                        parent_row=start.row,
                        parent_column=start.column,
                        obstacles_eliminated=list(
                            set(start.obstacles_eliminated+[(next_row, next_column)])),
                        steps=start.steps + 1
                    )
                else:
                    next_step = step(
                        row=next_row,
                        column=next_column,
                        parent_row=start.row,
                        parent_column=start.column,
                        obstacles_eliminated=list(
                            set(start.obstacles_eliminated)),
                        steps=start.steps + 1
                    )

                if (next_row, next_column) not in visited_path:
                    self.find_path(
                        start=next_step,
                        end=end,
                        path=path,
                        visited_data=visited_data,
                        visited_path=visited_path,
                        paths_with_obstacles=paths_with_obstacles
                    )
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited_data.remove(start)
        visited_path.remove((start.row, start.column))

    def _get_adjacent_spaces(self, row: int, col: int) -> list[tuple]:
        """
        It returns a generator that yields the coordinates of all adjacent spaces to the given space

        :param row: int: The row of the square we're checking
        :type row: int
        :param col: int: The column of the space to get adjacent spaces for
        :type col: int
        """
        # Adjacent obstacles are the four sides of the square and four corners
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                # Check if the adjacent square is on the grid
                if (row + row_offset >= 0 and
                    row + row_offset < len(self.grid) and
                    col + col_offset >= 0 and
                        col + col_offset < len(self.grid[0])):
                    if (row + row_offset, col + col_offset) != (row, col):
                        yield (row + row_offset, col + col_offset)

    def _calculate_shortest_steps_between_points(self, point_1: tuple, point_2: tuple) -> float:
        horizontal_steps = abs(point_2[0] - point_1[0])
        vertical_steps = abs(point_2[1] - point_1[1])
        least_steps = 0

        if horizontal_steps > vertical_steps:
            # Go diagonally by the count of vertical steps then continue straight
            # in the remaining horizontal to the point
            least_steps += vertical_steps
            least_steps += horizontal_steps-vertical_steps
        elif vertical_steps > horizontal_steps:
            # Go diagonally by the count of horizontal steps then continue straight
            # in the remaining vertical to the point
            least_steps += horizontal_steps
            least_steps += vertical_steps-horizontal_steps
        else:
            least_steps = horizontal_steps  # Least steps is going diagonal
            # Since the vertical and horizontal steps are the same going diagonal
            # by either of their amount would get you to the end

        return least_steps
