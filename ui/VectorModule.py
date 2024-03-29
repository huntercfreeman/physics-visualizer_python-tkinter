import tkinter as tk
import ThemeModule

class VectorModel:
    """Stores the vector-components as a list.
    Index 0 corresponds to x-magnitude, 1 to the y-magnitude, 2 to the z-magnitude, etc..."""
    def __init__(self, components: list):
        self.components = components

class VectorEditorDisplay(tk.Frame):
    def __init__(self, parent: tk.Tk, vector: VectorModel):
        super().__init__(parent, bg=ThemeModule.theme_current.footer_background_color)
        self.pack(side="left", fill="both", expand=1)
        self.vector = vector
        self.x_string_var=tk.StringVar()
        self.y_string_var=tk.StringVar()

        self.x_string_var.set(self.vector.components[0])
        self.y_string_var.set(self.vector.components[1])
        
        componentsLength = len(self.vector.components)

        header_frame = tk.Frame(self)
        body_frame = tk.Frame(self)

        header_frame.pack(side='left')
        body_frame.pack(side='left')

        # Header content
        label = tk.Label(
            header_frame,
            text='Vector Components:',
            bg=ThemeModule.theme_current.footer_background_color,
            fg=ThemeModule.theme_current.primary_foreground_color)
        label.pack()
        
        # Body content
        if componentsLength != 2:
            label = tk.Label(
                body_frame,
                text=f'{componentsLength} dimensions are not supported.',
                bg=ThemeModule.theme_current.footer_background_color,
                fg=ThemeModule.theme_current.primary_foreground_color)
            label.pack()
        else:
            x_label = tk.Label(
                body_frame,
                text='Ax',
                bg=ThemeModule.theme_current.header_background_color,
                fg=ThemeModule.theme_current.primary_foreground_color)
            
            x_entry = tk.Entry(body_frame, textvariable=self.x_string_var)
            
            y_label = tk.Label(
                body_frame,
                text='Ay',
                bg=ThemeModule.theme_current.header_background_color,
                fg=ThemeModule.theme_current.primary_foreground_color)
            
            y_entry=tk.Entry(body_frame, textvariable=self.y_string_var)

            x_label.grid(row=0,column=0)
            x_entry.grid(row=0,column=1)
            
            y_label.grid(row=1,column=0)
            y_entry.grid(row=1,column=1)
