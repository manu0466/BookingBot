class Building:

    """
    Class that represents a building.
    """

    def __init__(self, identifier: str, name: str):
        self._identifier = identifier
        self._name = name

    def get_identifier(self):
        return self._identifier

    def get_name(self) -> str:
        return self._name
