class MGTKProject:
    """Project definition class.
    Here, a project is defined as a collection of files indexed by a root project
    file, in the form `<name>.mgtk` (the mgtk "format" is mostly a marker).
    """

    def __init__(self, name: str) -> None:
        self._name = name
        # TODO define inner workings
