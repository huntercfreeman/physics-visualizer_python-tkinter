import tkinter as tk
import ThemeModule
import DynamicUiModule
from varname import nameof

def InitializeLayout(root: tk.Tk):
    AppHeaderDisplay(root)
    AppBodyDisplay(root)
    AppFooterDisplay(root)

class AppHeaderDisplay(tk.Frame):
    """Render the 'header' aka: 'navigation bar', or 'toolbar'."""

    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.header_background_color)
        self.pack_propagate(tk.FALSE)
        self.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        
        def show_settings_dialog():
            DynamicUiModule.dialog_service.register_dialog()

        button = tk.Button(self, text="settings", command=show_settings_dialog)
        button.pack()

        label = tk.Label(
            self,
            text=nameof(AppHeaderDisplay),
            bg=ThemeModule.theme_current.header_background_color,
            fg=ThemeModule.theme_current.primary_foreground_color)
        label.pack()

class AppBodyDisplay(tk.Frame):
    """TODO: docstring"""

    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.primary_background_color)
        self.pack_propagate(tk.FALSE)
        self.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)

        label = tk.Label(
            self,
            text=nameof(AppBodyDisplay),
            bg=ThemeModule.theme_current.primary_background_color,
            fg=ThemeModule.theme_current.primary_foreground_color)
        label.pack()

class AppFooterDisplay(tk.Frame):
    """TODO: docstring"""

    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.footer_background_color)
        self.pack_propagate(tk.FALSE)
        self.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
        
        label = tk.Label(
            self,
            text=nameof(AppFooterDisplay),
            bg=ThemeModule.theme_current.footer_background_color,
            fg=ThemeModule.theme_current.primary_foreground_color)
        label.pack()
