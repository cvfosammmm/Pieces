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


class CreateTodolistPopoverController(object):
    
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.submit_button.connect('clicked', self.on_submit_button_clicked)
        self.view.title_entry.connect('activate', self.on_title_entry_activate)
        self.view.title_entry.connect('changed', self.on_title_entry_changed)
        self.view.cancel_button.connect('clicked', self.on_cancel_button_clicked)
        self.view.connect('closed', self.on_popover_closed)

    def on_submit_button_clicked(self, button=None):
        if self.model.validation_state == True:
            self.model.submit_todolist()
            self.view.popdown()

    def on_title_entry_activate(self, entry=None):
        if self.model.validation_state == True:
            self.model.submit_todolist()
            self.view.popdown()

    def on_title_entry_changed(self, entry=None):
        self.model.set_title(entry.get_text())

    def on_popover_closed(self, popover=None):
        self.model.reset()

    def on_cancel_button_clicked(self, button=None):
        self.view.popdown()


