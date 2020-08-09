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

import os.path
import time
import pickle

from pieces.helpers.observable import Observable
import pieces.todolist.todolist as todolist_model
import pieces.workspace.workspace_presenter as workspace_presenter
import pieces.workspace.workspace_controller as workspace_controller
import pieces.workspace.sidebar.sidebar as sidebar
import pieces.workspace.entrybar.entrybar as entrybar
import pieces.workspace.headerbar.headerbar as headerbar
import pieces.workspace.keyboard_shortcuts.shortcuts as shortcuts
from pieces.app.service_locator import ServiceLocator


class Workspace(Observable):

    def __init__(self):
        Observable.__init__(self)

        self.todolists = list()
        self.active_todolist = None

        self.settings = ServiceLocator.get_settings()
        self.dark_mode = self.settings.get_value('preferences', 'prefer_dark_mode')

        self.headerbar = headerbar.Headerbar(self)
        self.sidebar = sidebar.Sidebar(self)
        self.sidebar_position = self.settings.get_value('window_state', 'sidebar_paned_position')
        self.entrybar = entrybar.Entrybar(self)
        self.shortcuts = shortcuts.Shortcuts()

    def init_workspace_controller(self):
        self.presenter = workspace_presenter.WorkspacePresenter(self)
        self.controller = workspace_controller.WorkspaceController(self)

    def create_todolist(self, title):
        last_modified = time.time()
        todolist = todolist_model.Todolist(title, last_modified)
        self.add_todolist(todolist)
        return todolist

    def add_todolist(self, todolist):
        if todolist in self.todolists: return False

        self.todolists.append(todolist)
        self.add_change_code('new_todolist', todolist)

    def remove_active_todolist(self):
        self.remove_todolist(self.get_active_todolist())

    def remove_todolist(self, todolist_rm):
        if todolist_rm == self.get_active_todolist():
            if len(self.todolists) > 1:
                self.todolists.sort(key=lambda todolist: todolist.last_modified)
                last_todolist = None
                use_next = False
                for todolist in self.todolists:
                    if use_next == True:
                        self.set_active_todolist(todolist)
                        break
                    elif todolist == todolist_rm:
                        if last_todolist != None:
                            self.set_active_todolist(last_todolist)
                            break
                        else:
                            use_next = True
                    last_todolist = todolist
            else:
                self.set_active_todolist(None)

        self.todolists.remove(todolist_rm)
        self.add_change_code('todolist_removed', todolist_rm)

    def get_active_todolist(self):
        return self.active_todolist
        
    def set_active_todolist(self, todolist):
        if self.active_todolist == todolist: return

        if self.active_todolist != None:
            self.add_change_code('new_inactive_todolist', self.active_todolist)
        self.active_todolist = todolist

        if self.active_todolist != None:
            self.add_change_code('new_active_todolist', todolist)

    def set_sidebar_position(self, sidebar_position):
        self.sidebar_position = sidebar_position

    def set_dark_mode(self, value):
        if self.dark_mode != value:
            self.dark_mode = value
            self.settings.set_value('preferences', 'prefer_dark_mode', self.dark_mode)
            self.add_change_code('set_dark_mode', value)


