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
        for dialog_display in self.__dialog_display_list:
            dialog_display.destroy()

        for value in DialogServiceModule.dialog_service.dialog_map.values():
            self.__dialog_display_list.append(DialogDisplayModule.DialogDisplay(
                self.root, value))

    def __del__(self):
        """The usage of '__del__()' can have some quirks as described in this link:
        https://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/
        
        That beings said, the '__init__' code is unrelated to the '__del__' in this scenario,
        and for that reason, it is believed that '__del__' is a fitting solution here."""
        DialogServiceModule.dialog_service.state_changed.removeListener(self.Render)