import tkinter as tk
import ThemeModule
from varname import nameof

def InitializeLayout(master):
    AppHeaderDisplay(master)
    AppBodyDisplay(master)
    AppFooterDisplay(master)

class AppHeaderDisplay(tk.Frame):
    """Render the 'header' aka: 'navigation bar', or 'toolbar'."""

    def __init__(self, parent):
        super().__init__(parent)
        
        text = tk.Text(self)
        text.insert(tk.INSERT, nameof(AppHeaderDisplay))
        text.pack()

        self["bg"]=ThemeModule.theme_current.background_color
        self.pack(side='top', fill='both', expand=tk.TRUE)

class AppBodyDisplay(tk.Frame):
    """TODO: docstring"""

    def __init__(self, parent):
        super().__init__(parent)

        text = tk.Text(self)
        text.insert(tk.INSERT, nameof(AppBodyDisplay))
        text.pack()

        self["bg"]=ThemeModule.theme_current.background_color
        self.pack(side='top', fill='both', expand=tk.TRUE)

class AppFooterDisplay(tk.Frame):
    """TODO: docstring"""

    def __init__(self, parent):
        super().__init__(parent)

        text = tk.Text(self)
        text.insert(tk.INSERT, nameof(AppFooterDisplay))
        text.pack()

        self["bg"]=ThemeModule.theme_current.background_color
        self.pack(side='top', fill='both', expand=tk.TRUE)