import tkinter as tk
from VectorModelModule import VectorModel
from Themes.ThemeStateModule import ThemeState
from Layouts.LayoutStateModule import LayoutState
from Dispatchers import StoreModule

class VectorEditorDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk, vector: VectorModel | None):
        """
        Constructor takes an existing vector object, or 'None'.
        
        If provided an existing vector object, then map the vector's attributes
        to the corresponding editor's attributes. The form is populated with the provided
        vector's attributes, however, the provided vector is treated as immutable.

        If provided 'None', then the editor's attributes are set to their type's default value.

        No submit button is provided, one must make their own.

        Completion of the form is expected to be done in the following way:
            -Read the attributes on the editor class.
            -Pass these attributes to the vector object constructor.
            -The user of this form can check the 'self.vector' attribute on this class
                to determine whether an update, or creation is being performed.
                -If 'self.vector' is 'None', then a creation is being performed
                -If 'self.vector' has a vector object instance, then an update is
                    being performed.
                    -To update, one can either overwrite the existing vector object
                        or construct a new vector object.
        """

        theme_state: ThemeState = StoreModule.Get(ThemeState())

        super().__init__(parent, bg=theme_state.theme_current.footer_background_color)
        self.pack(side="left", fill="both", expand=1)
        self.vector = vector

        layout_state: LayoutState = StoreModule.Get(LayoutState())

        layout_state.vector_editor_x_string_var = tk.StringVar()
        layout_state.vector_editor_y_string_var = tk.StringVar()

        layout_state.vector_editor_x_string_var.set(self.vector.components[0])
        layout_state.vector_editor_y_string_var.set(self.vector.components[1])
        
        componentsLength = len(self.vector.components)

        header_frame = tk.Frame(self)
        body_frame = tk.Frame(self)

        header_frame.pack(side='left')
        body_frame.pack(side='left')

        # Header content
        label = tk.Label(
            header_frame,
            text='Vector Components:',
            bg=theme_state.theme_current.footer_background_color,
            fg=theme_state.theme_current.primary_foreground_color)
        label.pack()
        
        # Body content
        if componentsLength != 2:
            label = tk.Label(
                body_frame,
                text=f'{componentsLength} dimensions are not supported.',
                bg=theme_state.theme_current.footer_background_color,
                fg=theme_state.theme_current.primary_foreground_color)
            label.pack()
        else:
            x_label = tk.Label(
                body_frame,
                text='Ax*i',
                bg=theme_state.theme_current.header_background_color,
                fg=theme_state.theme_current.primary_foreground_color)
            
            x_entry = tk.Entry(body_frame, textvariable = layout_state.vector_editor_x_string_var)
            
            y_label = tk.Label(
                body_frame,
                text='Ay*j',
                bg=theme_state.theme_current.header_background_color,
                fg=theme_state.theme_current.primary_foreground_color)
            
            y_entry=tk.Entry(body_frame, textvariable = layout_state.vector_editor_y_string_var)

            x_label.grid(row=0,column=0)
            x_entry.grid(row=0,column=1)
            
            y_label.grid(row=1,column=0)
            y_entry.grid(row=1,column=1)
