import tkinter as tk
from Layouts.LayoutStateModule import LayoutState
from Layouts.AppHeaderDisplayModule import AppHeaderDisplay
from Layouts.AppBodyDisplayModule import AppBodyDisplay
from Layouts.AppFooterDisplayModule import AppFooterDisplay
from Dialogs.DialogInitializerDisplayModule import DialogInitializerDisplay
from Themes.ThemeStateModule import ThemeState
from Dialogs.DialogStateModule import DialogState
from States.DispatcherModule import Dispatcher
from States import StoreModule
from Visualizations.VisualizationStateModule import VisualizationState

def main():

    RegisterState()

    global root
    root = tk.Tk()
    style_root(root)

    theme_state = StoreModule.Get(ThemeState)

    theme_state.state_changed.addListener(OnThemeState_StateChanged)

    render_ui(root)
    root.mainloop()

    theme_state.state_changed.removeListener(reload_ui)

def style_root(root: tk.Tk):
    # geometry variables
    width = 1280
    height = 960
    left = 800
    top = 150

    #Get the current screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # validate: width, height
    width = min(width, screen_width)
    height = min(height, screen_height)

    # valid : left, top
    if (width + left >= screen_width):
        left = 0
    if (height + top >= screen_height):
        top = 0
    
    root.geometry(f'{width}x{height}+{left}+{top}')
    root.pack_propagate(tk.FALSE)
    root["bg"] = StoreModule.Get(ThemeState).theme_current.primary_background_color

def render_ui(root: tk.Tk):
    global app_header_display
    global app_body_display
    global app_footer_display
    app_header_display = AppHeaderDisplay(root)
    app_body_display = AppBodyDisplay(root)
    app_footer_display = AppFooterDisplay(root)

    global dialog_initializer_display
    if dialog_initializer_display == None:
        dialog_initializer_display = DialogInitializerDisplay(root)
    else:
        dialog_initializer_display.root = root
        dialog_initializer_display.Render()

def reload_ui():
    destroy_ui()
    render_ui(root)

def destroy_ui():
    if dialog_initializer_display != None: dialog_initializer_display.destroy()

    if app_header_display != None: app_header_display.destroy()
    if app_body_display != None: app_body_display.destroy()
    if app_footer_display != None: app_footer_display.destroy()

def RegisterState():
    StoreModule.Register(LayoutState)
    StoreModule.Register(VisualizationState)
    StoreModule.Register(ThemeState)
    StoreModule.Register(DialogState)

def OnThemeState_StateChanged(*args):
    reload_ui()

root: tk.Tk = None

dialog_initializer_display: DialogInitializerDisplay = None
app_header_display: AppHeaderDisplay = None
app_body_display: AppBodyDisplay = None
app_footer_display: AppFooterDisplay = None

if __name__ == '__main__':
    main()

