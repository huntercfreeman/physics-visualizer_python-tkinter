class ThemeDisplay:
    """Contains colors for the UI."""
    def __init__(self,
                 display_name: str,
                 primary_background_color: str,
                 primary_foreground_color: str,
                 header_background_color: str):
        self.primary_background_color = primary_background_color
        self.primary_foreground_color = primary_foreground_color
        self.header_background_color = header_background_color

theme_list = [
    ThemeDisplay(
        display_name='dark',
        primary_background_color='#1e1e1e',
        primary_foreground_color='#d4d4d4',
        header_background_color='#2a2a2e'),
    ThemeDisplay(
        display_name='light',
        primary_background_color='#fdfdfd',
        primary_foreground_color='black',
        header_background_color='#cad5eb'),
]

theme_current = theme_list[0]
