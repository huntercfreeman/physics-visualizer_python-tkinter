import Vectors
import CoordinatesVisualizationModule

class VectorVisualization:
    def __init__(self, vector: Vectors.VectorModelModule.VectorModel, coordinates: CoordinatesVisualizationModule.CoordinatesVisualization):
        self.components = vector.components
        self.coordinates = coordinates.coordinates
