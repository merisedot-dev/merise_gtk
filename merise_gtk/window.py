import gi

# GTK checks
from gi.repository import Adw, Gtk

# inner imports


@Gtk.Template(
    resource_path="/com/github/merisedot-dev/merise_gtk/merise_gtk.ui")
class MGTKWindow(Adw.ApplicationWindow):
    # TODO fetch relevant components
    # TODO fetch relevant signals
    # TODO fetch relevant properties

    def __init__(self, **kwargs) -> None:
        self._proj = None # TODO define project type

        # GTK constructors like to do stuff
        super().__init__(kwargs)

        # TODO link correct behavior
        # TODO define behavior
