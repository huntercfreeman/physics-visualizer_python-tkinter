import tkinter as tk
import Visualizations
import Vectors

class LayoutService:
    def __init__(self):
        self.existing_root: tk.Tk = None

    def UiRender(self, root: tk.Tk):
        self.existing_root = root

    def UiStateHasChanged(self):
        self.app_header_display.destroy()
        self.app_body_display.destroy()
        self.app_footer_display.destroy()

        self.InitializeLayoutModule(self.existing_root)

    def UiDestroy(self):
        self.app_header_display.destroy()
        self.app_body_display.destroy()
        self.app_footer_display.destroy()

        self.InitializeLayoutModule(self.existing_root)

def InjectLayoutService(injectedLayoutService: LayoutService):
    global layout_service
    layout_service = injectedLayoutService

layout_service: LayoutService = None