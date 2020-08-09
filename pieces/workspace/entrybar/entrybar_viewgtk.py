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

from pieces.app.service_locator import ServiceLocator


class EntrybarView(Gtk.HBox):

    def __init__(self):
        Gtk.HBox.__init__(self)
        self.get_style_context().add_class('entrybar')

        self.text_entry = Gtk.Entry()

        self.overlay_text = Gtk.Label('Add a task...')
        self.overlay_text.set_xalign(0)
        self.overlay_text.get_style_context().add_class('placeholder-text')
        self.overlay_text.set_margin_left(9)

        self.todolist_button = Gtk.MenuButton()
        self.todolist_button.set_can_focus(False)
        self.todolist_button_label = Gtk.Label()
        self.todolist_button_label.set_max_width_chars(10)
        self.todolist_button_label.set_size_request(100, -1)
        self.todolist_button_label.set_xalign(0)
        self.todolist_button_label.set_ellipsize(Pango.EllipsizeMode.END)
        self.todolist_button.add(self.todolist_button_label)

        self.todolist_popover = EntrybarTodolistPopoverView()
        self.todolist_button.set_popover(self.todolist_popover)

        self.placeholder_overlay = Gtk.Overlay()
        self.placeholder_overlay.add(self.text_entry)
        self.placeholder_overlay.add_overlay(self.overlay_text)
        self.placeholder_overlay.set_overlay_pass_through(self.overlay_text, True)

        box = Gtk.HBox()
        box.get_style_context().add_class('linked')
        box.pack_start(self.placeholder_overlay, True, True, 0)
        box.pack_start(self.todolist_button, False, False, 0)
        box.set_margin_right(6)

        self.submit_button = Gtk.Button.new_from_icon_name('keyboard-enter-symbolic', Gtk.IconSize.BUTTON)
        self.submit_button.set_tooltip_text('Add Item')
        self.submit_button.set_can_focus(False)

        self.pack_start(box, True, True, 0)
        self.pack_start(self.submit_button, False, False, 0)


class EntrybarTodolistPopoverView(Gtk.Popover):

    def __init__(self):
        Gtk.Popover.__init__(self)
        self.get_style_context().add_class('entrybar-todolist-popover')

        self.list = Gtk.ListBox()
        self.list.set_can_focus(False)
        self.list.set_selection_mode(Gtk.SelectionMode.NONE)

        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_size_request(250, 250)
        self.scrolled_window.set_margin_left(12)
        self.scrolled_window.set_margin_right(12)
        self.scrolled_window.set_margin_top(12)
        self.scrolled_window.set_margin_bottom(12)
        self.scrolled_window.add(self.list)

        self.add(self.scrolled_window)
        self.scrolled_window.show_all()


