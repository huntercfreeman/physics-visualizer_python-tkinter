from Events.EventModelModule import EventModel
from States.StatefulModelModule import StatefulModel

class TooltipState(StatefulModel):

    store_key = None

    def __init__(self) -> None:
        super().__init__()
        self.state_changed: EventModel = EventModel()