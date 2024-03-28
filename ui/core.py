import tkinter as tk
import LayoutModule
import DialogModule

def main():
    root = tk.Tk()
    initialize_ui(root)
    root.mainloop()

def initialize_ui(root: tk.Tk):
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
    
    LayoutModule.InitializeLayoutModule(root)
    DialogModule.InitializeDialogModule(root)

if __name__ == '__main__':
    main()
