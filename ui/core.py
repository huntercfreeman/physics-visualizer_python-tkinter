from collections import namedtuple
import tkinter as tk
import json
import Theme 

def main():

    screen_measurements = get_curr_screen_width_height_tuple()

    # geometry variables
    width = 1280
    height = 960
    left = 800
    top = 150

    # validate: width, height
    width = min(width, screen_measurements.width)
    height = min(height, screen_measurements.height)

    # valid : left, top
    if (width + left >= screen_measurements.width):
        left = 0
    if (height + top >= screen_measurements.height):
        top = 0

    root = tk.Tk()
    root.geometry(f'{width}x{height}+{left}+{top}')

    canvas = tk.Canvas(root, bg=Theme.theme_current.background_color)
    canvas.pack(expand=1, fill=tk.BOTH)

    for loop_theme in Theme.theme_list:
        # capture the theme from the 'for' iterations by creating a lambda within a lambda.
        button = tk.Button(
            canvas,
            text="abc",
            command=(lambda x_theme: (lambda : print(json.dumps(x_theme.__dict__))))(loop_theme))

        button.pack()

    root.mainloop()

def get_curr_screen_width_height_tuple():
    """
    Workaround to get the size of the current screen in a multi-screen setup.

    Returns:
        geometry (str): The standard Tk geometry string.
            [width]x[height]+[left]+[top]

    https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python/56913005#56913005
    """
    root = tk.Tk()
    root.update_idletasks()
    root.attributes('-fullscreen', True)
    root.state('iconic')

    ScreenMeasurements = namedtuple('WidthHeight', ['width', 'height',])

    screen_measurements = ScreenMeasurements(root.winfo_width(), root.winfo_height())
    root.destroy()
    return screen_measurements

if __name__ == '__main__':
    main()

