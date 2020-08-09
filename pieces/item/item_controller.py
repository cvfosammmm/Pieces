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

from pieces.app.service_locator import ServiceLocator


class ItemController(object):
    
    def __init__(self, item, view_todo, view_done):
        self.item = item
        self.view_todo = view_todo
        self.view_done = view_done

        self.view_todo.check_button.connect('clicked', self.on_todo_check_button_clicked)
        self.view_done.check_button.connect('clicked', self.on_done_check_button_clicked)
        self.view_todo.text_button.connect('clicked', self.on_text_edit_button_clicked)
        self.view_todo.text_entry.connect('changed', self.on_text_entry_changed)
        self.view_todo.text_entry.connect('activate', self.on_text_entry_activate)
        self.view_todo.text_entry.connect('focus-out-event', self.on_text_entry_focus_out)

    def on_todo_check_button_clicked(self, button):
        self.item.set_is_done(True)
        button.set_active(False)

    def on_done_check_button_clicked(self, button):
        self.item.set_is_done(False)
        button.set_active(True)

    def on_text_edit_button_clicked(self, button):
        self.view_todo.stack.set_visible_child_name('edit')
        self.view_todo.text_entry.grab_focus()

    def on_text_entry_changed(self, entry):
        self.item.set_text(entry.get_text())

    def on_text_entry_activate(self, entry):
        ServiceLocator.get_main_window().entrybar.text_entry.grab_focus()

    def on_text_entry_focus_out(self, entry, event):
        self.view_todo.stack.set_visible_child_name('text')


