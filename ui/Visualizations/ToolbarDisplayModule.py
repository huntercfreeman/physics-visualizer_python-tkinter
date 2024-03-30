import tkinter as tk
import VisualizationServiceModule
import Themes

class ToolbarDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk):
        super().__init__(
            parent,
            bg=Themes.theme_service.theme_current.visualization_toolbar_background_color,
            width="100")
        self.pack(side='left', fill='y')

        label = tk.Label(
            self,
            text='Vectors:',
            bg=Themes.theme_service.theme_current.visualization_toolbar_background_color,
            fg=Themes.theme_service.theme_current.visualization_toolbar_foreground_color)
        label.pack()

def InjectVisualizationService(injectedVisualizationService: VisualizationServiceModule.VisualizationService):
    global visualization_service
    visualization_service = injectedVisualizationService

visualization_service: VisualizationServiceModule.VisualizationService = None