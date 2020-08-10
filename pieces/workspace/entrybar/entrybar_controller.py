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
from gi.repository import Gdk


class EntrybarController(object):
    
    def __init__(self, entrybar, view):
        self.entrybar = entrybar
        self.view = view

        self.view.submit_button.connect('clicked', self.on_submit_button_clicked)
        self.view.text_entry.connect('activate', self.on_text_entry_activate)
        self.view.text_entry.connect('key-press-event', self.on_text_entry_key_press)
        self.view.text_entry.connect('changed', self.on_text_entry_changed)
        self.view.project_popover.list.connect('row-activated', self.on_row_activated)

    def on_row_activated(self, box, row):
        self.entrybar.set_todolist(row.todolist)
        self.view.project_popover.popdown()

    def on_submit_button_clicked(self, button=None):
        if self.entrybar.validation_state == True:
            self.entrybar.submit_entry()

    def on_text_entry_activate(self, entry=None):
        if self.entrybar.validation_state == True:
            self.entrybar.submit_entry()

    def on_text_entry_key_press(self, entry, event):
        if event.keyval == Gdk.keyval_from_name('Tab'):
            return True
        elif event.keyval == Gdk.keyval_from_name('ISO_Left_Tab'):
            return True
        elif event.keyval == Gdk.keyval_from_name('Up'):
            return True
        elif event.keyval == Gdk.keyval_from_name('Down'):
            return True
        return False

    def on_text_entry_changed(self, entry=None):
        self.entrybar.set_text(entry.get_text())


