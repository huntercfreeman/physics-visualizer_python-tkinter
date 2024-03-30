import tkinter as tk
import LayoutServiceModule
import Themes
import Visualizations
import Vectors

class AppFooterDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=Themes.theme_service.theme_current.footer_background_color)
        self.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
        self.pack_propagate(tk.FALSE)

        def SubmitFormOnClick():
            try:
                component_x = int(layout_service.vector_editor_display.x_string_var.get())
                component_y = int(layout_service.vector_editor_display.y_string_var.get())

                coordinate_x = int(layout_service.coordinates_editor_display.x_string_var.get())
                coordinate_y = int(layout_service.coordinates_editor_display.y_string_var.get())

                layout_service.main_display.visualization_canvas_display.AddVector(
                    Vectors.VectorModel([component_x, component_y]),
                    Visualizations.CoordinatesVisualization([coordinate_x, coordinate_y]))
            except ValueError:
                print("some_variable did not contain a number!")
        button = tk.Button(self, text="New Vector", command=SubmitFormOnClick)
        button.pack(side="left")
        
        vector_editor_display = Vectors.VectorEditorDisplayModule.VectorEditorDisplay(self, Vectors.VectorModelModule.VectorModel([50, 50]))
        coordinates_editor_display = Visualizations.CoordinatesEditorDisplayModule.CoordinatesEditorDisplay(self, Visualizations.CoordinatesVisualizationModule.CoordinatesVisualization([0, 0]))

def InjectLayoutService(injectedLayoutService: LayoutServiceModule.LayoutService):
    global layout_service
    layout_service = injectedLayoutService

layout_service: LayoutServiceModule.LayoutService = None
