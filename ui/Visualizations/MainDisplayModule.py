import tkinter as tk
import VisualizationServiceModule
import CanvasDisplayModule
import ToolbarDisplayModule
import Themes

class MainDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk, root: tk.Tk):
        super().__init__(
            parent,
            bg=Themes.theme_service.theme_current.primary_background_color,
            highlightthickness=0)
        
        # This is hacky: The toolbar is dependent on the canvas, yet both are UI pieces,
        # Better code would be: separate canvas into a model and a display,
        # such that the display can exist outside the UI
        self.visualization_canvas_display: CanvasDisplayModule.CanvasDisplay = None

        self.visualization_toolbar_display = ToolbarDisplayModule.ToolbarDisplay(parent, self)
        self.visualization_canvas_display = CanvasDisplayModule.CanvasDisplay(parent, root, self)

def InjectVisualizationService(injectedVisualizationService: VisualizationServiceModule.VisualizationService):
    global visualization_service
    visualization_service = injectedVisualizationService

visualization_service: VisualizationServiceModule.VisualizationService = None