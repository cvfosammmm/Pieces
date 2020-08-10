#!/usr/bin/env python3
# coding: utf-8

# Copyright (C) 2017, 2018 Robert Griesel
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Pango


class Preferences(object):
    ''' Preferences dialog. '''

    def __init__(self, main_window):
        builder = Gtk.Builder.new_from_string('<?xml version="1.0" encoding="UTF-8"?><interface><object class="GtkDialog" id="dialog"><property name="use-header-bar">1</property></object></interface>', -1)

        self.dialog = builder.get_object('dialog')
        self.dialog.set_destroy_with_parent(True)
        self.dialog.set_type_hint(Gdk.WindowTypeHint.DIALOG)
        self.dialog.set_modal(True)
        self.dialog.set_transient_for(main_window)
        self.dialog.set_can_focus(False)
        self.dialog.set_size_request(400, 250)
        self.dialog.set_default_size(400, 250)
        
        self.headerbar = self.dialog.get_header_bar()
        self.headerbar.set_title(_('Preferences'))

        self.topbox = self.dialog.get_content_area()
        self.topbox.set_border_width(0)

        self.notebook = Gtk.Notebook()
        self.notebook.set_show_tabs(True)
        self.notebook.set_show_border(False)
        self.topbox.pack_start(self.notebook, True, True, 0)

        self.build_page_general()

        self.notebook.append_page(self.page_general, Gtk.Label(_('General')))

        self.dialog.show_all()

    def build_page_general(self):
        self.page_general = Gtk.VBox()
        self.page_general.set_margin_start(18)
        self.page_general.set_margin_end(18)
        self.page_general.set_margin_top(18)
        self.page_general.set_margin_bottom(18)
        self.page_general.get_style_context().add_class('preferences-page')

        label = Gtk.Label()
        label.set_markup('<b>' + _('Storage') + '</b>')
        label.set_xalign(0)
        label.set_margin_bottom(6)
        self.page_general.pack_start(label, False, False, 0)

        box = Gtk.HBox()
        label = Gtk.Label(_('Data folder:'))
        label.set_xalign(0)
        label.set_margin_right(12)
        box.pack_start(label, False, False, 0)
        self.data_folder_chooser_button = Gtk.Button()
        self.data_folder_chooser_button_widget = Gtk.HBox()
        self.data_folder_chooser_button_label = Gtk.Label('')
        self.data_folder_chooser_button_label.set_ellipsize(Pango.EllipsizeMode.START)
        self.data_folder_chooser_button_widget.pack_end(Gtk.Image.new_from_icon_name('document-open-symbolic', Gtk.IconSize.BUTTON), False, False, 0)
        self.data_folder_chooser_button_widget.pack_start(self.data_folder_chooser_button_label, False, False, 0)
        self.data_folder_chooser_button.add(self.data_folder_chooser_button_widget)
        box.pack_start(self.data_folder_chooser_button, True, True, 0)

        self.page_general.pack_start(box, False, False, 0)

    def run(self):
        return self.dialog.run()
        
    def response(self, args):
        self.dialog.response(args)
        
    def __del__(self):
        self.dialog.destroy()
        


