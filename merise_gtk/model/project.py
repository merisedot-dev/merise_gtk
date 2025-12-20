from gi.repository import GObject


class MGTKProject(GObject.Object):
    """Project modeling class.
    A project is defined as a set of MLD and MCD graphs that can reference each
    other, as well as SQL scripts resulting of the user's work.
    """
    __gtype_name__ = "MGTKProject"

    # TODO define watched signals
    # TODO define properties
    # TODO add extra logic

    def __init__(self, name: str, **kwargs) -> None:
        self._name = name
        # gtk constructor, to set the right defaults
        super().__init__(**kwargs)
