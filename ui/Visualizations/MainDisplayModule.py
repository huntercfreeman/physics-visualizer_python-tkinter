import tkinter as tk
from CanvasDisplayModule import CanvasDisplay
from ToolbarDisplayModule import ToolbarDisplay
from Themes.ThemeServiceModule import theme_service

class MainDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk, root: tk.Tk):
        super().__init__(
            parent,
            bg=theme_service.theme_current.primary_background_color,
            highlightthickness=0)

        # Render toolbar
        global visualization_toolbar_display
        if (visualization_toolbar_display != None):
            visualization_toolbar_display.__del__()        
        visualization_toolbar_display = ToolbarDisplay(parent)

        # Render canvas
        global visualization_canvas_display
        if (visualization_canvas_display != None):
            visualization_canvas_display.__del__()
        visualization_canvas_display = CanvasDisplay(parent, root)

visualization_toolbar_display: ToolbarDisplay = None
visualization_canvas_display: CanvasDisplay = None