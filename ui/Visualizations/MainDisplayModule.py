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

        # Render toolbar
        global visualization_toolbar_display
        if (visualization_toolbar_display != None):
            visualization_toolbar_display.__del__()        
        visualization_toolbar_display = ToolbarDisplayModule.ToolbarDisplay(parent)

        # Render canvas
        global visualization_canvas_display
        if (visualization_canvas_display != None):
            visualization_canvas_display.__del__()
        visualization_canvas_display = CanvasDisplayModule.CanvasDisplay(parent, root)

def InjectVisualizationService(injectedVisualizationService: VisualizationServiceModule.VisualizationService):
    global visualization_service
    visualization_service = injectedVisualizationService

visualization_toolbar_display: ToolbarDisplayModule.ToolbarDisplay = None
visualization_canvas_display: CanvasDisplayModule.CanvasDisplay = None
visualization_service: VisualizationServiceModule.VisualizationService = None