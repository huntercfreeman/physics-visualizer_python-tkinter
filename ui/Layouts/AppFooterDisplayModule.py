import tkinter as tk
from varname import nameof
from Layouts.LayoutStateModule import LayoutState
from Themes.ThemeStateModule import ThemeState
from Visualizations.VisualizationStateModule import VisualizationState
from Visualizations.CoordinatesModelModule import CoordinatesModel
from Visualizations.CoordinatesEditorDisplayModule import CoordinatesEditorDisplay
from Visualizations.CircleFormDisplayModule import CircleFormDisplay 
from Vectors.VectorEditorDisplayModule import VectorEditorDisplay
from Vectors.VectorModelModule import VectorModel
from Layouts.PanelModelModule import PanelModel
from States import StoreModule

class AppFooterDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):

        theme_state: ThemeState = StoreModule.Get(ThemeState)

        super().__init__(root, bg=theme_state.theme_current.footer_background_color)
        self.place(relx=0, rely=0.88, relwidth=1, relheight=0.12)
        self.pack_propagate(tk.FALSE)
        
        self.panel_model_active: PanelModel = None
        self.vector_editor_display: VectorEditorDisplay = None
        self.coordinates_editor_display: CoordinatesEditorDisplay= None
        self.circle_form_display: CircleFormDisplay = None
        self.tab_frame: tk.Frame = None
        self.button: tk.Button = None

        self.tab_active = nameof(self.vector_editor_display)

        visualization_state: VisualizationState = StoreModule.Get(VisualizationState)
        visualization_state.state_changed.addListener(
            self.OnVisualizationState_StateChanged)

        self.Render()
        
    def Render(self):
        if self.panel_model_active != None:
            self.panel_model_active.destroy_func()

        if self.button != None:
            self.button.destroy()

        self.CreateTabFrame()

        theme_state: ThemeState = StoreModule.Get(ThemeState)

        def SubmitFormOnClick():
            try:
                layout_state: LayoutState = StoreModule.Get(LayoutState)
                
                component_x = int(layout_state.vector_editor_x_string_var.get())
                component_y = int(layout_state.vector_editor_y_string_var.get())

                coordinate_x = int(layout_state.coordinates_editor_x_string_var.get())
                coordinate_y = int(layout_state.coordinates_editor_y_string_var.get())

                visualization_state: VisualizationState = StoreModule.Get(VisualizationState)

                visualization_state.AddVector(
                    VectorModel([component_x, component_y]),
                    CoordinatesModel([coordinate_x, coordinate_y]))
            except ValueError:
                print("some_variable did not contain a number!")
        
        self.button = tk.Button(
            self,
            text="New Vector",
            bg=theme_state.theme_current.button_background_color,
            fg=theme_state.theme_current.button_foreground_color,
            command=SubmitFormOnClick)
        self.button.pack(side="left")

        if self.tab_active == nameof(self.vector_editor_display):
            self.panel_model_active = PanelModel(
                self.CreateVectorForm,
                self.DestroyVectorForm)
        else:
            self.panel_model_active = PanelModel(
                self.CreateCircleForm,
                self.DestroyCircleForm)
            
        self.panel_model_active.create_func()

    def CreateTabFrame(self):
        if self.tab_frame != None:
            self.tab_frame.destroy()

        self.tab_frame = tk.Frame(self)
        self.tab_list: list[str] = (nameof(self.vector_editor_display), nameof(self.circle_form_display))

        theme_state: ThemeState = StoreModule.Get(ThemeState)

        for tab in self.tab_list:
            is_active = tab == self.tab_active

            bg = theme_state.theme_current.button_background_color
            if is_active: bg = theme_state.theme_current.button_active_background_color

            fg = theme_state.theme_current.button_foreground_color
            if is_active: fg = theme_state.theme_current.button_active_foreground_color
            
            button = tk.Button(
                self.tab_frame,
                text=tab,
                bg=bg,
                fg=fg,
                command=(lambda t: lambda: self.SetActiveTab(t))(tab))
            button.pack(side="left")

        self.tab_frame.pack(side="top")

    def SetActiveTab(self, tab):
        self.tab_active = tab
        self.Render()

    def CreateVectorForm(self):
        visualization_state: VisualizationState = StoreModule.Get(VisualizationState)

        self.vector_editor_display = VectorEditorDisplay(self, visualization_state.vector_editor_target)
        self.coordinates_editor_display = CoordinatesEditorDisplay(self, visualization_state.coordinates_editor_target)
    
    def DestroyVectorForm(self):
        if self.vector_editor_display != None:
            self.vector_editor_display.destroy()
            self.vector_editor_display = None

        if self.coordinates_editor_display != None:
            self.coordinates_editor_display.destroy()
            self.coordinates_editor_display = None

    def CreateCircleForm(self):
        self.circle_form_display = CircleFormDisplay(self)

    def DestroyCircleForm(self):
        if self.circle_form_display != None:
            self.circle_form_display.destroy()
            self.circle_form_display = None

    def OnVisualizationState_StateChanged(self, *args):
        if len(args) > 0:
            if isinstance(args[0], VectorModel):
                self.Render()

    def __del__(self):
        """The usage of '__del__()' can have some quirks as described in this link:
        https://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/."""
        
        visualization_state: VisualizationState = StoreModule.Get(VisualizationState)

        local_visualization_state = visualization_state

        if local_visualization_state != None:
            if hasattr(local_visualization_state, 'state_changed'):
                if hasattr(local_visualization_state.state_changed, 'removeListener'):
                    local_visualization_state.state_changed.removeListener(self.OnVisualizationState_StateChanged)
