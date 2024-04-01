import tkinter as tk
import LayoutServiceModule
import Themes
import Dialogs
from varname import nameof

def InjectLayoutService(injectedLayoutService: LayoutServiceModule.LayoutService):
    global layout_service
    layout_service = injectedLayoutService

class AppHeaderDisplay(tk.Frame):
    """Render the 'header' aka: 'navigation bar', or 'toolbar'."""
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=Themes.theme_service.theme_current.header_background_color)
        self.place(relx=0, rely=0, relwidth=1, relheight=0.08)
        self.pack_propagate(tk.FALSE)
        
        def show_settings_dialog():
            Dialogs.dialog_service.register_dialog("Settings")

        button = tk.Button(
            self,
            text="settings",
            bg=Themes.theme_service.theme_current.button_background_color,
            fg=Themes.theme_service.theme_current.button_foreground_color,
            command=show_settings_dialog)
        button.pack(side="left")

        label = tk.Label(
            self,
            text=nameof(AppHeaderDisplay),
            bg=Themes.theme_service.theme_current.header_background_color,
            fg=Themes.theme_service.theme_current.primary_foreground_color)
        label.pack(side="left")

def InjectLayoutService(injectedLayoutService: LayoutServiceModule.LayoutService):
    global layout_service
    layout_service = injectedLayoutService

layout_service: LayoutServiceModule.LayoutService = None