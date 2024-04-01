import tkinter as tk
import LayoutServiceModule
import Themes
import Visualizations
import HorizontalRules

class AppBodyDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=Themes.theme_service.theme_current.primary_background_color)
        self.place(relx=0, rely=0.08, relwidth=1, relheight=0.8)
        self.pack_propagate(tk.FALSE)
        
        HorizontalRules.HorizontalRuleDisplayModule.HorizontalRuleDisplay(self, anchor='n')

        main_display = Visualizations.MainDisplayModule.MainDisplay(self, root)

        HorizontalRules.HorizontalRuleDisplayModule.HorizontalRuleDisplay(self, anchor='s')

def InjectLayoutService(injectedLayoutService: LayoutServiceModule.LayoutService):
    global layout_service
    layout_service = injectedLayoutService

layout_service: LayoutServiceModule.LayoutService = None