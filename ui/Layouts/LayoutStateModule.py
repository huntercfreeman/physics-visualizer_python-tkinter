import tkinter as tk
from Events.EventModelModule import EventModel

class LayoutState:
    def __init__(self):
        self.existing_root: tk.Tk = None

        self.vector_editor_x_string_var: tk.StringVar = None
        self.vector_editor_y_string_var: tk.StringVar = None

        self.coordinates_editor_x_string_var: tk.StringVar = None
        self.coordinates_editor_y_string_var: tk.StringVar = None

        self.state_changed: EventModel = EventModel()
