import tkinter as tk
import ThemeModule
from varname import nameof

class HorizontalRuleDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk, anchor: str):
        super().__init__(parent, bg=ThemeModule.theme_current.primary_border_background_color, height=1)
        self.pack(side='top', anchor=anchor, expand=1, fill='x')