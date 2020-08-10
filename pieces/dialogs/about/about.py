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
from pieces.app.service_locator import ServiceLocator


class AboutDialog(Dialog):

    def __init__(self, main_window):
        self.main_window = main_window

    def run(self):
        self.setup()
        self.view.show_all()
        del(self.view)

    def setup(self):
        self.view = Gtk.AboutDialog()
        self.view.set_transient_for(self.main_window)
        self.view.set_modal(True)
        self.view.set_program_name('Pieces')
        self.view.set_version(ServiceLocator.get_pieces_version())
        self.view.set_copyright('Copyright © 2018-2020')
        self.view.set_comments(_('Pieces is a personal task manager.'))
        self.view.set_license_type(Gtk.License.GPL_3_0)
        self.view.set_website('https://www.cvfosammmm.org/pieces/')
        self.view.set_website_label('https://www.cvfosammmm.org/pieces/')
        self.view.set_authors(('Robert Griesel',))
        self.view.set_logo_icon_name('org.cvfosammmm.Pieces')
        

