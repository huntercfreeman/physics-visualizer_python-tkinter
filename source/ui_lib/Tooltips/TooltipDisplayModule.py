import tkinter as tk
from States import StoreModule
from Themes.ThemeStateModule import ThemeState

class TooltipDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):

        theme_state = StoreModule.Get(ThemeState)

        super().__init__(root, bg=theme_state.theme_current.header_background_color)
        self.place(relx=0, rely=0, relwidth=1, relheight=0.08)
        self.pack_propagate(tk.FALSE)