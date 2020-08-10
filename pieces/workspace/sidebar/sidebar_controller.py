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


class SidebarController(object):
    
    def __init__(self, sidebar, view):
        self.sidebar = sidebar
        self.view = view

        self.view.list_fixed.connect('row-selected', self.on_row_selected)
        self.view.project_list.connect('row-selected', self.on_row_selected)

    def on_row_selected(self, box, row):
        if row != None:
            if box == self.view.list_fixed:
                self.view.project_list.unselect_all()
            else:
                self.view.list_fixed.unselect_all()
            self.sidebar.set_todolist(row.todolist)


