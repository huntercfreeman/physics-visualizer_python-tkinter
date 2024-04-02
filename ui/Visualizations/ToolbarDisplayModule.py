import tkinter as tk
from VisualizationStateModule import VisualizationState
from Themes.ThemeStateModule import ThemeState
from Dispatchers import StoreModule

class ToolbarDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk):

        theme_state: ThemeState = StoreModule.Get(ThemeState())

        super().__init__(
            parent,
            bg=theme_state.theme_current.visualization_toolbar_background_color,
            width="300")
        self.place(relx=0, rely=0, relwidth=0.15, relheight=1)
        self.pack_propagate(tk.FALSE)

        self.vector_visualization_label_list: list[tk.Label] = []

        label = tk.Label(
            self,
            text='Vectors:',
            bg=theme_state.theme_current.visualization_toolbar_background_color,
            fg=theme_state.theme_current.visualization_toolbar_foreground_color,
            font=("Monospace 20 underline"))
        label.pack()

        visualization_state: VisualizationState = StoreModule.Get(VisualizationState())
        visualization_state.state_changed.addListener(self.OnVisualizationState_StateChanged)

        # Force initial rendering of the vectors
        self.Render()

    def Render(self):
        for label in self.vector_visualization_label_list:
            label.destroy()

        visualization_state: VisualizationState = StoreModule.Get(VisualizationState())
        theme_state: ThemeState = StoreModule.Get(ThemeState())

        for i,vector_visualization in enumerate(visualization_state.vector_visualization_list):
            def SetVectorEditorTargetOnClick(vector_visualization):
                visualization_state.vector_editor_target

            label = tk.Label(
                self,
                text='('
                     f'{vector_visualization.components[0]}, '
                     f'{vector_visualization.components[1]}'
                     ')',
                bg=theme_state.theme_current.visualization_toolbar_background_color,
                fg=theme_state.theme_current.visualization_toolbar_foreground_color,
                font=("Monospace", 18))
            label.bind("<Button-1>",lambda e,vector_visualization=vector_visualization:SetVectorEditorTargetOnClick(vector_visualization))
            label.pack()

            self.vector_visualization_label_list.append(label)

    def OnVisualizationState_StateChanged(self, *args):
        self.Render()

    def __del__(self):
        """The usage of '__del__()' can have some quirks as described in this link:
        https://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/."""

        visualization_state: VisualizationState = StoreModule.Get(VisualizationState())
        local_visualization_state = visualization_state

        if local_visualization_state != None:
            if hasattr(local_visualization_state, 'state_changed'):
                if hasattr(local_visualization_state.state_changed, 'removeListener'):
                    local_visualization_state.state_changed.removeListener(self.OnVisualizationState_StateChanged)

        self.destroy()
