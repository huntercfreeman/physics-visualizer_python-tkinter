import tkinter as tk
import ThemeModule
from varname import nameof

def InitializeLayout(root: tk.Tk):
    AppHeaderDisplay(root)
    AppBodyDisplay(root)
    AppFooterDisplay(root)

class AppHeaderDisplay(tk.Frame):
    """Render the 'header' aka: 'navigation bar', or 'toolbar'."""

    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.primary_background_color)
        self.pack_propagate(tk.FALSE)
        self.place(relx=0, rely=0, relwidth=1, relheight=0.2)
        
        button = tk.Button(self, text="settings")
        button.pack()

        label = tk.Label(
            self,
            text=nameof(AppHeaderDisplay),
            bg=ThemeModule.theme_current.primary_background_color,
            fg=ThemeModule.theme_current.primary_foreground_color)
        label.pack()

class AppBodyDisplay(tk.Frame):
    """TODO: docstring"""

    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.primary_background_color)
        self.pack_propagate(tk.FALSE)
        self.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

        label = tk.Label(
            self,
            text=nameof(AppBodyDisplay),
            bg=ThemeModule.theme_current.primary_background_color,
            fg=ThemeModule.theme_current.primary_foreground_color)
        label.pack()

class AppFooterDisplay(tk.Frame):
    """TODO: docstring"""

    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.primary_background_color)
        self.pack_propagate(tk.FALSE)
        self.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)
        
        label = tk.Label(
            self,
            text=nameof(AppFooterDisplay),
            bg=ThemeModule.theme_current.primary_background_color,
            fg=ThemeModule.theme_current.primary_foreground_color)
        label.pack()
        