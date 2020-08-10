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


class WelcomePageView(Gtk.ScrolledWindow):

    def __init__(self):
        Gtk.ScrolledWindow.__init__(self)

        self.set_hexpand(True)
        self.get_style_context().add_class('welcomepageview')

        self.box = Gtk.VBox()
        self.add(self.box)
        self.viewport = self.get_children().pop()
        
        self.welcome_message = Gtk.Label()
        self.welcome_message.set_text(_('Pieces is a todolist manager.\n\nTo make a list, click "New List" in the lower left corner.'))
        self.welcome_message.set_justify(Gtk.Justification.CENTER)
        self.welcome_message.set_size_request(400, 50)
        
        self.welcome_box = Gtk.VBox()
        self.welcome_box.set_size_request(400, 50)
        self.welcome_box.pack_start(self.welcome_message, False, False, 0)
        self.welcome_box_wrapper = Gtk.HBox()
        self.welcome_box_wrapper.set_center_widget(self.welcome_box)
        self.box.set_center_widget(self.welcome_box_wrapper)

    def set_sidebar_visible(self, sidebar_visible):
        pass


