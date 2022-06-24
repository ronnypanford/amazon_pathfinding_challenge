"""
Visualizer for the PathFinder class using pygame.
"""
import sys
import pygame
from tkinter import messagebox, Tk

window_size = (window_width, window_height) = 640, 480


# This class is a visualizer for the PathFinder class
class PathFinderVisualizer:
    """Visualizer for the PathFinder class"""

    def __init__(self):
        """
        It initializes the pygame window and sets the window size, caption, and clock
        """
        self.grid_width = 0
        self.grid_height = 0
        self.box_width = 0
        self.box_height = 0

        self.visualizer = pygame
        self.visualizer.init()
        self.window = self.visualizer.display.set_mode(window_size)
        self.window.fill((0, 20, 20))  # Fill the window with a colour
        self.visualizer.display.set_caption(
            "Optimized A*-adopted Path Finder Algorithm")
        self.clock = self.visualizer.time.Clock()

    def draw_grid(self, grid_width, grid_height):
        """
        It draws a grid of boxes on the screen, each box being a certain width and height

        :param grid_width: The number of boxes in the grid's width
        :param grid_height: The number of rows in the grid
        """
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.box_width = window_width // self.grid_width
        self.box_height = window_height // self.grid_height

        for row in range(self.grid_height):
            for column in range(self.grid_width):
                self.show(row, column, (44, 62, 80))

    def show(self, row, column, colour, border=0):
        """
        It draws a rectangle on the screen

        :param row: The row of the box to be shown
        :param column: The column of the grid to show
        :param colour: The colour of the box
        """
        self.visualizer.draw.rect(
            self.window,
            colour,
            (row * self.box_width,
             column * self.box_height,
             self.box_width - 1,
             self.box_height - 1),
            border
        )
        self.visualizer.display.update()

    def show_start_point(self, row, column):
        """
        It takes in a row and column and shows the start point

        :param row: the row of the start point
        :param column: The column of the cell to show
        """

        self.show(row, column, (0, 255, 200), int(0.05*self.box_width))

        font = self.visualizer.font.SysFont(
            self.visualizer.font.get_default_font(), int(0.2*self.box_width))
        self.window.blit(
            font.render('START', True, (0, 0, 0)), (
                (row*self.box_width+(2*row+self.box_width)//2 - self.box_width//5), (column*self.box_height+(2*column+self.box_height)//2 - self.box_height//10))
        )
        self.visualizer.display.update()

    def show_end_point(self, row, column):
        """
        It takes in a row and column and shows the end point

        :param row: the row of the cell to show
        :param column: The column of the cell to show
        """

        self.show(row, column, (0, 120, 255), int(0.05*self.box_width))

        font = self.visualizer.font.SysFont(
            self.visualizer.font.get_default_font(), int(0.2*self.box_width))
        self.window.blit(
            font.render('END', True, (0, 0, 0)), (
                (row*self.box_width+(2*row+self.box_width)//2 - self.box_width//5), (column*self.box_height+(2*column+self.box_height)//2 - self.box_height//10))
        )
        self.visualizer.display.update()

    def show_obstacle_point(self, row, column):
        """
        It takes in a row and column and shows the obstacle point

        :param row: the row of the cell to show
        :param column: The column of the cell to show
        """
        self.show(row, column, (90, 0, 0))

    def show_path(self, path, selected_path=False):
        """
        It takes a path and a boolean value, and if the boolean value is true, it will show the path in
        green for the final selected path, otherwise it will show the path in blue for detected paths

        :param path: The path to show
        :param selected_path: If True, the path will be shown in green. If False, the path will be shown
        in blue, defaults to False (optional)
        """
        colour = (0, 255, 0) if selected_path else (0, 0, 255)
        for step in path:
            if selected_path:
                self.show(step.row, step.column, colour)
            else:
                if path.index(step) > 0:
                    current = step
                    previous = path[path.index(step) - 1]
                    self.visualizer.draw.aaline(
                        self.window,
                        colour,
                        (current.row * self.box_width + (2*current.row+self.box_width)//2,
                         current.column * self.box_height + (2*current.column+self.box_height)//2),
                        (previous.row * self.box_width + (2*previous.row+self.box_width)//2,
                         previous.column * self.box_height + (2*previous.column+self.box_height)//2),
                        blend=1
                    )
                    self.visualizer.display.update()

            if path.index(step) == 0:
                font = self.visualizer.font.SysFont(
                    self.visualizer.font.get_default_font(), int(0.2*self.box_width)
                )
                self.window.blit(
                    font.render('START', True, (0, 0, 0)), (
                        (step.row*self.box_width+(2*step.row+self.box_width)//2 - self.box_width//5), (step.column*self.box_height+(2*step.column+self.box_height)//2 - self.box_height//10))
                )
            if path.index(step) == len(path)-1:
                font = self.visualizer.font.SysFont(
                    self.visualizer.font.get_default_font(), int(0.2*self.box_width)
                )
                self.window.blit(
                    font.render('END', True, (0, 0, 0)), (
                        (step.row*self.box_width+(2*step.row+self.box_width)//2 - self.box_width//5), (step.column*self.box_height+(2*step.column+self.box_height)//2 - self.box_height//10))
                )
            self.visualizer.display.update()

    def check_exit_clicked(self):
        """
        It checks if the user has clicked the exit button on the window
        """
        for event in self.visualizer.event.get():
            if event.type == self.visualizer.QUIT:
                self.exit()

    def exit(self):
        """
        The function takes in a self parameter, which is the instance of the class, and then calls the
        quit() function on the visualizer object, which is an instance of the class Visualizer, and then
        exits the program
        """
        self.visualizer.quit()
        sys.exit()
