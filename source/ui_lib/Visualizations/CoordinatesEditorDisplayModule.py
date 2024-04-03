import tkinter as tk
from class_lib.Visualizations.VisualizationStateModule import VisualizationState
from class_lib.Visualizations.CoordinatesModelModule import CoordinatesModel
from class_lib.Themes.ThemeStateModule import ThemeState
from class_lib.Layouts.LayoutStateModule import LayoutState
from class_lib.States import StoreModule

class CoordinatesEditorDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk):
        """
        Constructor takes an existing coordinates object, or 'None'.
        
        If provided an existing coordinates object, then map the coordinate's attributes
        to the corresponding editor's attributes. The form is populated with the provided
        coordinates object's attributes, however, the provided coordinates object is treated as immutable.

        If provided 'None', then the editor's attributes are set to their type's default value.

        No submit button is provided, one must make their own.

        Completion of the form is expected to be done in the following way:
            -Read the attributes on the editor class.
            -Pass these attributes to the coordinates object constructor.
            -The user of this form can check the 'self.coordinates' attribute on this class
                to determine whether an update, or creation is being performed.
                -If 'self.coordinates' is 'None', then a creation is being performed
                -If 'self.coordinates' has a coordinates object instance, then an update is
                    being performed.
                    -To update, one can either overwrite the existing coordinates object
                        or construct a new coordinates object.
        """

        theme_state = StoreModule.Get(ThemeState)

        super().__init__(parent, bg=theme_state.theme_current.footer_background_color)
        self.pack(side="left", fill="both", expand=1)

        visualization_state = StoreModule.Get(VisualizationState)
        visualization_state.state_changed.addListener(self.OnVisualizationState_StateChanged)

        self.coordinates: CoordinatesModel = None

        layout_state = StoreModule.Get(LayoutState)

        layout_state.coordinates_editor_x_string_var = tk.StringVar()
        layout_state.coordinates_editor_y_string_var = tk.StringVar()

        self.parameters_changed_key = None
        self.Render()

    def Render(self):

        visualization_state = StoreModule.Get(VisualizationState)

        # If the vector_editor_target parameter has NOT changed, then return
        if (id(visualization_state.coordinates_editor_target) == self.parameters_changed_key):
            return

        self.coordinates = visualization_state.coordinates_editor_target
        self.parameters_changed_key = id(self.coordinates)

        for c in list(self.children.values()): c.destroy()

        theme_state = StoreModule.Get(ThemeState)
        layout_state = StoreModule.Get(LayoutState)

        if self.coordinates is None:
            layout_state.coordinates_editor_x_string_var.set(0)
            layout_state.coordinates_editor_y_string_var.set(0)
            coordinatesLength= 2
        elif self.coordinates is not None:
            layout_state.coordinates_editor_x_string_var.set(self.coordinates.coordinates[0])
            layout_state.coordinates_editor_y_string_var.set(self.coordinates.coordinates[1])
            coordinatesLength = len(self.coordinates.coordinates)

        header_frame = tk.Frame(self)
        body_frame = tk.Frame(self)

        header_frame.pack(side='left')
        body_frame.pack(side='left')

        # Header content
        label = tk.Label(
            header_frame,
            text='Drawing Position:',
            bg=theme_state.theme_current.footer_background_color,
            fg=theme_state.theme_current.primary_foreground_color)
        label.pack()
        
        # Body content
        if coordinatesLength != 2:
            label = tk.Label(
                body_frame,
                text=f'{coordinatesLength} dimensions are not supported.',
                bg=theme_state.theme_current.footer_background_color,
                fg=theme_state.theme_current.primary_foreground_color)
            label.pack()
        else:
            x_label = tk.Label(
                body_frame,
                text='x',
                bg=theme_state.theme_current.header_background_color,
                fg=theme_state.theme_current.primary_foreground_color)
            
            x_entry = tk.Entry(body_frame, textvariable = layout_state.coordinates_editor_x_string_var)
            
            y_label = tk.Label(
                body_frame,
                text='y',
                bg=theme_state.theme_current.header_background_color,
                fg=theme_state.theme_current.primary_foreground_color)
            
            y_entry=tk.Entry(body_frame, textvariable = layout_state.coordinates_editor_y_string_var)

            x_label.grid(row=0,column=0)
            x_entry.grid(row=0,column=1)
            
            y_label.grid(row=1,column=0)
            y_entry.grid(row=1,column=1)


    def OnVisualizationState_StateChanged(self, *args):
        if len(args) > 0:
            if isinstance(args[0], CoordinatesModel):
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