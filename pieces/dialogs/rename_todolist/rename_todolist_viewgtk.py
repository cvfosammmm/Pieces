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
from gi.repository import Gtk, GLib
from gi.repository import Gdk


class RenameTodolistDialogView(object):

    def __init__(self, main_window):
        builder = Gtk.Builder.new_from_string('<?xml version="1.0" encoding="UTF-8"?><interface><object class="GtkDialog" id="dialog"><property name="use-header-bar">1</property></object></interface>', -1)

        self.dialog = builder.get_object('dialog')
        self.dialog.set_type_hint(Gdk.WindowTypeHint.DIALOG)
        self.dialog.set_modal(True)
        self.dialog.set_transient_for(main_window)
        self.dialog.set_destroy_with_parent(True)
        self.dialog.set_default_size(400, -1)
        self.dialog.set_can_focus(False)
        self.topbox = self.dialog.get_content_area()
        self.topbox.set_border_width(0)
        self.topbox.set_size_request(400, -1)
        
        self.create_headerbar()

        self.content = Gtk.VBox()
        self.content.set_margin_left(18)
        self.content.set_margin_right(18)

        label = Gtk.Label(_('Project Name'))
        label.set_xalign(0)
        label.set_margin_bottom(6)
        label.set_margin_top(18)
        label.get_style_context().add_class('dialog-entry-header')
        self.content.pack_start(label, False, False, 0)

        self.title_entry = Gtk.Entry()
        self.title_entry.set_margin_bottom(18)
        self.content.pack_start(self.title_entry, False, False, 0)

        self.topbox.pack_start(self.content, True, True, 0)
        self.topbox.show_all()

    def create_headerbar(self):
        self.headerbar = self.dialog.get_header_bar()
        self.headerbar.set_show_close_button(False)
        self.headerbar.set_title(_('Rename Project'))

        self.cancel_button = self.dialog.add_button(_('_Cancel'), Gtk.ResponseType.CANCEL)
        self.cancel_button.set_can_focus(False)
        
        self.rename_button = self.dialog.add_button(_('_Rename'), Gtk.ResponseType.APPLY)
        self.rename_button.set_can_focus(False)
        self.rename_button.get_style_context().add_class('suggested-action')
        
        self.headerbar.show_all()

    def run(self):
        return self.dialog.run()
        
    def __del__(self):
        self.dialog.destroy()


