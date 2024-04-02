import tkinter as tk
from LayoutServiceModule import LayoutService

class PanelModel:
    def __init__(self, create_func, destroy_func):
        self.create_func = create_func
        self.destroy_func = destroy_func

def InjectLayoutService(injectedLayoutService: LayoutService):
    global layout_service
    layout_service = injectedLayoutService
    
layout_service: LayoutService = None