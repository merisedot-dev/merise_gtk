import gi

# package metadata
__version__ = "0.0.0"

# GTK and Adwaita checks
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk

# inner imports
from .application import MGTKApp


# app launcher
def main() -> None:
    app: MGTKApp = MGTKApp()
    app.run()
