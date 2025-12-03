import gi

# package metadata
__version__ = "0.0.0"

# GTK and Adwaita checks
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw


class MyApp(Adw.Application):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect("activate", self.on_activate)

    def on_activate(self, app) -> None:
        builder = Gtk.Builder()
        builder.add_from_file("merise_gtk/merise_gtk.ui")
        # display main window
        self.win = builder.get_object("root-window")
        self.win.set_application(self)
        self.win.present()


def main() -> None:
    app = MyApp(application_id="test")
    app.run()
