class ThemeDisplay:
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
                 coordinate_system_axis_fill_color: str):
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

theme_list = [
    ThemeDisplay(
        display_name='dark',
        primary_background_color='#1e1e1e',
        primary_foreground_color='#dcdcdc',
        secondary_background_color='#2d2d2d',
        secondary_foreground_color='#dcdcdc',
        header_background_color='#2a2a2e',
        footer_background_color='#2a2a2e',
        dialog_toolbar_background_color='#071c57',
        primary_border_background_color='#d7d7d7',
        coordinate_system_axis_fill_color='#78c8d2'),
    ThemeDisplay(
        display_name='light',
        primary_background_color='#fdfdfd',
        primary_foreground_color='black',
        secondary_background_color='#fafaf4',
        secondary_foreground_color='black',
        header_background_color='#cad5eb',
        footer_background_color='#cad5eb',
        dialog_toolbar_background_color='#aac1ee',
        primary_border_background_color='black',
        coordinate_system_axis_fill_color='#006e5a'),
]

theme_current = theme_list[0]

def SetTheme(theme: ThemeDisplay):
    global theme_current
    theme_current = theme