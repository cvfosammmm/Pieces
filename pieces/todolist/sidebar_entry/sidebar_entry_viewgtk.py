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
from gi.repository import Pango


class SidebarEntryView(Gtk.ListBoxRow):

    def __init__(self, todolist):
        Gtk.ListBoxRow.__init__(self)
        self.get_style_context().add_class('sidebar-entry')
        self.set_can_focus(False)

        self.todolist = todolist

        self.hbox = Gtk.HBox()

        self.title_label = Gtk.Label()
        self.title_label.set_xalign(0)
        self.title_label.set_ellipsize(Pango.EllipsizeMode.END)

        self.todo_number_label = Gtk.Label()
        self.todo_number_label.get_style_context().add_class('todo-number')

        self.hbox.pack_start(self.title_label, True, True, 0)
        self.hbox.pack_end(self.todo_number_label, False, False, 0)
        self.add(self.hbox)

        self.show_all()


