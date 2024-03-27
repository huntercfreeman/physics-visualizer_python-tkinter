import json
import tkinter as tk
import ThemeModule
import LayoutModule

def main():
    root = tk.Tk()

    render_ui(root)

    # canvas = tk.Canvas(root, bg=ThemeModule.theme_current.background_color)
    # canvas.pack(expand=1, fill=tk.BOTH)

    # for loop_theme in ThemeModule.theme_list:
    #     # capture the theme from the 'for' iterations by creating a lambda within a lambda.
    #     button = tk.Button(
    #         canvas,
    #         text="abc",
    #         command=(lambda x_theme: (lambda : print(json.dumps(x_theme.__dict__))))(loop_theme))

    #     button.pack()

    root.mainloop()

def render_ui(root):
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

    # If the red background of 'root' is visible, then something is wrong.
    # The inner frames should cover 100% of the 'root', and their background color
    # therefore should be rendered instead of the root's red background color.
    root["bg"]='red'

    LayoutModule.InitializeLayout(root)

if __name__ == '__main__':
    main()

