import tkinter as tk
from Themes.ThemeStateModule import ThemeState
from Dispatchers import StoreModule

class CircleFormDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):

        theme_state: ThemeState = StoreModule.Get(ThemeState())

        super().__init__(root, bg=theme_state.theme_current.footer_background_color)
        self.pack(side="left", fill="both", expand=1)

        label = tk.Label(
            self,
            text='CircleFormDisplay',
            bg=theme_state.theme_current.visualization_toolbar_background_color,
            fg=theme_state.theme_current.visualization_toolbar_foreground_color,
            font=("Monospace 20 underline"))
        label.pack()
