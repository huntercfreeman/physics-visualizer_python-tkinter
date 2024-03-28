import tkinter as tk
import ThemeModule
import DialogModule
from varname import nameof

def InitializeLayoutModule(root: tk.Tk):
    global existing_root
    global app_header_display
    global app_body_display
    global app_footer_display

    existing_root = root

    app_header_display = AppHeaderDisplay(root)
    app_body_display = AppBodyDisplay(root)
    app_footer_display = AppFooterDisplay(root)

def DestroyLayoutModule():
    global existing_root
    global app_header_display
    global app_body_display
    global app_footer_display

    app_header_display.destroy()
    app_body_display.destroy()
    app_footer_display.destroy()

    InitializeLayoutModule(existing_root)

class AppHeaderDisplay(tk.Frame):
    """Render the 'header' aka: 'navigation bar', or 'toolbar'."""
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.header_background_color)
        self.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        self.pack_propagate(tk.FALSE)
        
        def show_settings_dialog():
            DialogModule.dialog_service.register_dialog("Settings")

        button = tk.Button(self, text="settings", command=show_settings_dialog)
        button.pack(side="left")

        label = tk.Label(
            self,
            text=nameof(AppHeaderDisplay),
            bg=ThemeModule.theme_current.header_background_color,
            fg=ThemeModule.theme_current.primary_foreground_color)
        label.pack(side="left")

class AppBodyDisplay(tk.Frame):
    """TODO: docstring"""
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.primary_background_color)
        self.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
        self.pack_propagate(tk.FALSE)

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
        self.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
        self.pack_propagate(tk.FALSE)
        
        label = tk.Label(
            self,
            text=nameof(AppFooterDisplay),
            bg=ThemeModule.theme_current.footer_background_color,
            fg=ThemeModule.theme_current.primary_foreground_color)
        label.pack()

existing_root: tk.Tk = None
app_header_display: AppHeaderDisplay = None
app_body_display: AppBodyDisplay = None
app_footer_display: AppFooterDisplay = None