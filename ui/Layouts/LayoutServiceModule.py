import tkinter as tk
import Events

class LayoutService:
    def __init__(self):
        self.existing_root: tk.Tk = None

        self.vector_editor_x_string_var: tk.StringVar = None
        self.vector_editor_y_string_var: tk.StringVar = None

        self.coordinates_editor_x_string_var: tk.StringVar = None
        self.coordinates_editor_y_string_var: tk.StringVar = None

        self.state_changed: Events.EventModelModule.EventModel = Events.EventModelModule.EventModel()

def InjectLayoutService(injectedLayoutService: LayoutService):
    global layout_service
    layout_service = injectedLayoutService

layout_service: LayoutService = None