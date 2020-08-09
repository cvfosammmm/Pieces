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

import os.path
from xdg.BaseDirectory import xdg_config_home
from xdg.BaseDirectory import *

import pieces.app.settings as settingscontroller
import pieces.helpers.popover_menu_builder as popover_menu_builder


class ServiceLocator(object):

    settings = None
    pieces_version = None
    resources_path = None
    app_icons_path = None
    popover_menu_builder = None

    def init_main_window(main_window):
        ServiceLocator.main_window = main_window

    def get_main_window():
        return ServiceLocator.main_window

    def get_settings():
        if ServiceLocator.settings == None:
            ServiceLocator.settings = settingscontroller.Settings(ServiceLocator.get_config_folder())
        return ServiceLocator.settings

    def get_popover_menu_builder():
        if ServiceLocator.popover_menu_builder == None:
            ServiceLocator.popover_menu_builder = popover_menu_builder.PopoverMenuBuilder()
        return ServiceLocator.popover_menu_builder

    def get_config_folder():
        return os.path.join(xdg_config_home, 'Pieces')

    def get_data_folder():
        return ServiceLocator.get_settings().get_value('preferences', 'data_folder')

    def init_pieces_version(pieces_version):
        ServiceLocator.pieces_version = pieces_version

    def get_pieces_version():
        return ServiceLocator.pieces_version

    def init_resources_path(resources_path):
        ServiceLocator.resources_path = resources_path

    def get_resources_path():
        return ServiceLocator.resources_path

    def init_app_icons_path(app_icons_path):
        ServiceLocator.app_icons_path = app_icons_path

    def get_app_icons_path():
        return ServiceLocator.app_icons_path


