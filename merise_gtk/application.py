import gi

# GTK checks
from gi.repository import Adw, Gio, Gtk

# inner imports
from .model import MGTKProject


class MGTKApp(Adw.Application):
    # TODO fetch relevant components
    # TODO fetch relevant signals
    # TODO fetch relevant properties

    def __init__(self, **kwargs) -> None:
        self._proj: MGTKProject = None

        # GTK constructors like to do stuff
        super().__init__(**kwargs)

        # link correct behavior
        self.connect("activate", self.on_activate)

    # launch method
    def on_activate(self, app) -> None:
        builder = Gtk.Builder()
        builder.add_from_file("merise_gtk/application.ui")
        # display main window
        self.win = builder.get_object("root-window")
        self.win.set_application(self)
        self.win.present()
