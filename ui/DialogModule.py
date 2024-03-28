import tkinter as tk
import ThemeModule
from varname import nameof

def InitializeDialog(root: tk.Tk):
    global dialog_service
    dialog_service = DialogService(root)

class DialogService:
    """Provides API to render a dialog"""
    def __init__(self, root: tk.Tk):
        self.root = root
        self.dialog_map = {}

    def register_dialog(self, display_name: str):
        if display_name not in self.dialog_map:
            self.dialog_map[display_name] = DialogDisplay(self.root, display_name)
    
    def dispose_dialog(self, display_name: str):
        if display_name in self.dialog_map:
            self.dialog_map[display_name].destroy()
            del self.dialog_map[display_name]
        
class DialogDisplay(tk.Frame):
    def __init__(self, root: tk.Tk, display_name: str):
        super().__init__(root, bg=ThemeModule.theme_current.secondary_background_color)
        self.place(relx=.2, rely=0.2, relwidth=0.6, relheight=0.6)
        self.display_name = display_name

        DialogDisplay.TitleDisplay(self, display_name)

        label = tk.Label(
            self,
            text=nameof(DialogDisplay),
            bg=ThemeModule.theme_current.secondary_background_color,
            fg=ThemeModule.theme_current.secondary_foreground_color)
        label.pack()

    class TitleDisplay(tk.Frame):
        def __init__(self, parent: tk.Tk, display_name: str):
            super().__init__(parent, bg=ThemeModule.theme_current.dialog_toolbar_background_color)
            self.pack(side='top', fill='both')
            # self.pack_propagate(tk.FALSE)

            label = tk.Label(
                self,
                text=display_name,
                bg=ThemeModule.theme_current.dialog_toolbar_background_color,
                fg=ThemeModule.theme_current.secondary_foreground_color)
            label.pack(side='left', fill='y')

            close_button = tk.Button(
                self,
                text='x',
                bg='red', # ThemeModule.theme_current.secondary_background_color,
                fg=ThemeModule.theme_current.secondary_foreground_color,
                command=lambda: dialog_service.dispose_dialog(display_name))
            close_button.pack(side='right', fill='y')

# Create an instance of the 'DialogService()' class once the 'InitializeDynamicUi(...)' function is ran
dialog_service = None