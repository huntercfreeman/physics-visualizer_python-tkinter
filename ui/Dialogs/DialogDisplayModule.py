import tkinter as tk
from varname import nameof
from Themes.ThemeServiceModule import ThemeService
from Themes.ThemeModelModule import ThemeModel
from DialogModelModule import DialogModel
from DialogServiceModule import DialogService
from Dispatchers import StoreModule

class DialogDisplay(tk.Frame):
    def __init__(self, root: tk.Tk, dialog: DialogModel):
        
        theme_service: ThemeService = StoreModule.Get(ThemeService())
        
        super().__init__(root, bg=theme_service.theme_current.secondary_background_color)
        self.place(relx=.2, rely=0.2, relwidth=0.6, relheight=0.6)
        self.dialog = dialog

        DialogDisplay.TitleDisplay(self, dialog)

        label = tk.Label(
            self,
            text=nameof(DialogDisplay),
            bg=theme_service.theme_current.secondary_background_color,
            fg=theme_service.theme_current.secondary_foreground_color)
        label.pack()

        def SetThemeOnClick(x_theme: ThemeModel):
            theme_service.SetTheme(x_theme)

        for loop_theme in theme_service.theme_list:
            # Capture the theme from the 'for' iterations by creating a lambda within a lambda.
            button = tk.Button(
                self,
                text=loop_theme.display_name,
                bg=theme_service.theme_current.button_background_color,
                fg=theme_service.theme_current.button_foreground_color,
                command=(lambda x_theme: lambda: SetThemeOnClick(x_theme))(loop_theme))
            button.pack()

    class TitleDisplay(tk.Frame):
        def __init__(self, parent: tk.Tk, dialog: DialogModel):

            theme_service: ThemeService = StoreModule.Get(ThemeService())

            super().__init__(parent, bg=theme_service.theme_current.dialog_toolbar_background_color)
            self.pack(side='top', fill='both')
            # self.pack_propagate(tk.FALSE)

            label = tk.Label(
                self,
                text=dialog.display_name,
                bg=theme_service.theme_current.dialog_toolbar_background_color,
                fg=theme_service.theme_current.secondary_foreground_color)
            label.pack(side='left', fill='y')

            dialog_service: DialogService = StoreModule.Get(DialogService())

            close_button = tk.Button(
                self,
                text='x',
                bg=theme_service.theme_current.danger_background_color,
                fg=theme_service.theme_current.button_foreground_color,
                command=lambda: dialog_service.dispose_dialog(dialog.display_name))
            close_button.pack(side='right', fill='y')