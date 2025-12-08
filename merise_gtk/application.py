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
        for act in ["mk_proj"]:
            action = Gio.SimpleAction.new(act, None)
            action.connect("activate", getattr(self, f"on_{act}_activate"))
            self.add_action(action) # FIXME this does not set anything
        self.connect("activate", self.on_activate)

    # launch method
    def on_activate(self, app) -> None:
        builder = Gtk.Builder()
        builder.add_from_file("merise_gtk/application.ui")
        # display main window
        self.win = builder.get_object("root-window")
        self.win.set_application(self)
        self.win.present()

    # project creator method
    def on_mk_proj_activate(self) -> None:
        pass # TODO find action to link
