# package metadata
__version__ = "0.0.0"

# outer imports

# inner imports
from .application import MGTKApp


# gettext bindings
def bindtxt() -> None:
    pass # TODO


# app launcher
def main() -> None:
    app: MGTKApp = MGTKApp()
    app.run()
