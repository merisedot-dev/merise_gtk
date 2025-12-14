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
    # fetch kids
    mgtk_header = Gtk.Template.Child()
    newproj_btn = Gtk.Template.Child()

    # TODO define callbacks
    # TODO define gtk-related properties

    def __init__(self, **kwargs) -> None:
        # TODO define inner attrs
        self._proj: MGTKProject = None
        # regular constructor for our window
        super().__init__(**kwargs)
        # add stateless actions to handle by the window
        for action in ["mk_proj"]:
            gio_act = Gio.SimpleAction.new(action, None)
            gio_act.connect("activate", getattr(self, f"on_{action}_activate"))
            self.add_action(gio_act)

    @GObject.Property(type=MGTKProject)
    def proj(self) -> MGTKProject:
        return self._proj

    def on_mk_proj_activate(self) -> None:
        pass
