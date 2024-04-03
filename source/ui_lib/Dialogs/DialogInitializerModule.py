import tkinter as tk
from class_lib.Dialogs.DialogStateModule import DialogState
from class_lib.States import StoreModule
from ui_lib.Dialogs.DialogDisplayModule import DialogDisplay

class DialogInitializer:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.__dialog_display_list: list[DialogDisplay] = []

        dialog_state = StoreModule.Get(DialogState)
        dialog_state.state_changed.addListener(self.OnDialogState_StateChanged)
        
        # Force an initial render
        self.Render()

    def Render(self):
        self.destroy()

        dialog_state = StoreModule.Get(DialogState)

        for value in dialog_state.dialog_map.values():
            self.__dialog_display_list.append(DialogDisplay(
                self.root, value))
            
    def destroy(self):
        for dialog_display in self.__dialog_display_list.copy():
            dialog_display.destroy()
            self.__dialog_display_list.remove(dialog_display)

    def OnDialogState_StateChanged(self, *args):
        self.Render()

    def __del__(self):
        """The usage of '__del__()' can have some quirks as described in this link:
        https://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/."""
        
        dialog_state = StoreModule.Get(DialogState)

        local_dialog_state = dialog_state

        if local_dialog_state != None:
            if hasattr(local_dialog_state, 'state_changed'):
                if hasattr(local_dialog_state.state_changed, 'removeListener'):
                    local_dialog_state.state_changed.removeListener(self.OnDialogState_StateChanged)