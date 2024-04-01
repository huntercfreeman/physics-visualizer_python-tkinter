class ThemeModel:
    """Contains colors for the UI."""
    def __init__(self,
                 display_name: str,
                 primary_background_color: str,
                 primary_foreground_color: str,
                 secondary_background_color: str,
                 secondary_foreground_color: str,
                 header_background_color: str,
                 footer_background_color: str,
                 dialog_toolbar_background_color: str,
                 primary_border_background_color: str,
                 coordinate_system_axis_fill_color: str,
                 visualization_toolbar_background_color: str,
                 visualization_toolbar_foreground_color: str,
                 button_background_color: str,
                 button_foreground_color: str,
                 button_active_background_color: str,
                 button_active_foreground_color: str):
        self.display_name = display_name
        self.primary_background_color = primary_background_color
        self.primary_foreground_color = primary_foreground_color
        self.secondary_background_color = secondary_background_color
        self.secondary_foreground_color = secondary_foreground_color
        self.header_background_color = header_background_color
        self.footer_background_color = footer_background_color
        self.dialog_toolbar_background_color = dialog_toolbar_background_color
        self.primary_border_background_color = primary_border_background_color
        self.coordinate_system_axis_fill_color = coordinate_system_axis_fill_color
        self.visualization_toolbar_background_color = visualization_toolbar_background_color
        self.visualization_toolbar_foreground_color = visualization_toolbar_foreground_color
        self.button_background_color = button_background_color
        self.button_foreground_color = button_foreground_color
        self.button_active_background_color = button_active_background_color
        self.button_active_foreground_color = button_active_foreground_color
