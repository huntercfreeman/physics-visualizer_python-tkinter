from Vectors.VectorModelModule import VectorModel
from Visualizations.CoordinatesModelModule import CoordinatesModel

class VectorVisualization:
    def __init__(self, vector: VectorModel, coordinates: CoordinatesModel):
        self.components = vector.components
        self.coordinates = coordinates.coordinates