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

from pieces.app.service_locator import ServiceLocator


class Headerbar(object):
    
    def __init__(self, workspace):
        self.workspace = workspace
        self.view = ServiceLocator.get_main_window().headerbar
        self.workspace.register_observer(self)
        self.view.hb_right.set_title('Pieces')

    '''
    *** notification handlers
    '''

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'todolist_removed':
            if len(self.workspace.todolists) == 0:
                self.view.hb_right.set_title('Pieces')

        if change_code == 'new_active_todolist':
            self.view.hb_right.set_title(parameter.get_title())
            parameter.register_observer(self)

        if change_code == 'new_inactive_todolist':
            parameter.unregister_observer(self)

        if change_code == 'title_changed':
            self.view.hb_right.set_title(parameter)


