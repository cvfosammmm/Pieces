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


class TodolistView(Gtk.ScrolledWindow):
    
    def __init__(self):
        Gtk.ScrolledWindow.__init__(self)

        self.hbox = Gtk.HBox()
        self.vbox = Gtk.VBox()
        self.vbox.set_size_request(600, -1)

        self.todo_container = Gtk.VBox()
        self.todo_container.set_margin_top(52);
        self.todo_container.set_margin_bottom(62);

        self.done_container = Gtk.VBox()
        self.done_container.set_margin_bottom(66);

        self.vbox.pack_start(self.todo_container, False, False, 0)
        self.vbox.pack_start(self.done_container, False, False, 0)

        self.hbox.set_center_widget(self.vbox)
        self.add(self.hbox)

        self.show_all()

    def do_get_request_mode(self):
        return Gtk.SizeRequestMode.CONSTANT_SIZE
                     
    def do_get_preferred_width(self):
        return 400, 600


