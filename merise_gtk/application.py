import gi
from .window import MGTKWindow

# GTK checks
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk

# Extra constants
APP_ID: str = "com.github.com.merisedot-dev.merise_gtk"


class MGTKApp(Adw.Application):
    """Root application class.
    This will act as a launcher, which will fetch the other windows and decide
    how the app will launch itself. Root-level logic should be handled here, as long
    as it doesn't rely on an interface.
    """

    def __init__(self) -> None:
        super().__init__(application_id=APP_ID)

    # define new application window for MeriseGtk
    def mk_window(self) -> MGTKWindow:
        win: MGTKWindow = MGTKWindow(application=self)
        # TODO add window specifics if needed
        self.add_window(win)
        return win

    # startup method for the app. Do not touch do_startup
    def do_activate(self) -> None:
        win = self.mk_window()
        win.present()
