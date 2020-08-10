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

import pieces.workspace.sidebar.create_project_popover.create_project_popover_controller as create_project_popover_controller
import pieces.workspace.sidebar.create_project_popover.create_project_popover_presenter as create_project_popover_presenter
from pieces.helpers.observable import Observable
from pieces.app.service_locator import ServiceLocator


class CreateProjectPopover(Observable):

    def __init__(self, workspace):
        Observable.__init__(self)

        self.workspace = workspace

        self.title = ''

        self.validation_state = False

        self.view = ServiceLocator.get_main_window().sidebar.create_project_popover
        self.controller = create_project_popover_controller.CreateProjectPopoverController(self, self.view)
        self.presenter = create_project_popover_presenter.CreateProjectPopoverPresenter(self, self.view)

    def set_title(self, title, notify=False):
        self.title = title
        self.validate()
        if notify:
            self.add_change_code('title_changed', title)

    def validate(self):
        validation_state = True
        if self.title == '':
            validation_state = False
        if validation_state != self.validation_state:
            self.validation_state = validation_state
            self.add_change_code('validation_state_changed', validation_state)

    def submit_todolist(self):
        todolist = self.workspace.create_todolist(self.title)
        self.workspace.set_active_todolist(todolist)

    def reset(self):
        self.set_title('', notify=True)

    def run(self):
        self.view.popup()


