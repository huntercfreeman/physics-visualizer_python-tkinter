import tkinter as tk
import Layouts
import Dialogs
import Themes

def main():
    global root
    root = tk.Tk()
    style_root(root)

    Themes.theme_service.state_changed.addListener(reload_ui)

    render_ui(root)
    root.mainloop()

    Themes.theme_service.state_changed.removeListener(reload_ui)

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
    global dialog_initializer_display
    if dialog_initializer_display == None:
        Dialogs.DialogInitializerDisplayModule.DialogInitializerDisplay(root)
    else:
        dialog_initializer_display.Render()

    global app_header_display
    global app_body_display
    global app_footer_display
    app_header_display = Layouts.AppHeaderDisplayModule.AppHeaderDisplay(root)
    app_body_display = Layouts.AppBodyDisplayModule.AppBodyDisplay(root)
    app_footer_display = Layouts.AppFooterDisplayModule.AppFooterDisplay(root)

def reload_ui():
    destroy_ui()
    render_ui(root)

def destroy_ui():
    if dialog_initializer_display != None: dialog_initializer_display.destroy()

    if app_header_display != None: app_header_display.destroy()
    if app_body_display != None: app_body_display.destroy()
    if app_footer_display != None: app_footer_display.destroy()

root: tk.Tk = None

dialog_initializer_display: Dialogs.DialogInitializerDisplayModule.DialogInitializerDisplay = None
app_header_display: Layouts.AppHeaderDisplayModule.AppHeaderDisplay = None
app_body_display: Layouts.AppBodyDisplayModule.AppBodyDisplay = None
app_footer_display: Layouts.AppFooterDisplayModule.AppFooterDisplay = None

if __name__ == '__main__':
    main()

