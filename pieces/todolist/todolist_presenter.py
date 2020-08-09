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
from gi.repository import Gtk

import pieces.helpers.helpers as helpers
from pieces.app.service_locator import ServiceLocator


class TodolistPresenter(object):
    
    def __init__(self, todolist, todolist_view):
        self.todolist = todolist
        self.view = todolist_view

        for item in self.todolist.items_todo:
            self.view.todo_container.pack_end(item.view_todo, False, False, 0)

        for item in self.todolist.items_done:
            self.view.done_container.pack_end(item.view_done, False, False, 0)

        self.todolist.register_observer(self)

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'new_item':
            item = parameter
            self.view.todo_container.pack_end(item.view_todo, False, False, 0)
            self.view.done_container.pack_end(item.view_done, False, False, 0)
            if not item.get_is_done():
                self.view.emit('scroll-child', Gtk.ScrollType.START, 0)
                item.highlight()

        if change_code == 'item_state_changed':
            item = parameter
            if item.get_is_done():
                self.view.done_container.remove(item.view_done)
                self.view.done_container.pack_end(item.view_done, False, False, 0)
                item.view_todo.set_reveal_child(False)
                item.view_done.set_reveal_child(True)
            else:
                self.view.todo_container.remove(item.view_todo)
                self.view.todo_container.pack_end(item.view_todo, False, False, 0)
                item.view_todo.set_reveal_child(True)
                item.view_done.set_reveal_child(False)
                self.view.emit('scroll-child', Gtk.ScrollType.START, 0)
                item.highlight()

        if change_code == 'item_text_changed':
            item = parameter
            pass


