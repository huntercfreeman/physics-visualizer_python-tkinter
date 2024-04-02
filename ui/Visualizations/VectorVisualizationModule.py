from Vectors.VectorModelModule import VectorModel
from CoordinatesVisualizationModule import CoordinatesVisualization

class VectorVisualization:
    def __init__(self, vector: VectorModel, coordinates: CoordinatesVisualization):
        self.components = vector.components
        self.coordinates = coordinates.coordinates
