import ThemeModelModule
import Events

class ThemeService():
    def __init__(self) -> None:
        self.state_changed: Events.EventModelModule.EventModel = Events.EventModelModule.EventModel()

        self.theme_list = [
            ThemeModelModule.ThemeModel(
                display_name='dark',
                primary_background_color='#1e1e1e',
                primary_foreground_color='#dcdcdc',
                secondary_background_color='#2d2d2d',
                secondary_foreground_color='#dcdcdc',
                header_background_color='#2a2a2e',
                footer_background_color='#2a2a2e',
                dialog_toolbar_background_color='#071c57',
                primary_border_background_color='#d7d7d7',
                coordinate_system_axis_fill_color='#78c8d2',
                visualization_toolbar_background_color='#2b2937',
                visualization_toolbar_foreground_color='#dcdcdc'),
            ThemeModelModule.ThemeModel(
                display_name='light',
                primary_background_color='#fdfdfd',
                primary_foreground_color='black',
                secondary_background_color='#fafaf4',
                secondary_foreground_color='black',
                header_background_color='#cad5eb',
                footer_background_color='#cad5eb',
                dialog_toolbar_background_color='#aac1ee',
                primary_border_background_color='black',
                coordinate_system_axis_fill_color='#006e5a',
                visualization_toolbar_background_color='#f8f8ee',
                visualization_toolbar_foreground_color='black'),
        ]

        self.theme_current = self.theme_list[0]

    def SetTheme(self, theme: ThemeModelModule.ThemeModel):
        self.theme_current = theme
        self.state_changed.trigger(theme)

def InjectThemeService(injectedThemeService: ThemeService):
    global theme_service
    theme_service = injectedThemeService

theme_service: ThemeService = None
