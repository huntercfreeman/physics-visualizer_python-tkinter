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

    def register_dialog(self):
        DialogDisplay(self.root)

class DialogDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.secondary_background_color)
        self.place(relx=.2, rely=0.2, relwidth=0.6, relheight=0.6)

        DialogDisplay.TitleDisplay(self)

        label = tk.Label(
            self,
            text=nameof(DialogDisplay),
            bg=ThemeModule.theme_current.secondary_background_color,
            fg=ThemeModule.theme_current.secondary_foreground_color)
        label.pack()

    class TitleDisplay(tk.Frame):
        def __init__(self, root: tk.Tk):
            super().__init__(root, bg=ThemeModule.theme_current.secondary_background_color)
            self.pack()
            self.pack_propagate(tk.FALSE)

            label = tk.Label(
                self,
                text=nameof(DialogDisplay),
                bg=ThemeModule.theme_current.secondary_background_color,
                fg=ThemeModule.theme_current.secondary_foreground_color)
            label.pack()

# Create an instance of the 'DialogService()' class once the 'InitializeDynamicUi(...)' function is ran
dialog_service = None