import tkinter as tk

class DialogService:
    """Provides API to render a dialog"""
    def __init__(self):
        self.dialog_map = {}

    def register_dialog(self, display_name: str):
        if display_name not in self.dialog_map:
            pass

    def dispose_dialog(self, display_name: str):
        if display_name in self.dialog_map:
            self.dialog_map[display_name].destroy()
            del self.dialog_map[display_name]

    def DestroyDialogModule(self):
        pass

def InjectDialogService(injectedDialogService: DialogService):
    global dialog_service
    dialog_service = injectedDialogService

dialog_service: DialogService = None
