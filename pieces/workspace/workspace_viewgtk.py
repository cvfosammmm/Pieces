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
from gi.repository import Gdk
from gi.repository import Gtk
from gi.repository import Gio
from gi.repository import GLib

import pieces.workspace.headerbar.headerbar_viewgtk as headerbar_view
import pieces.workspace.sidebar.sidebar_viewgtk as sidebar_view
import pieces.workspace.entrybar.entrybar_viewgtk as entrybar_view
import pieces.workspace.welcome_page.welcome_page_viewgtk as welcome_page_view

from pieces.app.service_locator import ServiceLocator

import os


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, app, settings):
        Gtk.Window.__init__(self, application=app)
        self.app = app
        self.set_size_request(-1, 550)
        self.add_events(Gdk.EventMask.KEY_PRESS_MASK)
        resources_path = ServiceLocator.get_resources_path()
        app_icons_path = ServiceLocator.get_app_icons_path()
        Gtk.IconTheme.append_search_path(Gtk.IconTheme.get_default(), os.path.join(resources_path, 'icons'))
        Gtk.IconTheme.append_search_path(Gtk.IconTheme.get_default(), app_icons_path)

        # window state variables
        self.current_width = 0
        self.current_height = 0
        self.ismaximized = False

        # headerbar
        self.headerbar = headerbar_view.HeaderBar()
        self.set_titlebar(self.headerbar)

        # notebook
        self.notebook = DocumentViewWrapper()
        self.notebook.append_page(welcome_page_view.WelcomePageView())

        # entrybar
        self.entrybar = entrybar_view.EntrybarView()

        # wrapper
        self.wrapper = Gtk.VBox()
        self.wrapper.pack_start(self.notebook, True, True, 0)
        self.wrapper.pack_start(self.entrybar, False, False, 0)
        self.wrapper.set_size_request(636, -1)

        # sidebar
        self.sidebar = sidebar_view.Sidebar()
        self.sidebar_visible = None

        # paned
        self.sidebar_paned = Gtk.HPaned()
        self.sidebar_paned.pack1(self.sidebar, False, False)
        self.sidebar_paned.pack2(self.wrapper, True, False)
        self.sidebar_paned.get_style_context().add_class('sidebar_paned')
        self.add(self.sidebar_paned)

        # sync paneds
        self.sidebar_paned.bind_property('position', self.headerbar, 'position', 1)

        self.css_provider = Gtk.CssProvider()
        self.css_provider.load_from_path(os.path.join(resources_path, 'style_gtk.css'))
        self.style_context = Gtk.StyleContext()
        self.style_context.add_provider_for_screen(self.get_screen(), self.css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

        # actions
        self.new_project_action = Gio.SimpleAction.new('new-project', None)
        self.add_action(self.new_project_action)

        self.rename_project_action = Gio.SimpleAction.new('rename-project', None)
        self.add_action(self.rename_project_action)

        self.delete_project_action = Gio.SimpleAction.new('delete-project', None)
        self.add_action(self.delete_project_action)

        self.shortcuts_window_action = Gio.SimpleAction.new('show-shortcuts-window', None)
        self.add_action(self.shortcuts_window_action)

        self.show_preferences_action = Gio.SimpleAction.new('show-preferences-dialog', None)
        self.add_action(self.show_preferences_action)

        self.show_about_action = Gio.SimpleAction.new('show-about-dialog', None)
        self.add_action(self.show_about_action)

        self.quit_action = Gio.SimpleAction.new('quit', None)
        self.add_action(self.quit_action)

        dm_default = GLib.Variant.new_boolean(settings.get_value('preferences', 'prefer_dark_mode'))
        self.toggle_dark_mode_action = Gio.SimpleAction.new_stateful('toggle-dark-mode', None, dm_default)
        self.add_action(self.toggle_dark_mode_action)
        settings.gtksettings.get_default().set_property('gtk-application-prefer-dark-theme', dm_default)


class DocumentViewWrapper(Gtk.Notebook):

    def __init__(self):
        Gtk.Notebook.__init__(self)

        self.set_show_tabs(False)
        self.set_show_border(False)
        self.set_scrollable(True)

    def do_get_request_mode(self):
        return Gtk.SizeRequestMode.CONSTANT_SIZE
                     
    def do_get_preferred_width(self):
        return 440, 440


