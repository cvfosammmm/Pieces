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


class CreateTodolistPopoverPresenter(object):
    
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.model.register_observer(self)

        self.view.submit_button.set_sensitive(False)

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'title_changed':
            self.view.title_entry.set_text(parameter)

        if change_code == 'validation_state_changed':
            self.view.submit_button.set_sensitive(parameter)

