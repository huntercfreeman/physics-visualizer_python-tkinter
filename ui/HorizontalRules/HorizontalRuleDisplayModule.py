import tkinter as tk
import Themes

class HorizontalRuleDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk, anchor: str):
        super().__init__(parent, bg=Themes.theme_service.theme_current.primary_border_background_color, height=1)
        self.pack(side='top', anchor=anchor, fill='x')