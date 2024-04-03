import tkinter as tk
from Dialogs.DialogModelModule import DialogModel
from Events.EventModelModule import EventModel
from States.StatefulModelModule import StatefulModel

class DialogState(StatefulModel):
    """Provides API to render a dialog"""

    store_key = None

    def __init__(self):
        super().__init__()
        DialogState.store_key = self
        self.dialog_map = {}
        self.state_changed: EventModel = EventModel()
        self.root: tk.Tk = None

    def register_dialog(self, display_name: str):
        if display_name not in self.dialog_map:
            self.dialog_map[display_name] = DialogModel(display_name)
            self.state_changed.trigger({"display_name":display_name})

    def dispose_dialog(self, display_name: str):
        if display_name in self.dialog_map:
            del self.dialog_map[display_name]
            self.state_changed.trigger({"display_name":display_name})

    def DestroyDialogModule(self):
        pass
