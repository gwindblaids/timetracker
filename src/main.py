#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk


class MainWindow(gtk.Window):
    """Main window class. Show on startup"""

    def __init__(self, title=__name__, ):
        """Create layouts and widgets for window object. Bind actions."""

        super().__init__(title=title)

        # ---------------------------------------------------------------------
        # create layouts
        self.general_layout = gtk.Box(spacing=6)
        self.left_menu_layout = gtk.VBox(spacing=30)
        self.left_menu_items_layout = gtk.VBox(spacing=20)
        self.center_layout = gtk.VBox(spacing=10)
        
        # ---------------------------------------------------------------------
        # packing layouts
        self.left_menu_layout.add(self.left_menu_items_layout)
        self.general_layout.add(self.left_menu_layout)
        self.general_layout.add(self.center_layout)
        self.add(self.general_layout)
       
        # ---------------------------------------------------------------------
        # create widgets
        self.menu_label = gtk.Label(label='Some text', xpad=23, ypad=24)
        self.menu_butt
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # packing widgets
        self.left_menu_layout.pack_start(self.menu_label, expand=True,
                                               fill=True, padding=20)
        # ---------------------------------------------------------------------

        self.connect('destroy', gtk.main_quit)
        self.show_all()




if __name__ == '__main__':
    main_window = MainWindow(title='test window')
    gtk.main()


