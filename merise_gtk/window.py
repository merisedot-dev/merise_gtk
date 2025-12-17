import gi

# GTK checks
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gio, GObject, Gtk

# inner imports
from .model import MGTKProject


@Gtk.Template(filename="merise_gtk/window.ui")
class MGTKWindow(Gtk.ApplicationWindow):
    # type definition
    __gtype_name__ = "root-window"

    # TODO fetch relevant signals
    # fetch widget kids
    mgtk_header = Gtk.Template.Child()
    newproj_btn = Gtk.Template.Child()
    open_btn = Gtk.Template.Child()

    # TODO define callbacks
    # TODO define gtk-related properties

    def __init__(self, **kwargs) -> None:
        # TODO define inner attrs
        self._proj: MGTKProject = None
        # gtk persistance specifics
        self._actions = {}
        # regular constructor for our window
        super().__init__(**kwargs)
        # TODO add stateless actions to handle by the window
        # TODO define on_click callbacks

    @GObject.Property(type=MGTKProject)
    def proj(self) -> MGTKProject:
        return self._proj

    @Gtk.Template.Callback()
    def newproj_btn_clicked(self, button) -> None:
        print("TODO")
