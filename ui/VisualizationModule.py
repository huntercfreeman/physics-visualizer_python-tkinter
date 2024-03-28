import tkinter as tk
import ThemeModule
import VectorModule
from varname import nameof

class VisualizationDisplay(tk.Canvas):
    def __init__(self, parent: tk.Tk, root: tk.Tk):
        super().__init__(
            parent,
            bg=ThemeModule.theme_current.primary_background_color,
            highlightthickness=0)
        self.pack(side='top', fill='both', expand=1)
        self.root = root
        
        self.update()
        self.InitializeCoordinateSystem()

    def InitializeCoordinateSystem(self):
        self.canvas_tags_axis_y = "axis_y"
        self.canvas_tags_axis_x = "axis_x"
        self.canvas_tags_vector = "vector"

        self.vector_list = []

        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()
        
        def InitializeAxisX():
            canvas_height_halfway = canvas_height / 2.0
            self.create_line(
                0,
                canvas_height_halfway,
                canvas_width,
                canvas_height_halfway,
                fill=ThemeModule.theme_current.coordinate_system_axis_fill_color,
                tags=self.canvas_tags_axis_x)
        InitializeAxisX()

        def InitializeAxisY():
            canvas_width_halfway = canvas_width / 2.0
            self.create_line(
                canvas_width_halfway,
                0,
                canvas_width_halfway,
                canvas_height,
                fill=ThemeModule.theme_current.coordinate_system_axis_fill_color,
                tags=self.canvas_tags_axis_y)
        InitializeAxisY()

    def AddVector(self, vector: VectorModule.VectorModel):
        self.vector_list.append(vector)

        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()

        canvas_width_halfway = canvas_width / 2.0
        canvas_height_halfway = canvas_height / 2.0

        self.create_line(
            canvas_width_halfway,
            canvas_height_halfway,
            canvas_width_halfway + vector.components[0],
            canvas_height_halfway + -1 * vector.components[1],
            fill='red',
            tags=self.canvas_tags_vector)
