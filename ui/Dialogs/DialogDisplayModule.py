import tkinter as tk
import Themes
import Layouts
import DialogModelModule
import DialogServiceModule
from varname import nameof

class DialogDisplay(tk.Frame):
    def __init__(self, root: tk.Tk, dialog: DialogModelModule.DialogModel):
        super().__init__(root, bg=Themes.theme_service.theme_current.secondary_background_color)
        self.place(relx=.2, rely=0.2, relwidth=0.6, relheight=0.6)
        self.dialog = dialog

        DialogDisplay.TitleDisplay(self, dialog)

        label = tk.Label(
            self,
            text=nameof(DialogDisplay),
            bg=Themes.theme_service.theme_current.secondary_background_color,
            fg=Themes.theme_service.theme_current.secondary_foreground_color)
        label.pack()

        def SetThemeOnClick(x_theme: Themes.ThemeModelModule.ThemeModel):
            Themes.SetTheme(x_theme)

            Layouts.DestroyLayoutModule()
            Layouts.InitializeLayoutModule(Layouts.existing_root)

            dialog_service.DestroyDialogModule()
            dialog_service.InitializeDialogModule(dialog_service.existing_root)
            dialog_service.register_dialog("Settings")

        for loop_theme in Themes.theme_service.theme_list:
            # Capture the theme from the 'for' iterations by creating a lambda within a lambda.
            button = tk.Button(
                self,
                text=loop_theme.display_name,
                command=(lambda x_theme: lambda: SetThemeOnClick(x_theme))(loop_theme))
            button.pack()

    class TitleDisplay(tk.Frame):
        def __init__(self, parent: tk.Tk, dialog: DialogModelModule.DialogModel):
            super().__init__(parent, bg=Themes.theme_service.theme_current.dialog_toolbar_background_color)
            self.pack(side='top', fill='both')
            # self.pack_propagate(tk.FALSE)

            label = tk.Label(
                self,
                text=dialog.display_name,
                bg=Themes.theme_service.theme_current.dialog_toolbar_background_color,
                fg=Themes.theme_service.theme_current.secondary_foreground_color)
            label.pack(side='left', fill='y')

            close_button = tk.Button(
                self,
                text='x',
                bg='red', # Themes.theme_service.theme_current.secondary_background_color,
                fg=Themes.theme_service.theme_current.secondary_foreground_color,
                command=lambda: dialog_service.dispose_dialog(dialog.display_name))
            close_button.pack(side='right', fill='y')

def InjectDialogService(injectedDialogService: DialogServiceModule.DialogService):
    global dialog_service
    dialog_service = injectedDialogService

dialog_service: DialogServiceModule.DialogService = None