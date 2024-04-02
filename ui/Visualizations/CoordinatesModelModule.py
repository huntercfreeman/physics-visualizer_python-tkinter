class CoordinatesModel:
    """Stores coordinates as a list.
    Index 0 corresponds to the x-axis, 1 to the y-axis, 2 to the z-axis, etc..."""
    def __init__(self, coordinates: list):
        self.coordinates = coordinates