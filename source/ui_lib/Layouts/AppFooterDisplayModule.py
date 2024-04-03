import tkinter as tk
from varname import nameof
from class_lib.Layouts.LayoutStateModule import LayoutState
from class_lib.Themes.ThemeStateModule import ThemeState
from class_lib.Visualizations.VisualizationStateModule import VisualizationState
from class_lib.Visualizations.CoordinatesModelModule import CoordinatesModel
from class_lib.Vectors.VectorModelModule import VectorModel
from class_lib.Layouts.PanelModelModule import PanelModel
from class_lib.States import StoreModule
from ui_lib.Visualizations.CoordinatesEditorDisplayModule import CoordinatesEditorDisplay
from ui_lib.Visualizations.CircleFormDisplayModule import CircleFormDisplay 
from ui_lib.Vectors.VectorEditorDisplayModule import VectorEditorDisplay

class AppFooterDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):

        theme_state = StoreModule.Get(ThemeState)

        super().__init__(root, bg=theme_state.theme_current.footer_background_color)
        self.place(relx=0, rely=0.88, relwidth=1, relheight=0.12)
        self.pack_propagate(tk.FALSE)
        
        self.panel_model_active: PanelModel = None
        self.vector_editor_display: VectorEditorDisplay = None
        self.coordinates_editor_display: CoordinatesEditorDisplay= None
        self.circle_form_display: CircleFormDisplay = None
        self.tab_frame: tk.Frame = None
        self.form_frame: tk.Frame = None

        self.tab_active = nameof(self.vector_editor_display)

        visualization_state = StoreModule.Get(VisualizationState)
        visualization_state.state_changed.addListener(
            self.OnVisualizationState_StateChanged)

        self.Render()
        
    def Render(self):
        if self.panel_model_active != None:
            self.panel_model_active.destroy_func()

        if self.form_frame != None:
            self.form_frame.destroy()

        self.CreateTabFrame()

        theme_state = StoreModule.Get(ThemeState)

        self.form_frame = tk.Frame(
            self,
            bg=theme_state.theme_current.footer_background_color)
        self.form_frame.pack(side="top", fill="x")

        self.form_left_frame = tk.Frame(
            self.form_frame,
            bg=theme_state.theme_current.footer_background_color)
        self.form_left_frame.pack(side="left")
        
        self.form_right_frame = tk.Frame(
            self.form_frame,
            bg=theme_state.theme_current.footer_background_color)
        self.form_right_frame.pack(side="left", fill="both")
        
        visualization_state = StoreModule.Get(VisualizationState)

        if visualization_state.vector_visualization_target == None:
            def DrawVectorOnClick():
                try:
                    layout_state = StoreModule.Get(LayoutState)
                    
                    component_x = int(layout_state.vector_editor_x_string_var.get())
                    component_y = int(layout_state.vector_editor_y_string_var.get())

                    coordinate_x = int(layout_state.coordinates_editor_x_string_var.get())
                    coordinate_y = int(layout_state.coordinates_editor_y_string_var.get())

                    visualization_state = StoreModule.Get(VisualizationState)

                    visualization_state.DrawVector(
                        VectorModel([component_x, component_y]),
                        CoordinatesModel([coordinate_x, coordinate_y]))
                except ValueError:
                    print("some_variable did not contain a number!")

            self.button = tk.Button(
                self.form_left_frame,
                text="Draw Vector",
                bg=theme_state.theme_current.button_background_color,
                fg=theme_state.theme_current.button_foreground_color,
                command=DrawVectorOnClick)
            self.button.pack(side="top")
        else:
            def ApplyChangesOnClick():
                pass
            self.button = tk.Button(
                self.form_left_frame,
                text="Apply",
                bg=theme_state.theme_current.button_background_color,
                fg=theme_state.theme_current.button_foreground_color,
                command=ApplyChangesOnClick)
            self.button.pack(side="top")

            def CancelChangesOnClick():
                pass
            self.button = tk.Button(
                self.form_left_frame,
                text="Cancel",
                bg=theme_state.theme_current.danger_background_color,
                fg=theme_state.theme_current.button_foreground_color,
                command=CancelChangesOnClick)
            self.button.pack(side="top")

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

        theme_state = StoreModule.Get(ThemeState)

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
        visualization_state = StoreModule.Get(VisualizationState)

        self.vector_editor_display = VectorEditorDisplay(self.form_right_frame)
        self.coordinates_editor_display = CoordinatesEditorDisplay(self.form_right_frame)
    
    def DestroyVectorForm(self):
        if self.vector_editor_display != None:
            self.vector_editor_display.destroy()
            self.vector_editor_display = None

        if self.coordinates_editor_display != None:
            self.coordinates_editor_display.destroy()
            self.coordinates_editor_display = None

    def CreateCircleForm(self):
        self.circle_form_display = CircleFormDisplay(self.form_right_frame)

    def DestroyCircleForm(self):
        if self.circle_form_display != None:
            self.circle_form_display.destroy()
            self.circle_form_display = None

    def OnVisualizationState_StateChanged(self, *args):
        if len(args) > 0:
            if isinstance(args[0], VectorModel):
                self.Render()

    def destroy(self):
        self.__del__()
        super().destroy()

    def __del__(self):
        """The usage of '__del__()' can have some quirks as described in this link:
        https://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/."""
        
        local_visualization_state = StoreModule.Get(VisualizationState)

        if local_visualization_state != None:
            if hasattr(local_visualization_state, 'state_changed'):
                if hasattr(local_visualization_state.state_changed, 'removeListener'):
                    local_visualization_state.state_changed.removeListener(self.OnVisualizationState_StateChanged)
