import gi

# GTK checks
from gi.repository import Adw, Gtk

# inner imports
from .model import MGTKProject


@Gtk.Template(filename="merise_gtk/window.ui")
class MGTKWindow(Gtk.ApplicationWindow):
    # type definition
    __gtype_name__ = "root-window"

    # TODO fetch relevant signals
    # TODO fetch kids
    # TODO define callbacks

    def __init__(self, **kwargs) -> None:
        # TODO define inner attrs
        super().__init__(**kwargs)
