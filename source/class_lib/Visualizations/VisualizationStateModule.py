from class_lib.Events.EventModelModule import EventModel
from class_lib.Visualizations.VectorVisualizationModule import VectorVisualization
from class_lib.Vectors.VectorModelModule import VectorModel
from class_lib.Visualizations.CoordinatesModelModule import CoordinatesModel
from class_lib.States.StatefulModelModule import StatefulModel

class VisualizationState(StatefulModel):

    store_key = None

    def __init__(self):
        super().__init__()
        self.vector_visualization_list: list[VectorVisualization] = []
        self.state_changed: EventModel = EventModel()

        self.vector_visualization_target: VectorVisualization = None
        self.vector_editor_target: VectorModel = None
        self.coordinates_editor_target: CoordinatesModel = None

    def DrawVector(self,
                  vector: VectorModel,
                  coordinates: CoordinatesModel):
        
        vector_visualization = VectorVisualization(vector, coordinates)
        self.vector_visualization_list.append(vector_visualization)

        self.state_changed.trigger([vector_visualization])

    def SetVectorVisualizationTarget(self, vector_visualization: VectorVisualization | None):
        self.vector_visualization_target = vector_visualization
        self.vector_editor_target = VectorModel(vector_visualization.components)
        self.coordinates_editor_target = CoordinatesModel(vector_visualization.coordinates)
        
        self.state_changed.trigger([self.vector_editor_target])
        self.state_changed.trigger([self.coordinates_editor_target])
