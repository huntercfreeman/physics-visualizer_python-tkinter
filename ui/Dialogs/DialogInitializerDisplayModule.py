import tkinter as tk
from DialogServiceModule import dialog_service
import DialogDisplayModule

class DialogInitializerDisplay:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.__dialog_display_list: list[DialogDisplayModule.DialogDisplay] = []
        dialog_service.state_changed.addListener(self.Render)
        
        # Force an initial render
        self.Render()

    def Render(self):
        self.destroy()

        for value in dialog_service.dialog_map.values():
            self.__dialog_display_list.append(DialogDisplayModule.DialogDisplay(
                self.root, value))
            
    def destroy(self):
        for dialog_display in self.__dialog_display_list:
            dialog_display.destroy()
            self.__dialog_display_list.remove(dialog_display)

    def __del__(self):
        """The usage of '__del__()' can have some quirks as described in this link:
        https://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/."""

        local_dialog_service = dialog_service

        if local_dialog_service != None:
            if hasattr(local_dialog_service, 'state_changed'):
                if hasattr(local_dialog_service.state_changed, 'removeListener'):
                    local_dialog_service.state_changed.removeListener(self.Render)