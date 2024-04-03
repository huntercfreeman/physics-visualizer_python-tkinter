from Events.EventModelModule import EventModel
from Visualizations.VectorVisualizationModule import VectorVisualization
from Vectors.VectorModelModule import VectorModel
from Visualizations.CoordinatesModelModule import CoordinatesModel
from States.StatefulModelModule import StatefulModel

class VisualizationState(StatefulModel):

    store_key = None

    def __init__(self):
        super().__init__()
        self.vector_visualization_list: list[VectorVisualization] = []
        self.state_changed: EventModel = EventModel()

        self.vector_editor_target: VectorModel = None
        self.coordinates_editor_target: CoordinatesModel = None

    def AddVector(self,
                  vector: VectorModel,
                  coordinates: CoordinatesModel):
        
        vector_visualization = VectorVisualization(vector, coordinates)
        self.vector_visualization_list.append(vector_visualization)

        self.state_changed.trigger({"vector_visualization":vector_visualization})

    def SetVectorEditorTarget(self, vector: VectorModel | None):
        self.vector_editor_target = vector
        self.state_changed.trigger([vector])