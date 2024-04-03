import tkinter as tk
from varname import nameof
from Themes.ThemeStateModule import ThemeState
from Themes.ThemeModelModule import ThemeModel
from Dialogs.DialogModelModule import DialogModel
from Dialogs.DialogStateModule import DialogState
from States import StoreModule

class DialogDisplay(tk.Frame):
    def __init__(self, root: tk.Tk, dialog: DialogModel):
        
        theme_state: ThemeState = StoreModule.Get(ThemeState)
        
        super().__init__(root, bg=theme_state.theme_current.secondary_background_color)
        self.place(relx=.2, rely=0.2, relwidth=0.6, relheight=0.6)
        self.dialog = dialog

        DialogDisplay.TitleDisplay(self, dialog)

        label = tk.Label(
            self,
            text='Theme:',
            bg=theme_state.theme_current.secondary_background_color,
            fg=theme_state.theme_current.secondary_foreground_color)
        label.pack()

        def SetThemeOnClick(x_theme: ThemeModel):
            theme_state.SetTheme(x_theme)

        for loop_theme in theme_state.theme_list:

            bg = theme_state.theme_current.button_background_color
            fg = theme_state.theme_current.button_foreground_color

            if theme_state.theme_current == loop_theme:
                bg = theme_state.theme_current.button_active_background_color
                fg = theme_state.theme_current.button_active_foreground_color

            # Capture the theme from the 'for' iterations by creating a lambda within a lambda.
            button = tk.Button(
                self,
                text=loop_theme.display_name,
                bg=bg,
                fg=fg,
                command=(lambda x_theme: lambda: SetThemeOnClick(x_theme))(loop_theme))
            button.pack()

    class TitleDisplay(tk.Frame):
        def __init__(self, parent: tk.Tk, dialog: DialogModel):

            theme_state: ThemeState = StoreModule.Get(ThemeState)

            super().__init__(parent, bg=theme_state.theme_current.dialog_toolbar_background_color)
            self.pack(side='top', fill='both')
            # self.pack_propagate(tk.FALSE)

            label = tk.Label(
                self,
                text=dialog.display_name,
                bg=theme_state.theme_current.dialog_toolbar_background_color,
                fg=theme_state.theme_current.secondary_foreground_color)
            label.pack(side='left', fill='y')

            dialog_state: DialogState = StoreModule.Get(DialogState)

            close_button = tk.Button(
                self,
                text='x',
                bg=theme_state.theme_current.danger_background_color,
                fg=theme_state.theme_current.button_foreground_color,
                command=lambda: dialog_state.dispose_dialog(dialog.display_name))
            close_button.pack(side='right', fill='y')