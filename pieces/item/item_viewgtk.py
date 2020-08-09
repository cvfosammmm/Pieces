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


class ItemViewTodo(Gtk.Revealer):
    
    def __init__(self):
        Gtk.Revealer.__init__(self)

        self.hbox = Gtk.HBox()
        self.hbox.get_style_context().add_class('item-todo')

        self.check_button = Gtk.CheckButton()
        self.check_button.set_can_focus(False)
        self.check_button.set_margin_right(5)
        self.check_button.get_style_context().add_class('check')

        self.stack = Gtk.Stack()

        box = Gtk.HBox()
        self.text_button = Gtk.Button.new_with_label('')
        self.text_button.set_can_focus(False)
        self.text_button.get_style_context().add_class('text-label')
        box.pack_start(self.text_button, False, False, 0)
        self.stack.add_named(box, 'text')

        self.text_entry = Gtk.Entry()
        self.text_entry.set_size_request(574, -1)
        self.stack.add_named(self.text_entry, 'edit')

        self.hbox.pack_start(self.check_button, False, False, 0)
        self.hbox.pack_start(self.stack, False, False, 0)

        self.add(self.hbox)
        self.show_all()


class ItemViewDone(Gtk.Revealer):
    
    def __init__(self):
        Gtk.Revealer.__init__(self)

        self.hbox = Gtk.HBox()
        self.hbox.get_style_context().add_class('item-done')

        self.check_button = Gtk.CheckButton()
        self.check_button.set_can_focus(False)
        self.check_button.set_margin_right(14)
        self.check_button.get_style_context().add_class('flat')
        self.check_button.set_active(True)
        self.text_label = Gtk.Label()
        self.text_label.set_xalign(0)

        self.hbox.pack_start(self.check_button, False, False, 0)
        self.hbox.pack_start(self.text_label, True, True, 0)

        self.add(self.hbox)
        self.show_all()


