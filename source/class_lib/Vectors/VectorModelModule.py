class VectorModel:
    """Stores the vector-components as a list.
    Index 0 corresponds to x-magnitude, 1 to the y-magnitude, 2 to the z-magnitude, etc..."""
    def __init__(self, components: list):
        self.components = components
        