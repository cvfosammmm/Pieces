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
import uuid
import pickle
import shutil
import time

import pieces.todolist.todolist_controller as todolist_controller
import pieces.todolist.todolist_presenter as todolist_presenter
import pieces.todolist.todolist_viewgtk as todolist_view
import pieces.todolist.sidebar_entry.sidebar_entry as sidebar_entry
import pieces.todolist.entrybar_selection_entry.entrybar_selection_entry as entrybar_selection_entry
import pieces.item.item as item_model
from pieces.helpers.observable import Observable
from pieces.app.service_locator import ServiceLocator


class Todolist(Observable):

    def __init__(self, title, last_modified, items_todo=None, items_done=None):
        Observable.__init__(self)

        self.items_todo = items_todo if items_todo else list()
        self.items_done = items_done if items_done else list()
        self.last_modified = last_modified
        self.title = title

        for item in self.items_todo + self.items_done: item.register_observer(self)

        self.view = todolist_view.TodolistView()
        self.presenter = todolist_presenter.TodolistPresenter(self, self.view)
        self.sidebar_entry = sidebar_entry.SidebarEntry(self)
        self.entrybar_selection_entry = entrybar_selection_entry.EntrybarSelectionEntry(self)

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'is_done_changed':
            item = notifying_object
            if item.get_is_done():
                self.items_todo.remove(item)
                self.items_done.append(item)
            else:
                self.items_done.remove(item)
                self.items_todo.append(item)

            self.add_change_code('item_state_changed', item)
            self.set_last_modified()

        if change_code == 'text_changed':
            item = notifying_object
            self.add_change_code('item_text_changed', item)
            self.set_last_modified()

        if change_code == 'description_changed':
            item = notifying_object
            self.set_last_modified()

    def get_title(self):
        return self.title
        
    def set_title(self, title):
        self.title = title
        self.add_change_code('title_changed', title)
        self.set_last_modified()

    def get_last_modified(self):
        return self.last_modified

    def set_last_modified(self, date=None):
        if date == None:
            date = time.time()
        self.last_modified = date
        self.add_change_code('last_modified_changed')

    def get_number_of_items(self):
        return len(self.items_todo) + len(self.items_done)

    def get_number_of_items_done(self):
        return len(self.items_done)

    def get_number_of_items_todo(self):
        return len(self.items_todo)

    def create_item(self, text, description=None):
        item = item_model.Item(False, text, description)
        self.add_item(item)
        return item

    def add_item(self, item):
        if (item in self.items_todo) or (item in self.items_done): return False

        if item.get_is_done():
            self.items_done.append(item)
        else:
            self.items_todo.append(item)
        item.register_observer(self)
        self.add_change_code('new_item', item)
        self.set_last_modified()


