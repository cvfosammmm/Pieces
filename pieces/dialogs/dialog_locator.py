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

import pieces.dialogs.about.about as about_dialog
import pieces.dialogs.preferences.preferences as preferences_dialog
import pieces.dialogs.keyboard_shortcuts.keyboard_shortcuts as keyboard_shortcuts_dialog
import pieces.dialogs.delete_todolist_confirmation.delete_todolist_confirmation as delete_todolist_confirmation_dialog
import pieces.dialogs.rename_todolist.rename_todolist as rename_todolist_dialog


class DialogLocator(object):

    dialogs = dict()

    def init_dialogs(main_window, workspace):
        dialogs = dict()
        dialogs['about'] = about_dialog.AboutDialog(main_window)
        dialogs['preferences'] = preferences_dialog.PreferencesDialog(main_window)
        dialogs['keyboard_shortcuts'] = keyboard_shortcuts_dialog.KeyboardShortcutsDialog(main_window)
        dialogs['delete_todolist_confirmation'] = delete_todolist_confirmation_dialog.DeleteTodolistConfirmationDialog(main_window)
        dialogs['rename_todolist'] = rename_todolist_dialog.RenameTodolistDialog(main_window)
        DialogLocator.dialogs = dialogs
    
    def get_dialog(dialog_type):
        return DialogLocator.dialogs[dialog_type]


