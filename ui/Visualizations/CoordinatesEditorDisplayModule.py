import tkinter as tk
from CoordinatesVisualizationModule import CoordinatesVisualization
from Themes.ThemeServiceModule import theme_service
from Layouts import LayoutServiceModule
from Dispatchers import StoreModule

class CoordinatesEditorDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk, coordinates: CoordinatesVisualization | None):
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
        super().__init__(parent, bg=theme_service.theme_current.footer_background_color)
        self.pack(side="left", fill="both", expand=1)
        self.coordinates = coordinates

        layout_service: LayoutServiceModule.LayoutService = StoreModule.Get(StoreModule.fullname(LayoutServiceModule))

        layout_service.coordinates_editor_x_string_var = tk.StringVar()
        layout_service.coordinates_editor_y_string_var = tk.StringVar()

        layout_service.coordinates_editor_x_string_var.set(self.coordinates.coordinates[0])
        layout_service.coordinates_editor_y_string_var.set(self.coordinates.coordinates[1])
        
        coordinatesLength = len(self.coordinates.coordinates)
        
        header_frame = tk.Frame(self)
        body_frame = tk.Frame(self)

        header_frame.pack(side='left')
        body_frame.pack(side='left')

        # Header content
        label = tk.Label(
            header_frame,
            text='Coordinates:',
            bg=theme_service.theme_current.footer_background_color,
            fg=theme_service.theme_current.primary_foreground_color)
        label.pack()
        
        # Body content
        if coordinatesLength != 2:
            label = tk.Label(
                body_frame,
                text=f'{coordinatesLength} dimensions are not supported.',
                bg=theme_service.theme_current.footer_background_color,
                fg=theme_service.theme_current.primary_foreground_color)
            label.pack()
        else:
            x_label = tk.Label(
                body_frame,
                text='x',
                bg=theme_service.theme_current.header_background_color,
                fg=theme_service.theme_current.primary_foreground_color)
            
            x_entry = tk.Entry(body_frame, textvariable = layout_service.coordinates_editor_x_string_var)
            
            y_label = tk.Label(
                body_frame,
                text='y',
                bg=theme_service.theme_current.header_background_color,
                fg=theme_service.theme_current.primary_foreground_color)
            
            y_entry=tk.Entry(body_frame, textvariable = layout_service.coordinates_editor_y_string_var)

            x_label.grid(row=0,column=0)
            x_entry.grid(row=0,column=1)
            
            y_label.grid(row=1,column=0)
            y_entry.grid(row=1,column=1)
