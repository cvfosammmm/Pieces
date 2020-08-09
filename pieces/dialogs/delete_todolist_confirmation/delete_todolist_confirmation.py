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

from pieces.dialogs.dialog import Dialog


class DeleteTodolistConfirmationDialog(Dialog):

    def __init__(self, main_window):
        self.main_window = main_window

    def run(self, todolist):
        self.setup(todolist)
        response = self.view.run()
        if response == Gtk.ResponseType.YES:
            return_value = True
        else:
            return_value = False
        self.close()
        return return_value

    def setup(self, todolist):
        self.view = Gtk.MessageDialog(self.main_window, 0, Gtk.MessageType.QUESTION)

        no_items = todolist.get_number_of_items()
        no_items_done = todolist.get_number_of_items_done()
        no_items_todo = no_items - no_items_done
        self.view.set_property('text', 'Deleting »{title}« with {number_of_items_todo} open tasks.'.format(title=todolist.get_title(), number_of_items_todo=no_items_todo))
        self.view.format_secondary_markup('Do you really want to do this?')

        self.view.add_buttons('_Cancel', Gtk.ResponseType.CANCEL)
        delete_button = self.view.add_button('_Yes, delete this list', Gtk.ResponseType.YES)
        delete_button.get_style_context().add_class('destructive-action')
        self.view.set_default_response(Gtk.ResponseType.CANCEL)


