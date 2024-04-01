import tkinter as tk
import Themes
import VisualizationServiceModule

class CircleFormDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=Themes.theme_service.theme_current.footer_background_color)

        label = tk.Label(
            self,
            text='CircleFormDisplay',
            bg=Themes.theme_service.theme_current.visualization_toolbar_background_color,
            fg=Themes.theme_service.theme_current.visualization_toolbar_foreground_color,
            font=("Monospace 20 underline"))
        label.pack()

def InjectVisualizationService(injectedVisualizationService: VisualizationServiceModule.VisualizationService):
    global visualization_service
    visualization_service = injectedVisualizationService

visualization_service: VisualizationServiceModule.VisualizationService = None