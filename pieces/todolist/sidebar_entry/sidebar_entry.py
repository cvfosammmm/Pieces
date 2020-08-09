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

import pieces.todolist.sidebar_entry.sidebar_entry_viewgtk as sidebar_entry_view
from pieces.app.service_locator import ServiceLocator


class SidebarEntry(object):

    def __init__(self, todolist):
        self.todolist = todolist
        self.view = sidebar_entry_view.SidebarEntryView(todolist)
        self.view.title_label.set_text(todolist.get_title())
        self.view.todo_number_label.set_text(str(self.todolist.get_number_of_items_todo()))

        self.todolist.register_observer(self)

    '''
    *** notification handlers
    '''

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'title_changed':
            self.view.title_label.set_text(parameter)

        if change_code == 'new_item':
            self.view.todo_number_label.set_text(str(self.todolist.get_number_of_items_todo()))

        if change_code == 'item_state_changed':
            self.view.todo_number_label.set_text(str(self.todolist.get_number_of_items_todo()))

        if change_code == 'last_modified_changed':
            self.view.changed()


