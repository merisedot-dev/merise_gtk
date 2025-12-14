import gi

# GTK checks
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk

# inner imports
from .model import MGTKProject


@Gtk.Template(filename="merise_gtk/window.ui")
class MGTKWindow(Gtk.ApplicationWindow):
    # type definition
    __gtype_name__ = "root-window"

    # TODO fetch relevant signals
    # fetch kids
    mgtk_header = Gtk.Template.Child()

    # TODO define callbacks

    def __init__(self, **kwargs) -> None:
        # TODO define inner attrs
        self._proj: MGTKProject = None
        # regular constructor for our window
        super().__init__(**kwargs)
