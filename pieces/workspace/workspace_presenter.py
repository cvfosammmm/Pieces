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

import pieces.helpers.helpers as helpers
from pieces.app.service_locator import ServiceLocator


class WorkspacePresenter(object):

    def __init__(self, workspace):
        self.workspace = workspace
        self.main_window = ServiceLocator.get_main_window()
        self.workspace.register_observer(self)
        self.main_window.sidebar_paned.set_position(self.workspace.sidebar_position)

        self.main_window.delete_todolist_action.set_enabled(False)
        self.main_window.rename_todolist_action.set_enabled(False)

        for todolist in self.workspace.todolists:
            self.main_window.notebook.append_page(todolist.view)

        if self.workspace.active_todolist == None:
            self.show_welcome_page()
        else:
            self.show_todolist(self.workspace.active_todolist)

    '''
    *** notification handlers, get called by observed workspace
    '''

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'new_todolist':
            self.main_window.notebook.append_page(parameter.view)

        if change_code == 'todolist_removed':
            if len(self.workspace.todolists) == 0:
                self.show_welcome_page()
            self.main_window.notebook.remove(parameter.view)

        if change_code == 'new_active_todolist':
            self.show_todolist(parameter)

        if change_code == 'new_inactive_todolist':
            pass

        if change_code == 'set_dark_mode':
            ServiceLocator.get_settings().gtksettings.get_default().set_property('gtk-application-prefer-dark-theme', parameter)

    def show_todolist(self, todolist):
        page_number = self.main_window.notebook.page_num(todolist.view)
        todolist.view.get_vadjustment().set_value(0)
        self.main_window.notebook.set_current_page(page_number)
        self.main_window.delete_todolist_action.set_enabled(True)
        self.main_window.rename_todolist_action.set_enabled(True)
        self.main_window.entrybar.show_all()
        self.main_window.entrybar.text_entry.grab_focus()

    def show_welcome_page(self):
        self.main_window.delete_todolist_action.set_enabled(False)
        self.main_window.rename_todolist_action.set_enabled(False)
        self.main_window.entrybar.hide()


