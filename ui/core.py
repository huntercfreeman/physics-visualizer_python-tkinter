import tkinter as tk
from Layouts.LayoutServiceModule import LayoutService
from Layouts.AppHeaderDisplayModule import AppHeaderDisplay
from Layouts.AppBodyDisplayModule import AppBodyDisplay
from Layouts.AppFooterDisplayModule import AppFooterDisplay
from Dialogs.DialogInitializerDisplayModule import DialogInitializerDisplay
from Themes.ThemeServiceModule import ThemeService
from Dialogs.DialogServiceModule import DialogService
from Dispatchers.DispatcherModule import Dispatcher
from Dispatchers import StoreModule
from Visualizations.VisualizationServiceModule import VisualizationService

def main():

    RegisterState()

    global root
    root = tk.Tk()
    style_root(root)

    theme_service: ThemeService = StoreModule.Get(ThemeService())

    theme_service.state_changed.addListener(reload_ui)

    render_ui(root)
    root.mainloop()

    theme_service.state_changed.removeListener(reload_ui)

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

    # If the red background of 'root' is visible, then something is wrong.
    # The inner frames should cover 100% of the 'root', and their background color
    # therefore should be rendered instead of the root's red background color.
    root["bg"]='red'

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
    StoreModule.Register(LayoutService())
    StoreModule.Register(VisualizationService())
    StoreModule.Register(ThemeService())
    StoreModule.Register(DialogService())

root: tk.Tk = None

dialog_initializer_display: DialogInitializerDisplay = None
app_header_display: AppHeaderDisplay = None
app_body_display: AppBodyDisplay = None
app_footer_display: AppFooterDisplay = None

if __name__ == '__main__':
    main()

