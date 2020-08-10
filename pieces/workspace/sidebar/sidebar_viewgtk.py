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

import pieces.workspace.sidebar.create_todolist_popover.create_todolist_popover_viewgtk as create_todolist_popover_view


class Sidebar(Gtk.VBox):

    def __init__(self):
        Gtk.VBox.__init__(self)
        self.set_size_request(250, 500)
        
        self.get_style_context().add_class('sidebar')

        self.vbox = Gtk.VBox()

        self.list_fixed = Gtk.ListBox()
        self.list_fixed.set_can_focus(False)
        self.vbox.pack_start(self.list_fixed, False, False, 0)

        self.list_custom = Gtk.ListBox()
        self.list_custom.set_can_focus(False)
        self.vbox.pack_start(self.list_custom, True, True, 0)

        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.add(self.vbox)

        self.create_todolist_popover = create_todolist_popover_view.CreateTodolistPopoverView()

        self.action_bar = Gtk.ActionBar()
        self.create_list_button = Gtk.MenuButton()
        self.create_list_button.set_label(_('New List'))
        self.create_list_button.set_popover(self.create_todolist_popover)
        self.create_list_button.set_tooltip_text(_('Add List'))
        self.create_list_button.set_can_focus(False)
        self.action_bar.pack_start(self.create_list_button)

        self.pack_start(self.scrolled_window, True, True, 0)
        self.pack_start(self.action_bar, False, False, 0)

        self.show_all()


