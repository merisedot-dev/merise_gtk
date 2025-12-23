import gi

# GTK checks
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gio, GObject, Gtk

# inner imports
from .model import MGTKProject


@Gtk.Template(filename="merise_gtk/window.ui")
class MGTKWindow(Gtk.ApplicationWindow):
    """Root window template class.
    This is meant to be the first type of GTK widget called by the application and
    will govern the placement and interactions within the application window.
    It will also handle the placement of new widgets, but not their logic.
    """

    # type definition
    __gtype_name__ = "root-window"

    # TODO fetch relevant signals
    # headerbar widgets
    mgtk_header = Gtk.Template.Child()
    newproj_btn = Gtk.Template.Child()
    open_btn = Gtk.Template.Child()
    redo_btn = Gtk.Template.Child()
    undo_btn = Gtk.Template.Child()

    # main area widgets
    mgtk_stack = Gtk.Template.Child()
    mgtk_version_lbl = Gtk.Template.Child()

    # creation form widgets
    proj_name_entry = Gtk.Template.Child()
    validate_btn = Gtk.Template.Child()
    cancel_btn = Gtk.Template.Child()
    path_picker = Gtk.Template.Child()
    path_picker_lbl = Gtk.Template.Child()
    mcd_name_entry = Gtk.Template.Child()

    def __init__(self, **kwargs) -> None:
        self._proj: MGTKProject = None
        # regular GTK constructor for our window
        super().__init__(**kwargs)
        # TODO add stateless actions to handle by the window
        # TODO ensure stack is operational and points to the right page

    @GObject.Property(type=MGTKProject)
    def proj(self) -> MGTKProject:
        return self._proj

    @Gtk.Template.Callback()
    def newproj_btn_clicked(self, button) -> None:
        print("TODO")

    @Gtk.Template.Callback()
    def open_btn_clicked(self, button) -> None:
        print("TODO")

    @Gtk.Template.Callback()
    def redo_btn_clicked(self, button) -> None:
        print("TODO")

    @Gtk.Template.Callback()
    def undo_btn_clicked(self, button) -> None:
        print("TODO")

    @Gtk.Template.Callback()
    def validate_btn_clicked(self, button) -> None:
        print("TODO")

    @Gtk.Template.Callback()
    def cancel_btn_clicked(self, button) -> None:
        print("TODO")

    @Gtk.Template.Callback()
    def path_picker_clicked(self, button) -> None:
        print("TODO")
