import tkinter as tk
from LayoutServiceModule import LayoutService
from Themes import theme_service
from Dialogs import dialog_service

class AppHeaderDisplay(tk.Frame):
    """Render the 'header' aka: 'navigation bar', or 'toolbar'."""
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=theme_service.theme_current.header_background_color)
        self.place(relx=0, rely=0, relwidth=1, relheight=0.08)
        self.pack_propagate(tk.FALSE)
        
        def show_settings_dialog():
            dialog_service.register_dialog("Settings")

        button = tk.Button(
            self,
            text="settings",
            bg=theme_service.theme_current.button_background_color,
            fg=theme_service.theme_current.button_foreground_color,
            command=show_settings_dialog)
        button.pack(side="left")

def InjectLayoutService(injectedLayoutService: LayoutService):
    global layout_service
    layout_service = injectedLayoutService
    
layout_service: LayoutService = None