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

from pieces.dialogs.dialog import Dialog
import pieces.dialogs.rename_project.rename_project_viewgtk as view


class RenameProjectDialog(Dialog):

    def __init__(self, main_window):
        self.main_window = main_window
        self.current_values = dict()
        self.validation_state = False

        self.view = view.RenameProjectDialogView(self.main_window)
        self.view.title_entry.connect('activate', self.on_title_entry_activate)
        self.view.title_entry.connect('changed', self.on_title_entry_changed)

    def run(self, todolist):
        self.init_current_values(todolist)
        self.view.title_entry.set_text(self.current_values['title'])
        self.setup()
        self.validate()

        self.view.rename_button.set_sensitive(self.validation_state)
        self.view.title_entry.select_region(0, len(self.current_values['title']))
        response = self.view.run()

        if response == Gtk.ResponseType.APPLY:
            todolist.set_title(self.current_values['title'])

        self.view.dialog.hide()

    def init_current_values(self, todolist):
        self.current_values['title'] = todolist.get_title()
    
    def setup(self):
        self.view.topbox.show_all()

    def on_title_entry_activate(self, entry=None):
        if self.validation_state == True:
            self.view.rename_button.clicked()

    def on_title_entry_changed(self, entry=None):
        self.set_title(entry.get_text())

    def set_title(self, title, notify=False):
        self.current_values['title'] = title
        self.validate()
        if notify:
            self.add_change_code('title_changed', title)

    def validate(self):
        validation_state = True
        if self.current_values['title'] == '':
            validation_state = False
        if validation_state != self.validation_state:
            self.validation_state = validation_state
            self.view.rename_button.set_sensitive(validation_state)


