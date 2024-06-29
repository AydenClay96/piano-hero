from config import Parameters


class Object():
    """General Object superclass with useful generic information."""

    def __init__(self, name: str,
                 settings: Parameters,
                 position: tuple[float, float]) -> None:
        self.settings = settings
        self.name = name
        self.position = position
