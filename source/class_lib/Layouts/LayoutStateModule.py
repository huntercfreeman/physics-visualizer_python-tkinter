import tkinter as tk
from class_lib.Events.EventModelModule import EventModel
from class_lib.States.StatefulModelModule import StatefulModel

class LayoutState(StatefulModel):

    store_key = None

    def __init__(self):
        super().__init__()
        self.existing_root: tk.Tk = None

        self.vector_editor_x_string_var: tk.StringVar = None
        self.vector_editor_y_string_var: tk.StringVar = None

        self.coordinates_editor_x_string_var: tk.StringVar = None
        self.coordinates_editor_y_string_var: tk.StringVar = None

        self.state_changed: EventModel = EventModel()
