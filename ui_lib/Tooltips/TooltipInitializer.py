import tkinter as tk
from States import StoreModule
from Tooltips.TooltipDisplayModule import TooltipDisplay
from Tooltips.TooltipStateModule import TooltipState

class TooltipInitializer:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.__tooltip_display_list: list[TooltipDisplay] = []

        tooltip_state = StoreModule.Get(TooltipState)
        tooltip_state.state_changed.addListener(self.OnDialogState_StateChanged)
        
        # Force an initial render
        self.Render()

    def Render(self):
        self.destroy()

        tooltip_state = StoreModule.Get(TooltipState)

        for value in tooltip_state.tooltip_map.values():
            self.__tooltip_display_list.append(TooltipDisplay(
                self.root, value))
            
    def destroy(self):
        for dialog_display in self.__tooltip_display_list.copy():
            dialog_display.destroy()
            self.__tooltip_display_list.remove(dialog_display)

    def OnDialogState_StateChanged(self, *args):
        self.Render()

    def __del__(self):
        """The usage of '__del__()' can have some quirks as described in this link:
        https://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/."""
        
        local_tooltip_state = StoreModule.Get(TooltipState)

        if local_tooltip_state != None:
            if hasattr(local_tooltip_state, 'state_changed'):
                if hasattr(local_tooltip_state.state_changed, 'removeListener'):
                    local_tooltip_state.state_changed.removeListener(self.OnDialogState_StateChanged)