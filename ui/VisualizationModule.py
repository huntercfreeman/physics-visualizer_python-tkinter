import tkinter as tk
import ThemeModule
import VectorModule

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

        width_midpoint = canvas_width / 2.0
        height_midpoint = canvas_height / 2.0
        
        def InitializeAxisX():
            # Create the axis itself
            self.create_line(
                0,
                height_midpoint,
                canvas_width,
                height_midpoint,
                fill=ThemeModule.theme_current.coordinate_system_axis_fill_color,
                tags=self.canvas_tags_axis_x)

            # Create 'ticks' for positive-values along the axis for visually determining coordinate positions
            counter_magnitude = (canvas_width / 2) * 0.1
            tick_height = 10
            for counter in range(0, 10):
                offset = (counter + 1) * counter_magnitude
                tick_pos_x = width_midpoint + offset
                # TODO: Calculate height of text
                height_of_text = 10
                self.create_line(
                    tick_pos_x,
                    height_midpoint - tick_height,
                    tick_pos_x,
                    height_midpoint + tick_height,
                    fill=ThemeModule.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    tick_pos_x,
                    height_midpoint + tick_height + height_of_text,
                    text=f'{int(offset)}',
                    fill=ThemeModule.theme_current.coordinate_system_axis_fill_color)

            # Create 'ticks' for negative-values along the axis for visually determining coordinate positions
            counter_magnitude = (canvas_width / 2) * 0.1
            tick_height = 10
            for counter in range(0, 10):
                offset = -1 * ((counter + 1) * counter_magnitude)
                tick_pos_x = width_midpoint + offset
                # TODO: Calculate height of text
                height_of_text = 10
                self.create_line(
                    tick_pos_x,
                    height_midpoint - tick_height,
                    tick_pos_x,
                    height_midpoint + tick_height,
                    fill=ThemeModule.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    tick_pos_x,
                    height_midpoint + tick_height + height_of_text,
                    text=f'{int(offset)}',
                    fill=ThemeModule.theme_current.coordinate_system_axis_fill_color)
        InitializeAxisX()

        def InitializeAxisY():
            # Create the axis itself
            self.create_line(
                width_midpoint,
                0,
                width_midpoint,
                canvas_height,
                fill=ThemeModule.theme_current.coordinate_system_axis_fill_color,
                tags=self.canvas_tags_axis_y)
            
            # Create 'ticks' for positive-values along the axis for visually determining coordinate positions
            counter_magnitude = (canvas_height / 2) * 0.1
            tick_width = 10
            for counter in range(0, 10):
                offset = (counter + 1) * counter_magnitude
                tick_pos_y = height_midpoint - offset
                # TODO: Calculate width of text
                text_offset = 20
                self.create_line(
                    width_midpoint - tick_width,
                    tick_pos_y,
                    width_midpoint + tick_width,
                    tick_pos_y,
                    fill=ThemeModule.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    width_midpoint + tick_width + text_offset,
                    tick_pos_y,
                    text=f'{int(offset)}',
                    fill=ThemeModule.theme_current.coordinate_system_axis_fill_color)
                
            # Create 'ticks' for negative-values along the axis for visually determining coordinate positions
            counter_magnitude = (canvas_height / 2) * 0.1
            tick_width = 10
            for counter in range(0, 10):
                offset = -1 * ((counter + 1) * counter_magnitude)
                tick_pos_y = height_midpoint - offset
                # TODO: Calculate width of text
                text_offset = 20
                self.create_line(
                    width_midpoint - tick_width,
                    tick_pos_y,
                    width_midpoint + tick_width,
                    tick_pos_y,
                    fill=ThemeModule.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    width_midpoint + tick_width + text_offset,
                    tick_pos_y,
                    text=f'{int(offset)}',
                    fill=ThemeModule.theme_current.coordinate_system_axis_fill_color)
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
            fill=ThemeModule.theme_current.primary_foreground_color,
            arrow='last',
            width=2,
            tags=self.canvas_tags_vector)
