from class_lib.Dialogs.DialogModelModule import DialogModel
from class_lib.Events.EventModelModule import EventModel
from class_lib.States.StatefulModelModule import StatefulModel

class DialogState(StatefulModel):
    """Provides API to render a dialog"""
    store_key = None

    def __init__(self):
        super().__init__()
        self.state_changed: EventModel = EventModel()
        self.dialog_map = {}

    def register_dialog(self, display_name: str):
        if display_name not in self.dialog_map:
            self.dialog_map[display_name] = DialogModel(display_name)
            self.state_changed.trigger([display_name])

    def dispose_dialog(self, display_name: str):
        if display_name in self.dialog_map:
            del self.dialog_map[display_name]
            self.state_changed.trigger([display_name])
