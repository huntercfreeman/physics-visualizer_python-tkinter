class ThemeDisplay:
    """Contains colors for the UI."""
    def __init__(self, background_color: str, foreground_color: str):
        self.background_color = background_color
        self.foreground_color = foreground_color

theme_list = [
    ThemeDisplay(background_color='#1e1e1e', foreground_color='#d4d4d4'),
    ThemeDisplay(background_color='#fdfdfd', foreground_color=''),
]

theme_current = theme_list[0]
