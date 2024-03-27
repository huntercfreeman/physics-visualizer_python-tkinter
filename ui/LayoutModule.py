import tkinter as tk
from varname import nameof

class LayoutDisplay(tk.Frame):
    """Top level 'tkinter.Frame' for the application."""

    def __init__(self, parent):
        super().__init__(parent)
        
        AppHeaderDisplay(self)
        AppBodyDisplay(self)
        AppFooterDisplay(self)

        self.pack()

class AppHeaderDisplay(tk.Frame):
    """Render the 'header' aka: 'navigation bar', or 'toolbar'."""

    def __init__(self, parent):
        super().__init__(parent)
        
        text = tk.Text(self)
        text.insert(tk.INSERT, nameof(AppHeaderDisplay))
        text.pack()

        self.pack()

class AppBodyDisplay(tk.Frame):
    """TODO: docstring"""

    def __init__(self, parent):
        super().__init__(parent)

        text = tk.Text(self)
        text.insert(tk.INSERT, nameof(AppBodyDisplay))
        text.pack()

        self.pack()

class AppFooterDisplay(tk.Frame):
    """TODO: docstring"""

    def __init__(self, parent):
        super().__init__(parent)
        
        text = tk.Text(self)
        text.insert(tk.INSERT, nameof(AppFooterDisplay))
        text.pack()

        self.pack()