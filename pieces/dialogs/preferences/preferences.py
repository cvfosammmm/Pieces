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
import pieces.dialogs.preferences.preferences_viewgtk as view
from pieces.app.service_locator import ServiceLocator


class PreferencesDialog(Dialog):

    def __init__(self, main_window):
        self.main_window = main_window
        self.settings = ServiceLocator.get_settings()

    def run(self):
        self.setup()
        self.view.run()
        del(self.view)

    def setup(self):
        self.view = view.Preferences(self.main_window)

        self.view.data_folder_chooser_button_label.set_text(self.settings.get_value('preferences', 'data_folder'))
        self.view.data_folder_chooser_button.connect('clicked', self.on_data_folder_chooser_clicked)

    def on_data_folder_chooser_clicked(self, button):
        action = Gtk.FileChooserAction.SELECT_FOLDER
        buttons = ('_Cancel', Gtk.ResponseType.CANCEL, '_Select', Gtk.ResponseType.APPLY)
        dialog = Gtk.FileChooserDialog('Select Folder', self.main_window, action, buttons)

        dialog.set_do_overwrite_confirmation(True)

        for widget in dialog.get_header_bar().get_children():
            if isinstance(widget, Gtk.Button) and widget.get_label() == '_Select':
                widget.get_style_context().add_class(Gtk.STYLE_CLASS_SUGGESTED_ACTION)
                widget.set_can_default(True)
                widget.grab_default()

        dialog.set_current_folder(self.settings.get_value('preferences', 'data_folder'))
        response = dialog.run()
        return_value = None
        if response == Gtk.ResponseType.APPLY:
            self.settings.set_value('preferences', 'data_folder', dialog.get_current_folder())
            self.view.data_folder_chooser_button_label.set_text(self.settings.get_value('preferences', 'data_folder'))
        dialog.hide()
        del(dialog)


