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
        
        self.visualization_toolbar_display = ToolbarDisplayModule.ToolbarDisplay(parent)
        self.visualization_canvas_display = CanvasDisplayModule.CanvasDisplay(parent, root)

def InjectVisualizationService(injectedVisualizationService: VisualizationServiceModule.VisualizationService):
    global visualization_service
    visualization_service = injectedVisualizationService

visualization_service: VisualizationServiceModule.VisualizationService = None