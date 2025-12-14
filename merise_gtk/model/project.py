from gi.repository import GObject


class MGTKProject(GObject.Object):
    __gtype_name__ = "MGTKProject"

    # TODO define watched signals
    # TODO define properties
    # TODO add extra logic

    def __init__(self, name: str, **kwargs) -> None:
        self._name = name
        # gtk constructor, to set the right defaults
        super().__init__(**kwargs)
