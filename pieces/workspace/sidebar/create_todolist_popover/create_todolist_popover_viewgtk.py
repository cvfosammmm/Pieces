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


class CreateTodolistPopoverView(Gtk.Popover):

    def __init__(self):
        Gtk.Popover.__init__(self)

        self.box = Gtk.VBox()
        self.box.set_margin_left(18)
        self.box.set_margin_right(18)
        self.box.set_margin_top(18)
        self.box.set_margin_bottom(18)

        self.header = Gtk.Label('List Name')
        self.header.set_xalign(0)
        self.header.set_margin_bottom(6)
        self.header.get_style_context().add_class('popover-dialog-header')

        self.title_entry = Gtk.Entry()
        self.title_entry.set_margin_bottom(18)
        self.title_entry.set_size_request(300, -1)

        self.button_box = Gtk.HBox()
        self.cancel_button = Gtk.Button.new_with_label('Cancel')
        self.cancel_button.set_size_request(132, -1)
        self.submit_button = Gtk.Button.new_with_label('Create List')
        self.submit_button.set_margin_left(12)
        self.submit_button.set_size_request(156, -1)
        self.submit_button.get_style_context().add_class('suggested-action')
        self.button_box.pack_start(self.cancel_button, False, False, 0)
        self.button_box.pack_start(self.submit_button, False, False, 0)

        self.box.pack_start(self.header, False, False, 0)
        self.box.pack_start(self.title_entry, False, False, 0)
        self.box.pack_start(self.button_box, False, False, 0)
        self.add(self.box)

        self.box.show_all()


