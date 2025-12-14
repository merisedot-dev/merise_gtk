# package metadata
__version__ = "0.0.0"

# inner imports
from .application import MGTKApp


# app launcher
def main() -> None:
    app: MGTKApp = MGTKApp()
    app.run()
