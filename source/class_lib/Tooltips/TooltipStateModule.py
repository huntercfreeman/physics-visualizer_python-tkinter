from class_lib.Events.EventModelModule import EventModel
from class_lib.States.StatefulModelModule import StatefulModel
from class_lib.Tooltips.TooltipModelModule import TooltipModel

class TooltipState(StatefulModel):
    """Provides API to render a tooltip"""
    store_key = None

    def __init__(self) -> None:
        super().__init__()
        self.state_changed: EventModel = EventModel()
        self.tooltip_map = {}

    def register_tooltip(self, display_name: str):
        if display_name not in self.tooltip_map:
            self.tooltip_map[display_name] = TooltipModel(display_name)
            self.state_changed.trigger([display_name])

    def dispose_tooltip(self, display_name: str):
        if display_name in self.tooltip_map:
            del self.tooltip_map[display_name]
            self.state_changed.trigger([display_name])
