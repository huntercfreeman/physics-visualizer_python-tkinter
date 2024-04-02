from Events.EventModelModule import EventModel
from VectorVisualizationModule import VectorVisualization
from Vectors.VectorModelModule import VectorModel
from CoordinatesVisualizationModule import CoordinatesVisualization

class VisualizationState:
    def __init__(self):
        self.vector_visualization_list: list[VectorVisualization] = []
        self.state_changed: EventModel = EventModel()

    def AddVector(self,
                  vector: VectorModel,
                  coordinates: CoordinatesVisualization):
        
        vector_visualization = VectorVisualization(vector, coordinates)
        self.vector_visualization_list.append(vector_visualization)

        self.state_changed.trigger(vector_visualization)