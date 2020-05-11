import pluggy

# Decorator for hook. The function that was decorated with this
# will be called from de master source if it in Hookspecks availables
indicatorimpl = pluggy.HookimplMarker("indicator")

# Custom featured needed
import gi
from hooks import IndicatorSpec

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


class IndicatorPlugin1(IndicatorSpec):
    """A hook implementation namespace.
    """

    @indicatorimpl
    def get_hook_menu(self, ):
        """Return a Gtk.MenuItem() array to be showed on App indicator (System tray)

		This method is the only one must be decorated. The others methods is used by this
        :return: new Menu Gtk.MenuItem
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