class PanelModel:
    def __init__(self, create_func, destroy_func):
        self.create_func = create_func
        self.destroy_func = destroy_func
