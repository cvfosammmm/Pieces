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


class ItemPresenter(object):
    
    def __init__(self, item, view_todo, view_done):
        self.item = item
        self.view_todo = view_todo
        self.view_done = view_done

        self.view_todo.text_button.set_label(self.item.get_text())
        self.view_todo.text_entry.set_text(self.item.get_text())
        self.view_done.text_label.set_text(self.item.get_text())

        self.view_todo.set_reveal_child(not self.item.get_is_done())
        self.view_done.set_reveal_child(self.item.get_is_done())

        self.item.register_observer(self)

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'text_changed':
            self.view_todo.text_button.set_label(parameter)
            self.view_todo.text_entry.set_text(parameter)
            self.view_done.text_label.set_text(parameter)


