import tkinter as tk
from class_lib.Themes.ThemeStateModule import ThemeState
from class_lib.States import StoreModule
from ui_lib.Visualizations.MainDisplayModule import MainDisplay
from ui_lib.HorizontalRules.HorizontalRuleDisplayModule import HorizontalRuleDisplay

class AppBodyDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):

        theme_state = StoreModule.Get(ThemeState)
        
        super().__init__(root, bg=theme_state.theme_current.primary_background_color)
        self.place(relx=0, rely=0.08, relwidth=1, relheight=0.8)
        self.pack_propagate(tk.FALSE)
        
        HorizontalRuleDisplay(self, anchor='n')
        main_display = MainDisplay(self, root)
        HorizontalRuleDisplay(self, anchor='s')
