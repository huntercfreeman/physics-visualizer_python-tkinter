import tkinter as tk
import ThemeModule
from varname import nameof

def InitializeLayout(master):
    rowIndex = 0

    AppHeaderDisplay(master, rowIndex)
    rowIndex += 1

    AppBodyDisplay(master, rowIndex)
    rowIndex += 1

    AppFooterDisplay(master, rowIndex)
    rowIndex += 1

class AppHeaderDisplay(tk.Frame):
    """Render the 'header' aka: 'navigation bar', or 'toolbar'."""

    def __init__(self, master, rowIndex):
        super().__init__(master)
        
        text = tk.Text(self)
        text.insert(tk.INSERT, nameof(AppHeaderDisplay))
        text.pack()

        self["bg"]=ThemeModule.theme_current.background_color
        self.grid(row=rowIndex, column=0, sticky='nsew')

class AppBodyDisplay(tk.Frame):
    """TODO: docstring"""

    def __init__(self, master, rowIndex):
        super().__init__(master)

        text = tk.Text(self)
        text.insert(tk.INSERT, nameof(AppBodyDisplay))
        text.pack()

        self["bg"]=ThemeModule.theme_current.background_color
        self.grid(row=rowIndex, column=0, sticky='nsew')

class AppFooterDisplay(tk.Frame):
    """TODO: docstring"""

    def __init__(self, master, rowIndex):
        super().__init__(master)

        text = tk.Text(self)
        text.insert(tk.INSERT, nameof(AppFooterDisplay))
        text.pack()

        self["bg"]=ThemeModule.theme_current.background_color
        self.grid(row=rowIndex, column=0, sticky='nsew')