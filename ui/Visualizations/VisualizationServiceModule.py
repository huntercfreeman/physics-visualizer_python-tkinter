import Events
import Vectors
import CoordinatesVisualizationModule
import VectorVisualizationModule

class VisualizationService:
    def __init__(self):
        self.vector_visualization_list: list[VectorVisualizationModule.VectorVisualization] = []
        self.state_changed: Events.EventModelModule.EventModel = Events.EventModelModule.EventModel()

    def AddVector(self,
                  vector: Vectors.VectorModelModule.VectorModel,
                  coordinates: CoordinatesVisualizationModule.CoordinatesVisualization):
        
        self.vector_visualization_list.append(VectorVisualizationModule.VectorVisualization(
            vector, coordinates))
        
        self.state_changed.trigger((vector, coordinates))

def InjectVisualizationService(injectedVisualizationService: VisualizationService):
    global visualization_service
    visualization_service = injectedVisualizationService

visualization_service: VisualizationService = None