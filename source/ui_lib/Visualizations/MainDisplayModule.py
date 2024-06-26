import tkinter as tk
from class_lib.Themes.ThemeStateModule import ThemeState
from class_lib.States import StoreModule
from ui_lib.Visualizations.ToolbarDisplayModule import ToolbarDisplay
from ui_lib.Visualizations.CanvasDisplayModule import CanvasDisplay

class MainDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk, root: tk.Tk):

        theme_state = StoreModule.Get(ThemeState)

        super().__init__(
            parent,
            bg=theme_state.theme_current.primary_background_color,
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