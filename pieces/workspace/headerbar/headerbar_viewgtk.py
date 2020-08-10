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

from pieces.app.service_locator import ServiceLocator


class HeaderBar(Gtk.Paned):

    def __init__(self):
        Gtk.Paned.__init__(self)

        button_layout = ServiceLocator.get_settings().button_layout

        show_close_button = True if (button_layout.find('close') < button_layout.find(':') and button_layout.find('close') >= 0) else False
        self.hb_left = HeaderBarLeft(show_close_button)
        
        show_close_button = True if (button_layout.find('close') > button_layout.find(':') and button_layout.find('close') >= 0) else False
        self.hb_right = HeaderBarRight(show_close_button)

        self.pack1(self.hb_left, False, False)
        self.pack2(self.hb_right, True, False)


class HeaderBarLeft(Gtk.HeaderBar):
        
    def __init__(self, show_close_button):
        Gtk.HeaderBar.__init__(self)
        self.pmb = ServiceLocator.get_popover_menu_builder()

        self.set_size_request(250, -1)
        self.set_show_close_button(show_close_button)


class HeaderBarRight(Gtk.HeaderBar):
        
    def __init__(self, show_close_button):
        Gtk.HeaderBar.__init__(self)
        self.pmb = ServiceLocator.get_popover_menu_builder()

        self.set_show_close_button(show_close_button)

        # workspace menu
        self.insert_workspace_menu()

    def insert_workspace_menu(self):
        popover = Gtk.PopoverMenu()
        stack = popover.get_child()

        box = Gtk.VBox()
        self.pmb.set_box_margin(box)
        self.pmb.add_action_button(box, _('Rename project...'), 'win.rename-todolist', keyboard_shortcut='F2')
        self.pmb.add_action_button(box, _('Delete project...'), 'win.delete-todolist')
        self.pmb.add_separator(box)
        self.pmb.add_menu_button(box, _('View'), 'view')
        self.pmb.add_separator(box)
        self.pmb.add_action_button(box, _('Preferences'), 'win.show-preferences-dialog')
        self.pmb.add_separator(box)
        self.pmb.add_action_button(box, _('Keyboard Shortcuts'), 'win.show-shortcuts-window')
        self.pmb.add_action_button(box, _('About'), 'win.show-about-dialog')
        self.pmb.add_separator(box)
        self.pmb.add_action_button(box, _('Quit'), 'win.quit', keyboard_shortcut=_('Ctrl') + '+Q')
        stack.add_named(box, 'main')
        box.show_all()

        # view submenu
        box = Gtk.VBox()
        self.pmb.set_box_margin(box)
        self.pmb.add_header_button(box, _('View'))
        self.pmb.add_action_button(box, _('Dark Mode'), 'win.toggle-dark-mode')
        stack.add_named(box, 'view')
        box.show_all()

        self.menu_button = Gtk.MenuButton()
        image = Gtk.Image.new_from_icon_name('open-menu-symbolic', Gtk.IconSize.BUTTON)
        self.menu_button.set_image(image)
        self.menu_button.set_can_focus(False)
        self.menu_button.set_popover(popover)
        self.pack_end(self.menu_button)


