from class_lib.Events.EventModelModule import EventModel
from class_lib.States.StatefulModelModule import StatefulModel

class TooltipState(StatefulModel):

    store_key = None

    def __init__(self) -> None:
        super().__init__()
        self.state_changed: EventModel = EventModel()