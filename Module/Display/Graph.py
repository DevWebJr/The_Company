import numpy as np
import matplotlib.pyplot as schema


class Graph():
    def __init__(self, title: str = "", x_label: str = "", y_label: str = "", figsize=(int, int)):
        self._id= id
        self._title = title
        self._x_label = x_label
        self._y_label = y_label
        self._figsize = figsize
        self._show_grid = True

    """Getters & Setters"""
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def x_label(self):
        return self._x_label

    @x_label.setter
    def x_label(self, value):
        self._x_label = value

    @property
    def y_label(self):
        return self._y_label

    @y_label.setter
    def y_label(self, value):
        self._y_label = value

    @property
    def show_grid(self):
        return self._show_grid

    @show_grid.setter
    def show_grid(self, value):
        self._show_grid = value

    """Methods"""

    def show(self, x_values, y_values, title):


        schema.figure(figsize=(12, 8))
        #values of x and y
        schema.plot(y_values, x_values, c="green", lw=3.5)
        schema.title(title)
        schema.xlabel(self._x_label)
        schema.ylabel(self._y_label)
        schema.title(self._title)
        schema.grid(self._show_grid)
        
        schema.show()

    def xy_values(self, zones):
        raise NotImplementedError
