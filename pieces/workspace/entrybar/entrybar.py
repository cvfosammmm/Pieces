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

import pieces.workspace.entrybar.entrybar_controller as entrybar_controller
import pieces.workspace.entrybar.entrybar_presenter as entrybar_presenter
from pieces.helpers.observable import Observable
from pieces.app.service_locator import ServiceLocator


class Entrybar(Observable):

    def __init__(self, workspace):
        Observable.__init__(self)

        self.workspace = workspace

        self.todolist = self.workspace.get_active_todolist()
        self.text = ''
        self.description = None

        self.validation_state = False

        self.view = ServiceLocator.get_main_window().entrybar
        self.controller = entrybar_controller.EntrybarController(self, self.view)
        self.presenter = entrybar_presenter.EntrybarPresenter(self, self.view)

        self.workspace.register_observer(self)

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'new_todolist':
            self.add_change_code('new_todolist', parameter)

        if change_code == 'todolist_removed':
            self.add_change_code('todolist_removed', parameter)

        if change_code == 'new_active_todolist':
            self.set_todolist(parameter)
            parameter.register_observer(self)

        if change_code == 'new_inactive_todolist':
            parameter.unregister_observer(self)

        if change_code == 'title_changed':
            self.add_change_code('todolist_title_changed', parameter)

    def set_todolist(self, todolist):
        if self.todolist != None:
            self.todolist.entrybar_selection_entry.set_is_selected(False)
        todolist.entrybar_selection_entry.set_is_selected(True)
        self.todolist = todolist
        self.add_change_code('todolist_changed', todolist)

    def set_text(self, text):
        self.text = text
        self.validate()
        self.add_change_code('text_changed', text)

    def set_description(self, description):
        self.description = description

    def validate(self):
        validation_state = True
        if self.text == '':
            validation_state = False
        if validation_state != self.validation_state:
            self.validation_state = validation_state
            self.add_change_code('validation_state_changed', validation_state)

    def submit_entry(self):
        self.todolist.create_item(self.text)
        self.reset()

    def reset(self):
        self.view.text_entry.set_text('')
        self.set_description(None)
        self.set_todolist(self.workspace.get_active_todolist())


