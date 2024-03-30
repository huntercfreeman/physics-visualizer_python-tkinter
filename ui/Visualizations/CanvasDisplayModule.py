import tkinter as tk
import VisualizationServiceModule
import CoordinatesVisualizationModule
import VectorVisualizationModule
import Themes
import Vectors

class CanvasDisplay(tk.Canvas):
    def __init__(self, parent: tk.Tk, root: tk.Tk):
        super().__init__(
            parent,
            bg=Themes.theme_service.theme_current.primary_background_color,
            highlightthickness=0)

        self.pack(side='left', fill='both', expand=1)
        self.root = root
        
        self.update()
        self.InitializeCoordinateSystem()

    def InitializeCoordinateSystem(self):
        self.canvas_tags_axis_y = "axis_y"
        self.canvas_tags_axis_x = "axis_x"
        self.canvas_tags_vector = "vector"

        self.vector_visualization_list: list[VectorVisualizationModule.VectorVisualization] = []

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
                fill=Themes.theme_service.theme_current.coordinate_system_axis_fill_color,
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
                    fill=Themes.theme_service.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    tick_pos_x,
                    height_midpoint + tick_height + height_of_text,
                    text=f'{int(offset)}',
                    fill=Themes.theme_service.theme_current.coordinate_system_axis_fill_color)

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
                    fill=Themes.theme_service.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    tick_pos_x,
                    height_midpoint + tick_height + height_of_text,
                    text=f'{int(offset)}',
                    fill=Themes.theme_service.theme_current.coordinate_system_axis_fill_color)
        InitializeAxisX()

        def InitializeAxisY():
            # Create the axis itself
            self.create_line(
                width_midpoint,
                0,
                width_midpoint,
                canvas_height,
                fill=Themes.theme_service.theme_current.coordinate_system_axis_fill_color,
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
                    fill=Themes.theme_service.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    width_midpoint + tick_width + text_offset,
                    tick_pos_y,
                    text=f'{int(offset)}',
                    fill=Themes.theme_service.theme_current.coordinate_system_axis_fill_color)
                
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
                    fill=Themes.theme_service.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    width_midpoint + tick_width + text_offset,
                    tick_pos_y,
                    text=f'{int(offset)}',
                    fill=Themes.theme_service.theme_current.coordinate_system_axis_fill_color)
        InitializeAxisY()

    def AddVector(self,
                  vector: Vectors.VectorModelModule.VectorModel,
                  coordinates: CoordinatesVisualizationModule.CoordinatesVisualization = CoordinatesVisualizationModule.CoordinatesVisualization([0, 0])):
        
        vector_visualization = VectorVisualizationModule.VectorVisualization(vector, coordinates)
        self.vector_visualization_list.append(vector_visualization)
        self.DrawVectorVisualization(vector_visualization)
        
    def DrawVectorVisualization(self, vector_visualization: VectorVisualizationModule.VectorVisualization):
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
            fill=Themes.theme_service.theme_current.primary_foreground_color,
            arrow='last',
            width=2,
            tags=self.canvas_tags_vector)

    def SetVectorVisualizationList(self, vector_visualization_list: list):
        self.vector_visualization_list = vector_visualization_list

        for vector_visualization in self.vector_visualization_list:
            self.DrawVectorVisualization(vector_visualization)

def InjectVisualizationService(injectedVisualizationService: VisualizationServiceModule.VisualizationService):
    global visualization_service
    visualization_service = injectedVisualizationService

visualization_service: VisualizationServiceModule.VisualizationService = None