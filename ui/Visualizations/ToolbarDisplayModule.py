import tkinter as tk
import VisualizationServiceModule
import VectorVisualizationModule
import Themes

class ToolbarDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk):
        super().__init__(
            parent,
            bg=Themes.theme_service.theme_current.visualization_toolbar_background_color,
            width="300")
        self.place(relx=0, rely=0, relwidth=0.15, relheight=1)
        self.pack_propagate(tk.FALSE)

        self.vector_visualization_label_list: list[tk.Label] = []

        label = tk.Label(
            self,
            text='Vectors:',
            bg=Themes.theme_service.theme_current.visualization_toolbar_background_color,
            fg=Themes.theme_service.theme_current.visualization_toolbar_foreground_color,
            font=("Monospace 20 underline"))
        label.pack()

        visualization_service.state_changed.addListener(self.Render)

        # Force initial rendering of the vectors
        self.Render()

    def Render(self):
        for label in self.vector_visualization_label_list:
            label.destroy()

        for vector_visualization in visualization_service.vector_visualization_list:
            label = tk.Label(
                self,
                # TODO: https://www.compart.com/en/unicode/U+0134
                #       Use the i-hat, j-hat, k-hat; characters
                text=f'{vector_visualization.components[0]}i,'
                     f'{vector_visualization.components[1]}j,'
                     f'{vector_visualization.coordinates[0]}x,'
                     f'{vector_visualization.coordinates[1]}y,',
                bg=Themes.theme_service.theme_current.visualization_toolbar_background_color,
                fg=Themes.theme_service.theme_current.visualization_toolbar_foreground_color,
                font=("Monospace", 18))
            label.pack()
            self.vector_visualization_label_list.append(label)

    def __del__(self):
        """The usage of '__del__()' can have some quirks as described in this link:
        https://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/."""

        local_visualization_service = visualization_service

        if local_visualization_service != None:
            if hasattr(local_visualization_service, 'state_changed'):
                if hasattr(local_visualization_service.state_changed, 'removeListener'):
                    local_visualization_service.state_changed.removeListener(self.Render)

        self.destroy()

def InjectVisualizationService(injectedVisualizationService: VisualizationServiceModule.VisualizationService):
    global visualization_service
    visualization_service = injectedVisualizationService

visualization_service: VisualizationServiceModule.VisualizationService = None