import tkinter as tk
from DialogStateModule import DialogState
from DialogDisplayModule import DialogDisplay
from Dispatchers import StoreModule

class DialogInitializerDisplay:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.__dialog_display_list: list[DialogDisplay] = []

        dialog_state: DialogState = StoreModule.Get(DialogState())
        dialog_state.state_changed.addListener(self.Render)
        
        # Force an initial render
        self.Render()

    def Render(self):
        self.destroy()

        dialog_state: DialogState = StoreModule.Get(DialogState())

        for value in dialog_state.dialog_map.values():
            self.__dialog_display_list.append(DialogDisplay(
                self.root, value))
            
    def destroy(self):
        for dialog_display in self.__dialog_display_list:
            dialog_display.destroy()
            self.__dialog_display_list.remove(dialog_display)

    def __del__(self):
        """The usage of '__del__()' can have some quirks as described in this link:
        https://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/."""
        
        dialog_state: DialogState = StoreModule.Get(DialogState())

        local_dialog_state = dialog_state

        if local_dialog_state != None:
            if hasattr(local_dialog_state, 'state_changed'):
                if hasattr(local_dialog_state.state_changed, 'removeListener'):
                    local_dialog_state.state_changed.removeListener(self.Render)