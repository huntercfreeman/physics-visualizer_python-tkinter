import tkinter as tk
from VisualizationStateModule import VisualizationState
from VectorVisualizationModule import VectorVisualization
from Themes.ThemeStateModule import ThemeState
from Dispatchers import StoreModule

class CanvasDisplay(tk.Canvas):
    def __init__(self, parent: tk.Tk, root: tk.Tk):

        theme_state: ThemeState = StoreModule.Get(ThemeState())

        super().__init__(
            parent,
            bg=theme_state.theme_current.primary_background_color,
            highlightthickness=0)
        self.place(relx=0.15, rely=0, relwidth=0.85, relheight=1)
        self.pack_propagate(tk.FALSE)

        self.root = root
        
        self.update()
        self.InitializeCoordinateSystem()

        visualization_state: VisualizationState = StoreModule.Get(VisualizationState())
        
        visualization_state.state_changed.addListener(self.OnVisualizationState_StateChanged)

        # Force initial rendering of the vectors
        self.Render()

    def InitializeCoordinateSystem(self):
        self.canvas_tags_axis_y = "axis_y"
        self.canvas_tags_axis_x = "axis_x"
        self.canvas_tags_vector = "vector"

        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()

        width_midpoint = canvas_width / 2.0
        height_midpoint = canvas_height / 2.0
        
        theme_state: ThemeState = StoreModule.Get(ThemeState())

        def InitializeAxisX():
            # Create the axis itself
            self.create_line(
                0,
                height_midpoint,
                canvas_width,
                height_midpoint,
                fill=theme_state.theme_current.coordinate_system_axis_fill_color,
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
                    fill=theme_state.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    tick_pos_x,
                    height_midpoint + tick_height + height_of_text,
                    text=f'{int(offset)}',
                    fill=theme_state.theme_current.coordinate_system_axis_fill_color)

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
                    fill=theme_state.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    tick_pos_x,
                    height_midpoint + tick_height + height_of_text,
                    text=f'{int(offset)}',
                    fill=theme_state.theme_current.coordinate_system_axis_fill_color)
        InitializeAxisX()

        def InitializeAxisY():
            # Create the axis itself
            self.create_line(
                width_midpoint,
                0,
                width_midpoint,
                canvas_height,
                fill=theme_state.theme_current.coordinate_system_axis_fill_color,
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
                    fill=theme_state.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    width_midpoint + tick_width + text_offset,
                    tick_pos_y,
                    text=f'{int(offset)}',
                    fill=theme_state.theme_current.coordinate_system_axis_fill_color)
                
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
                    fill=theme_state.theme_current.coordinate_system_axis_fill_color,
                    tags=self.canvas_tags_axis_x)
                self.create_text(
                    width_midpoint + tick_width + text_offset,
                    tick_pos_y,
                    text=f'{int(offset)}',
                    fill=theme_state.theme_current.coordinate_system_axis_fill_color)
        InitializeAxisY()

    def Render(self):
        self.delete(self.canvas_tags_vector)

        visualization_state: VisualizationState = StoreModule.Get(VisualizationState())
        
        for vector_visualization in visualization_state.vector_visualization_list:
            self.DrawVectorVisualization(vector_visualization)

    def DrawVectorVisualization(self, vector_visualization: VectorVisualization):
        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()

        canvas_width_halfway = canvas_width / 2.0
        canvas_height_halfway = canvas_height / 2.0

        initial_x = canvas_width_halfway + vector_visualization.coordinates[0]
        initial_y = canvas_height_halfway - vector_visualization.coordinates[1]

        theme_state: ThemeState = StoreModule.Get(ThemeState())

        self.create_line(
            initial_x,
            initial_y,
            initial_x + vector_visualization.components[0],
            initial_y + (-1 * vector_visualization.components[1]),
            fill=theme_state.theme_current.primary_foreground_color,
            arrow='last',
            width=2,
            tags=self.canvas_tags_vector)
        
    def OnVisualizationState_StateChanged(self, *args):
        self.Render()
        
    def __del__(self):
        """The usage of '__del__()' can have some quirks as described in this link:
        https://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/."""

        visualization_state: VisualizationState = StoreModule.Get(VisualizationState())
        
        local_visualization_state = visualization_state

        if local_visualization_state != None:
            if hasattr(local_visualization_state, 'state_changed'):
                if hasattr(local_visualization_state.state_changed, 'removeListener'):
                    local_visualization_state.state_changed.removeListener(self.OnVisualizationState_StateChanged)

        self.destroy()
