import pluggy

hookimpl = pluggy.HookimplMarker("indicator")
import gi

try:
    gi.require_version('Gtk', '3.0')
    gi.require_version('Gdk', '3.0')
    gi.require_version('AppIndicator3', '0.1')
    gi.require_version('GdkPixbuf', '2.0')
    gi.require_version('Keybinder', '3.0')
except Exception as e:
    print(e)
    exit(-1)
from gi.repository import Gtk
class IndicatorPlugin1(object):
    """A hook implementation namespace.
    """

    @hookimpl
    def get_hook_menu(self, ):
        """Return a Gtk.Menu().

        :return: new Menu Gtk.Menu
        """
        project_item = Gtk.CheckMenuItem.new_with_label('Testing menu')
        project_item.connect('toggled', self.on_menu_filter_project_toggled)

        project_item2 = Gtk.CheckMenuItem.new_with_label('Testing menu 2')
        project_item2.connect('toggled', self.on_menu_filter_project_toggled2)

        return [project_item, project_item2]

    def on_menu_filter_project_toggled(self, widget):
        print('Testing menu')

    def on_menu_filter_project_toggled2(self, widget):
        print('Testing menu 2')