from Themes.ThemeModelModule import ThemeModel
from Events.EventModelModule import EventModel
from States.StatefulModelModule import StatefulModel

class ThemeState(StatefulModel):

    store_key = None

    def __init__(self) -> None:
        super().__init__()
        self.state_changed: EventModel = EventModel()

        self.theme_list = [
            ThemeModel(
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
                visualization_toolbar_foreground_color='#dcdcdc',
                button_background_color='#1e56a7',
                button_foreground_color='#DCDCDC',
                button_active_background_color='#753282',
                button_active_foreground_color='#d2d2d2',
                danger_background_color='#b35252'),
            ThemeModel(
                display_name='light',
                primary_background_color='#fdfdfd',
                primary_foreground_color='black',
                secondary_background_color='#f6f4ee',
                secondary_foreground_color='black',
                header_background_color='#cad5eb',
                footer_background_color='#cad5eb',
                dialog_toolbar_background_color='#aac1ee',
                primary_border_background_color='black',
                coordinate_system_axis_fill_color='#006e5a',
                visualization_toolbar_background_color='#f6f4ee',
                visualization_toolbar_foreground_color='black',
                button_background_color='#0b30c7',
                button_foreground_color='#f0f0f0',
                button_active_background_color='#d889e8',
                button_active_foreground_color='black',
                danger_background_color='#b35252'),
        ]

        self.theme_current = self.theme_list[0]

    def SetTheme(self, theme: ThemeModel):
        self.theme_current = theme
        self.state_changed.trigger({"theme":theme})
        