import tkinter as tk
import ThemeModule
import DialogModule
import VisualizationModule
import HorizontalRuleModule
import VectorModule
from varname import nameof

def InitializeLayoutModule(root: tk.Tk):
    global existing_root
    global app_header_display
    global app_body_display
    global app_footer_display

    existing_root = root

    app_header_display = AppHeaderDisplay(root)
    app_body_display = AppBodyDisplay(root)
    app_footer_display = AppFooterDisplay(root)

def DestroyLayoutModule():
    global existing_root
    global app_header_display
    global app_body_display
    global app_footer_display

    app_header_display.destroy()
    app_body_display.destroy()
    app_footer_display.destroy()

    InitializeLayoutModule(existing_root)

class AppHeaderDisplay(tk.Frame):
    """Render the 'header' aka: 'navigation bar', or 'toolbar'."""
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.header_background_color)
        self.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        self.pack_propagate(tk.FALSE)
        
        def show_settings_dialog():
            DialogModule.dialog_service.register_dialog("Settings")

        button = tk.Button(self, text="settings", command=show_settings_dialog)
        button.pack(side="left")

        label = tk.Label(
            self,
            text=nameof(AppHeaderDisplay),
            bg=ThemeModule.theme_current.header_background_color,
            fg=ThemeModule.theme_current.primary_foreground_color)
        label.pack(side="left")

class AppBodyDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.primary_background_color)
        self.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
        self.pack_propagate(tk.FALSE)
        
        global visualization_display
        past_visualization_display = visualization_display

        HorizontalRuleModule.HorizontalRuleDisplay(self, anchor='n')

        visualization_display = VisualizationModule.VisualizationDisplay(self, root)

        if past_visualization_display != None:
            visualization_display.SetVectorVisualizationList(
                past_visualization_display.vector_visualization_list)

        HorizontalRuleModule.HorizontalRuleDisplay(self, anchor='s')

class AppFooterDisplay(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root, bg=ThemeModule.theme_current.footer_background_color)
        self.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
        self.pack_propagate(tk.FALSE)

        frame = tk.Frame(self)
        frame.pack(side="left")
        
        def SubmitFormOnClick():
            global vector_under_edit
            global vector_editor_display

            try:
                x = int(vector_editor_display.x_string_var.get())
                y = int(vector_editor_display.y_string_var.get())

                vector_editor_display.Submit()
                vector_editor_display.destroy()

                visualization_display.AddVector(VectorModule.VectorModel([x, y]))
                vector_editor_display = VectorModule.VectorEditorDisplay(self, vector_under_edit)
            except ValueError:
                print("some_variable did not contain a number!")
        button = tk.Button(frame, text="New Vector", command=SubmitFormOnClick)
        button.pack(side="top")
        
        global vector_under_edit
        global vector_editor_display

        vector_editor_display = VectorModule.VectorEditorDisplay(self, vector_under_edit)

existing_root: tk.Tk = None
app_header_display: AppHeaderDisplay = None
app_body_display: AppBodyDisplay = None
app_footer_display: AppFooterDisplay = None

visualization_display: VisualizationModule.VisualizationDisplay = None

vector_under_edit: VectorModule.VectorModel = VectorModule.VectorModel([50, 50])
vector_editor_display: VectorModule.VectorEditorDisplay = None