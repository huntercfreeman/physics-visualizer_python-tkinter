import tkinter as tk
from Themes.ThemeServiceModule import ThemeService
from Dispatchers import StoreModule

class HorizontalRuleDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk, anchor: str):

        theme_service: ThemeService = StoreModule.Get(ThemeService())

        super().__init__(parent, bg=theme_service.theme_current.primary_border_background_color, height=1)
        self.pack(side='top', anchor=anchor, fill='x')