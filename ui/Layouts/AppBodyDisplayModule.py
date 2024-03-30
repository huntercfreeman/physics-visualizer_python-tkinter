import tkinter as tk
import LayoutServiceModule
import Themes
import Visualizations
import HorizontalRules

class AppBodyDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=Themes.theme_service.theme_current.primary_background_color)
        self.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
        self.pack_propagate(tk.FALSE)
        
        past_main_display = layout_service.main_display

        HorizontalRules.HorizontalRuleDisplay(self, anchor='n')

        layout_service.main_display = Visualizations.MainDisplay(self, root)

        if past_main_display != None:
            layout_service.main_display.visualization_canvas_display.SetVectorVisualizationList(
                past_main_display.visualization_canvas_display.vector_visualization_list)

        HorizontalRules.HorizontalRuleDisplay(self, anchor='s')

def InjectLayoutService(injectedLayoutService: LayoutServiceModule.LayoutService):
    global layout_service
    layout_service = injectedLayoutService

layout_service: LayoutServiceModule.LayoutService = None