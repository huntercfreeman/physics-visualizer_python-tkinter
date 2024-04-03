import tkinter as tk
from Themes.ThemeStateModule import ThemeState
from States import StoreModule

class HorizontalRuleDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk, anchor: str):

        theme_state = StoreModule.Get(ThemeState)

        super().__init__(parent, bg=theme_state.theme_current.primary_border_background_color, height=1)
        self.pack(side='top', anchor=anchor, fill='x')