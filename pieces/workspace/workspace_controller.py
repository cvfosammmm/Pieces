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
from gi.repository import GLib

from pieces.app.service_locator import ServiceLocator
from pieces.dialogs.dialog_locator import DialogLocator


class WorkspaceController(object):
    ''' Mediator between workspace and view. '''
    
    def __init__(self, workspace):

        self.workspace = workspace
        self.main_window = ServiceLocator.get_main_window()

        self.s_allocation = 0

        self.main_window.new_project_action.connect('activate', self.on_new_project_action_activated)
        self.main_window.rename_project_action.connect('activate', self.on_rename_project_action_activated)
        self.main_window.delete_project_action.connect('activate', self.on_delete_project_action_activated)
        self.main_window.shortcuts_window_action.connect('activate', self.show_shortcuts_window)
        self.main_window.show_preferences_action.connect('activate', self.show_preferences_dialog)
        self.main_window.show_about_action.connect('activate', self.show_about_dialog)
        self.main_window.toggle_dark_mode_action.connect('activate', self.on_dark_mode_toggle_toggled)

        self.main_window.sidebar.connect('size-allocate', self.on_sidebar_size_allocate)

    '''
    *** signal handlers
    '''

    def on_dark_mode_toggle_toggled(self, action, parameter=None):
        new_state = not action.get_state().get_boolean()
        action.set_state(GLib.Variant.new_boolean(new_state))
        self.workspace.set_dark_mode(new_state)

    def on_sidebar_size_allocate(self, sidebar, allocation):
        if allocation.width != self.s_allocation:
            self.s_allocation = allocation.width
            self.workspace.set_sidebar_position(allocation.width)

    '''
    *** actions
    '''

    def show_shortcuts_window(self, action, parameter=''):
        DialogLocator.get_dialog('keyboard_shortcuts').run()

    def show_preferences_dialog(self, action=None, parameter=''):
        DialogLocator.get_dialog('preferences').run()

    def show_about_dialog(self, action, parameter=''):
        DialogLocator.get_dialog('about').run()

    def on_new_project_action_activated(self, action=None, parameter=''):
        self.main_window.sidebar.create_list_button.clicked()

    def on_rename_project_action_activated(self, action=None, parameter=''):
        todolist = self.workspace.get_active_todolist()
        DialogLocator.get_dialog('rename_project').run(todolist)

    def on_delete_project_action_activated(self, action=None, parameter=''):
        todolist = self.workspace.get_active_todolist()
        if DialogLocator.get_dialog('delete_project_confirmation').run(todolist):
            self.workspace.remove_active_todolist()


