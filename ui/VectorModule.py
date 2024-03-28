import tkinter as tk
import ThemeModule
from varname import nameof

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
        
        if componentsLength != 2:
            label = tk.Label(
                self,
                text=f'{componentsLength} dimensions are not supported.',
                bg=ThemeModule.theme_current.footer_background_color,
                fg=ThemeModule.theme_current.primary_foreground_color)
            label.pack()
        else:
            x_label = tk.Label(
                self,
                text='x',
                bg=ThemeModule.theme_current.header_background_color,
                fg=ThemeModule.theme_current.primary_foreground_color)
            x_entry = tk.Entry(self, textvariable=self.x_string_var)
            
            y_label = tk.Label(
                self,
                text='y',
                bg=ThemeModule.theme_current.header_background_color,
                fg=ThemeModule.theme_current.primary_foreground_color)
            y_entry=tk.Entry(self, textvariable=self.y_string_var)

            x_label.grid(row=0,column=0)
            x_entry.grid(row=0,column=1)
            
            y_label.grid(row=1,column=0)
            y_entry.grid(row=1,column=1)

    def Submit(self):
        print(f'x: {self.x_string_var.get()}')
        print(f'y: {self.y_string_var.get()}')
        
        self.x_string_var.set("")
        self.y_string_var.set("")

class Coordinates:
    """Stores coordinates as a list.
    Index 0 corresponds to the x-axis, 1 to the y-axis, 2 to the z-axis, etc..."""
    def __init__(self, coordinates: list):
        self.coordinates = coordinates
        