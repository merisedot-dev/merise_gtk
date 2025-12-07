import gi

# GTK checks
from gi.repository import Adw, Gio, Gtk

# inner imports
from .model import MGTKProject


class MGTKApp(Adw.Application):
    # TODO fetch relevant components
    # TODO fetch relevant signals
    # TODO fetch relevant properties
    # TODO set keybinds for ease of use

    def __init__(self, **kwargs) -> None:
        self._proj: MGTKProject = None
        # GTK constructors like to do stuff
        super().__init__(**kwargs)
        # adding CSS stylesheet
        css_file = Gio.File.new_for_path("merise_gtk/merise_gtk.css")
        self._css_provider = Gtk.CssProvider()
        self._css_provider.load_from_file(css_file)
        # link relevant behaviors
        self.connect("activate", self._on_activate)

    # launch method
    def _on_activate(self, app) -> None:
        builder = Gtk.Builder()
        builder.add_from_file("merise_gtk/application.ui")
        # display main window
        self.win = builder.get_object("root-window")
        self.win.set_application(self)
        self.win.present()

    # project creator method
    def _mk_proj(self) -> None:
        pass # TODO find action to link
