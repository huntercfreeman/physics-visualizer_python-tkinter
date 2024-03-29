import tkinter as tk
import ThemeModule
import VectorModule

class CoordinatesVisualization:
    """Stores coordinates as a list.
    Index 0 corresponds to the x-axis, 1 to the y-axis, 2 to the z-axis, etc..."""
    def __init__(self, coordinates: list):
        self.coordinates = coordinates

class VectorVisualization:
    def __init__(self, vector: VectorModule.VectorModel, coordinates: CoordinatesVisualization):
        self.components = vector.components
        self.coordinates = coordinates.coordinates

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

        self.vector_visualization_list = []

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

    def AddVector(self,
                  vector: VectorModule.VectorModel,
                  coordinates: CoordinatesVisualization = CoordinatesVisualization([0, 0])):
        
        vector_visualization = VectorVisualization(vector, coordinates)
        self.vector_visualization_list.append(vector_visualization)
        self.DrawVectorVisualization(vector_visualization)
        
    def DrawVectorVisualization(self, vector_visualization: VectorVisualization):
        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()

        canvas_width_halfway = canvas_width / 2.0
        canvas_height_halfway = canvas_height / 2.0

        initial_x = canvas_width_halfway + vector_visualization.coordinates[0]
        initial_y = canvas_height_halfway - vector_visualization.coordinates[1]

        self.create_line(
            initial_x,
            initial_y,
            initial_x + vector_visualization.components[0],
            initial_y + (-1 * vector_visualization.components[1]),
            fill=ThemeModule.theme_current.primary_foreground_color,
            arrow='last',
            width=2,
            tags=self.canvas_tags_vector)

    def SetVectorVisualizationList(self, vector_visualization_list: list):
        self.vector_visualization_list = vector_visualization_list

        for vector_visualization in self.vector_visualization_list:
            self.DrawVectorVisualization(vector_visualization)

class CoordinatesEditorDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk, coordinates: CoordinatesVisualization):
        super().__init__(parent, bg=ThemeModule.theme_current.footer_background_color)
        self.pack(side="left", fill="both", expand=1)
        self.coordinates = coordinates
        self.x_string_var=tk.StringVar()
        self.y_string_var=tk.StringVar()

        self.x_string_var.set(self.coordinates.coordinates[0])
        self.y_string_var.set(self.coordinates.coordinates[1])
        
        coordinatesLength = len(self.coordinates.coordinates)
        
        header_frame = tk.Frame(self)
        body_frame = tk.Frame(self)

        header_frame.pack(side='left')
        body_frame.pack(side='left')

        # Header content
        label = tk.Label(
            header_frame,
            text='Coordinates:',
            bg=ThemeModule.theme_current.footer_background_color,
            fg=ThemeModule.theme_current.primary_foreground_color)
        label.pack()
        
        # Body content
        if coordinatesLength != 2:
            label = tk.Label(
                body_frame,
                text=f'{coordinatesLength} dimensions are not supported.',
                bg=ThemeModule.theme_current.footer_background_color,
                fg=ThemeModule.theme_current.primary_foreground_color)
            label.pack()
        else:
            x_label = tk.Label(
                body_frame,
                text='x',
                bg=ThemeModule.theme_current.header_background_color,
                fg=ThemeModule.theme_current.primary_foreground_color)
            
            x_entry = tk.Entry(body_frame, textvariable=self.x_string_var)
            
            y_label = tk.Label(
                body_frame,
                text='y',
                bg=ThemeModule.theme_current.header_background_color,
                fg=ThemeModule.theme_current.primary_foreground_color)
            
            y_entry=tk.Entry(body_frame, textvariable=self.y_string_var)

            x_label.grid(row=0,column=0)
            x_entry.grid(row=0,column=1)
            
            y_label.grid(row=1,column=0)
            y_entry.grid(row=1,column=1)