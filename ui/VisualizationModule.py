import tkinter as tk
import ThemeModule
from varname import nameof

class VisualizationDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk):
        super().__init__(parent, bg=ThemeModule.theme_current.primary_background_color)
        self.pack(side='top', fill='both')

        canvas = tk.Canvas(
            parent,
            bg=ThemeModule.theme_current.primary_background_color,
            highlightthickness=0)
        canvas.pack(expand=1, fill=tk.BOTH)