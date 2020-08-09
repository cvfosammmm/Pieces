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
from gi.repository import Gio

import pieces.workspace.sidebar.sidebar_controller as sidebar_controller
import pieces.workspace.sidebar.sidebar_presenter as sidebar_presenter
import pieces.workspace.sidebar.create_todolist_popover.create_todolist_popover as create_todolist_popover_model
from pieces.helpers.observable import Observable
from pieces.app.service_locator import ServiceLocator


class Sidebar(Observable):

    def __init__(self, workspace):
        Observable.__init__(self)

        self.workspace = workspace
        self.todolist = None

        self.view = ServiceLocator.get_main_window().sidebar
        self.controller = sidebar_controller.SidebarController(self, self.view)
        self.presenter = sidebar_presenter.SidebarPresenter(self, self.view)

        self.create_todolist_popover = create_todolist_popover_model.CreateTodolistPopover(workspace)

        self.workspace.register_observer(self)

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'new_todolist':
            self.add_change_code(change_code, parameter)

        if change_code == 'todolist_removed':
            self.add_change_code(change_code, parameter)

        if change_code == 'new_active_todolist':
            self.set_todolist(parameter)

    def set_todolist(self, todolist):
        self.todolist = todolist
        self.workspace.set_active_todolist(todolist)
        self.presenter.select_row_by_todolist(todolist)


