import tkinter as tk
import LayoutServiceModule
import Themes
import Visualizations
import Vectors
import PanelModelModule
from varname import nameof

class AppFooterDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=Themes.theme_service.theme_current.footer_background_color)
        self.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
        self.pack_propagate(tk.FALSE)
        
        self.panel_model_active: PanelModelModule.PanelModel = None
        self.vector_editor_display: Vectors.VectorEditorDisplayModule.VectorEditorDisplay = None
        self.coordinates_editor_display: Visualizations.CoordinatesEditorDisplayModule.CoordinatesEditorDisplay= None
        self.circle_form_display: Visualizations.CircleFormDisplayModule.CircleFormDisplay = None
        self.tab_frame: tk.Frame = None
        self.button: tk.Button = None

        self.tab_active = nameof(self.vector_editor_display)

        self.Render()
        
    def Render(self):
        if self.panel_model_active != None:
            self.panel_model_active.destroy_func()

        if self.button != None:
            self.button.destroy()

        self.CreateTabFrame()

        def SubmitFormOnClick():
            try:
                component_x = int(layout_service.vector_editor_x_string_var.get())
                component_y = int(layout_service.vector_editor_y_string_var.get())

                coordinate_x = int(layout_service.coordinates_editor_x_string_var.get())
                coordinate_y = int(layout_service.coordinates_editor_y_string_var.get())

                Visualizations.visualization_service.AddVector(
                    Vectors.VectorModelModule.VectorModel([component_x, component_y]),
                    Visualizations.CoordinatesVisualizationModule.CoordinatesVisualization([coordinate_x, coordinate_y]))
            except ValueError:
                print("some_variable did not contain a number!")
        self.button = tk.Button(self, text="New Vector", command=SubmitFormOnClick)
        self.button.pack(side="left")

        if self.tab_active == nameof(self.vector_editor_display):
            self.panel_model_active = PanelModelModule.PanelModel(
                self.CreateVectorForm,
                self.DestroyVectorForm)
        else:
            self.panel_model_active = PanelModelModule.PanelModel(
                self.CreateCircleForm,
                self.DestroyCircleForm)
            
        self.panel_model_active.create_func()

    def CreateTabFrame(self):
        if self.tab_frame != None:
            self.tab_frame.destroy()

        self.tab_frame = tk.Frame(self)
        self.tab_list: list[str] = (nameof(self.vector_editor_display), nameof(self.circle_form_display))

        for tab in self.tab_list:
            print(tab + '==' + self.tab_active)

            is_active = tab == self.tab_active
            active_styling = ''
            
            if is_active: active_styling += 'red'
            else: active_styling += 'blue'

            button = tk.Button(
                self.tab_frame,
                text=tab,
                bg=active_styling,
                command=(lambda t: lambda: self.SetActiveTab(t))(tab))
            button.pack(side="left")

        self.tab_frame.pack(side="top")

    def SetActiveTab(self, tab):
        self.tab_active = tab
        self.Render()

    def CreateVectorForm(self):
        self.vector_editor_display = Vectors.VectorEditorDisplayModule.VectorEditorDisplay(self, Vectors.VectorModelModule.VectorModel([50, 50]))
        self.coordinates_editor_display = Visualizations.CoordinatesEditorDisplayModule.CoordinatesEditorDisplay(self, Visualizations.CoordinatesVisualizationModule.CoordinatesVisualization([0, 0]))
    
    def DestroyVectorForm(self):
        if self.vector_editor_display != None:
            self.vector_editor_display.destroy()
            self.vector_editor_display = None

        if self.coordinates_editor_display != None:
            self.coordinates_editor_display.destroy()
            self.coordinates_editor_display = None

    def CreateCircleForm(self):
        self.circle_form_display = Visualizations.CircleFormDisplayModule.CircleFormDisplay(self)

    def DestroyCircleForm(self):
        if self.circle_form_display != None:
            self.circle_form_display.destroy()
            self.circle_form_display = None

def InjectLayoutService(injectedLayoutService: LayoutServiceModule.LayoutService):
    global layout_service
    layout_service = injectedLayoutService

layout_service: LayoutServiceModule.LayoutService = None
