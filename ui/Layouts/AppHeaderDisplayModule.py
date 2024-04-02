import tkinter as tk
from Themes.ThemeStateModule import ThemeState
from Dialogs.DialogStateModule import DialogState
from Dispatchers import StoreModule

class AppHeaderDisplay(tk.Frame):
    """Render the 'header' aka: 'navigation bar', or 'toolbar'."""
    def __init__(self, root: tk.Tk):

        theme_state: ThemeState = StoreModule.Get(ThemeState())

        super().__init__(root, bg=theme_state.theme_current.header_background_color)
        self.place(relx=0, rely=0, relwidth=1, relheight=0.08)
        self.pack_propagate(tk.FALSE)
        
        dialog_state: DialogState = StoreModule.Get(DialogState())

        def show_settings_dialog():
            dialog_state.register_dialog("Settings")

        button = tk.Button(
            self,
            text="settings",
            bg=theme_state.theme_current.button_background_color,
            fg=theme_state.theme_current.button_foreground_color,
            command=show_settings_dialog)
        button.pack(side="left")
