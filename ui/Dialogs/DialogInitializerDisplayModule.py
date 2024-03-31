import tkinter as tk
import DialogServiceModule
import DialogDisplayModule

class DialogInitializerDisplay:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.__dialog_display_list: list[DialogDisplayModule.DialogDisplay] = []
        DialogServiceModule.dialog_service.state_changed.addListener(self.Render)
        
        # Force an initial render
        self.Render()

    def Render(self):
        self.destroy()

        for value in DialogServiceModule.dialog_service.dialog_map.values():
            self.__dialog_display_list.append(DialogDisplayModule.DialogDisplay(
                self.root, value))
            
    def destroy(self):
        for dialog_display in self.__dialog_display_list:
            dialog_display.destroy()
            self.__dialog_display_list.remove(dialog_display)

    def __del__(self):
        """The usage of '__del__()' can have some quirks as described in this link:
        https://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/."""

        dialog_service = DialogServiceModule.dialog_service

        if dialog_service != None:
            if hasattr(dialog_service, 'state_changed'):
                if hasattr(dialog_service.state_changed, 'removeListener'):
                    dialog_service.state_changed.removeListener(self.Render)