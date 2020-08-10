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


class SidebarPresenter(object):
    
    def __init__(self, sidebar, view):
        self.sidebar = sidebar
        self.view = view
        self.sidebar.register_observer(self)
        self.view.project_list.set_sort_func(self.sort_func)

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'new_todolist':
            self.view.project_list.prepend(parameter.sidebar_entry.view)

        if change_code == 'todolist_removed':
            self.view.project_list.remove(parameter.sidebar_entry.view)

    def select_row_by_todolist(self, todolist):
        self.view.project_list.select_row(todolist.sidebar_entry.view)

    def sort_func(self, row1, row2):
        if row1.todolist.last_modified > row2.todolist.last_modified: return -1
        elif row1.todolist.last_modified < row2.todolist.last_modified: return 1
        else: return 0


