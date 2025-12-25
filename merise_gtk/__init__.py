# package metadata
__version__ = "0.0.0"

# outer imports
import gettext, locale

# inner imports
from .application import MGTKApp

# extra constants
LOCALE_PATH: str = "po"
GETTEXT_DOMAIN: str = "MeriseGTK"


# gettext bindings
def bindtxt() -> None:
    # fetching correct translations
    gettext.bindtextdomain(GETTEXT_DOMAIN, LOCALE_PATH)
    gettext.textdomain(GETTEXT_DOMAIN)
    gettext.install(GETTEXT_DOMAIN)


# app launcher
def main() -> None:
    bindtxt() # ensure correct translation is fetched
    app: MGTKApp = MGTKApp() # FIXME find how to pass the translation
    app.run()
