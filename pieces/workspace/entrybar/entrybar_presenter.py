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


class EntrybarPresenter(object):
    
    def __init__(self, entrybar, view):
        self.entrybar = entrybar
        self.view = view
        self.entrybar.register_observer(self)
        self.view.project_popover.list.set_sort_func(self.sort_func)

        self.view.submit_button.set_sensitive(False)

        self.view.text_entry.grab_focus()

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'text_changed':
            if parameter == '':
                self.view.overlay_text.show_all()
            else:
                self.view.overlay_text.hide()

        if change_code == 'todolist_changed':
            self.view.project_button_label.set_text(parameter.get_title())

        if change_code == 'todolist_title_changed':
            self.view.project_button_label.set_text(self.entrybar.todolist.get_title())

        if change_code == 'validation_state_changed':
            self.view.submit_button.set_sensitive(parameter)

        if change_code == 'new_todolist':
            self.view.project_popover.list.prepend(parameter.entrybar_selection_entry.view)

        if change_code == 'todolist_removed':
            self.view.project_popover.list.remove(parameter.entrybar_selection_entry.view)

    def sort_func(self, row1, row2):
        if row1.todolist.last_modified > row2.todolist.last_modified: return -1
        elif row1.todolist.last_modified < row2.todolist.last_modified: return 1
        else: return 0


