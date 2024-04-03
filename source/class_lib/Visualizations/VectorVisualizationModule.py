from class_lib.Vectors.VectorModelModule import VectorModel
from class_lib.Visualizations.CoordinatesModelModule import CoordinatesModel

class VectorVisualization:
    def __init__(self, vector: VectorModel, coordinates: CoordinatesModel):
        self.components = vector.components
        self.coordinates = coordinates.coordinates
