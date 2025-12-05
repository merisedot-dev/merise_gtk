import gi
import os

# package metadata
__version__ = "0.0.0"

# GTK and Adwaita checks
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("GIRepository", "3.0")
from gi.repository import Adw, Gio, Gtk

# TODO load GResource data
resource = Gio.Resource.load("merise_gtk.gresource")
resource._register()

# TODO inner imports
from .application import MGTKApp


# app launcher
def main() -> None:
    app: MGTKApp = MGTKApp(
        application_id="com/github/merisedot-dev/merise_gtk")
    app.run()
