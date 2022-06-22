# PathFinder is a class that finds the shortest path between two points on a grid.
# The grid is a 2D array of integers.
# The pathfinder will find the shortest path between two points on the grid.
# The pathfinder will return the path as a list of coordinates.

from collections import defaultdict
from math import sqrt
import random
from collections import deque, namedtuple


class PathFinder:
    """
    PathFinder is a class that finds the shortest path between two points on a grid.

    The grid is a 2D array of integers.
    The pathfinder will find the shortest path between two points on the grid.
    The pathfinder will return the path as a list of coordinates.

    The grid is represented by an array of 0s. Any obstacle on the grid is represented by a 1.

    """

    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
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
            print("The grid does not have enough space for the obstacles")

        for i in range(num_obstacles):
            random_obstacle = random.choice(free_spaces)
            self.grid[random_obstacle[0]][random_obstacle[1]] = 1
            free_spaces.remove(random_obstacle)

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
        except AssertionError:
            print("The delivery point must be within the grid")

    def shortest_path(self, with_obstacle: bool) -> list[list[tuple]]:
        """
        This function returns a list of all possible paths from the starting point to the delivery point.
        The paths are represented as a list of tuples.
        """
        return [[]]

    def find_all_paths(self):
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
             "steps", "distance"]
        )

        start = step(
            self.starting_point[0], self.starting_point[1], None, None, [], 0, 0)
        end = step(
            self.delivery_point[0], self.delivery_point[1], None, None, [], 0, 0)

        visited_data = []
        visited_path = []

        self.find_path(start, end, self.all_paths, visited_data, visited_path)

        return self.all_paths

    def find_path(self, start: tuple, end: tuple, path: list[tuple], visited_data: list[tuple], visited_path: list[tuple]) -> list[tuple]:
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
             "steps", "distance"]
        )

        visited_data.append(start)
        visited_path.append((start.row, start.column))

        path.append(start)

        if (start.row, start.column) == (end.row, end.column):
            if path not in self.all_paths:
                delivery_point_arrived = (
                    item for item in path if item.row == end.row and item.column == end.column)
                distance_covered_by_path = delivery_point_arrived.distance
                steps_covered_by_path = delivery_point_arrived.steps
                obstacles_eliminated_by_path = len(delivery_point_arrived.obstacles_eliminated)
                self.all_paths.append(
                    (path)
                )

        else:
            # If current step is not destination
            # Recur for all the steps adjacent to this vertex
            for next_row, next_column in self._get_adjacent_spaces(start.row, start.column):

                distance = self._calculate_distance_between_points(
                    (start.row, start.column), (next_row, next_column))

                if self.grid[next_row][next_column] == 1:  # Next step is an obstacle
                    next_step = step(
                        row=next_row,
                        column=next_column,
                        parent_row=start.row,
                        parent_column=start.column,
                        obstacles_eliminated=list(
                            set(start.obstacles_eliminated+[(next_row, next_column)])),
                        distance=start.distance + distance,
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
                        distance=start.distance + distance,
                        steps=start.steps + 1
                    )

                if (next_row, next_column) not in visited_path:
                    self.find_path(
                        start=next_step,
                        end=end,
                        path=path,
                        visited_data=visited_data,
                        visited_path=visited_path
                    )

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

    def _calculate_distance_between_points(self, point_1: tuple, point_2: tuple) -> float:
        """
        It takes two points as input and returns the distance between them

        :param point_1: tuple
        :type point_1: tuple
        :param point_2: tuple
        :type point_2: tuple
        :return: The distance between two points.
        """
        return float(sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2))


# # This class represents a directed graph
# # using adjacency list representation

# class Graph:

#     def __init__(self, vertices):
#         # No. of vertices
#         self.V = vertices

#         # default dictionary to store graph
#         self.graph = defaultdict(list)

#     # function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)

#     '''A recursive function to print all paths from 'u' to 'd'.
# 	visited[] keeps track of vertices in current path.
# 	path[] stores actual vertices and path_index is current
# 	index in path[]'''

#     def printAllPathsUtil(self, u, d, visited, path):

#         # Mark the current node as visited and store in path
#         visited[u] = True
#         path.append(u)

#         # If current vertex is same as destination, then print
#         # current path[]
#         if u == d:
#             print(path)
#         else:
#             # If current vertex is not destination
#             # Recur for all the vertices adjacent to this vertex
#             for i in self.graph[u]:
#                 if visited[i] == False:
#                     self.printAllPathsUtil(i, d, visited, path)

#         # Remove current vertex from path[] and mark it as unvisited
#         path.pop()
#         visited[u] = False

#     # Prints all paths from 's' to 'd'
#     def printAllPaths(self, s, d):

#         # Mark all the vertices as not visited
#         visited = [False]*(self.V)

#         # Create an array to store paths
#         path = []

#         # Call the recursive helper function to print all paths
#         self.printAllPathsUtil(s, d, visited, path)


# # Create a graph given in the above diagram
# g = Graph(4)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(0, 3)
# g.addEdge(2, 0)
# g.addEdge(2, 1)
# g.addEdge(1, 3)

# s = 2
# d = 3
# print("Following are all different paths from % d to % d :" % (s, d))
# g.printAllPaths(s, d)
# # This code is contributed by Neelam Yadav
