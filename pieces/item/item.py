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
from gi.repository import GObject

import os.path
import os
import uuid
import pickle
import time

import pieces.item.item_viewgtk as item_view
import pieces.item.item_controller as item_controller
import pieces.item.item_presenter as item_presenter
from pieces.helpers.observable import Observable
from pieces.app.service_locator import ServiceLocator


class Item(Observable):

    def __init__(self, is_done, text, description=''):
        Observable.__init__(self)

        self.text = text
        self.description = description
        self.is_done = is_done

        self.highlight_start = -1

        self.view_todo = item_view.ItemViewTodo()
        self.view_done = item_view.ItemViewDone()
        self.controller = item_controller.ItemController(self, self.view_todo, self.view_done)
        self.presenter = item_presenter.ItemPresenter(self, self.view_todo, self.view_done)

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text
        self.add_change_code('text_changed', text)

    def set_description(self, description):
        self.description = description
        self.add_change_code('description_changed', description)

    def get_is_done(self):
        return self.is_done

    def set_is_done(self, is_done):
        if is_done != self.is_done:
            self.is_done = is_done
            self.add_change_code('is_done_changed', is_done)

    def highlight(self):
        self.highlight_start = time.time()
        GObject.timeout_add(5, self.update_highlight)

    def update_highlight(self):
        if time.time() - self.highlight_start < 1.25:
            time_factor = int(20 * self.ease(min(1.25 - (time.time() - self.highlight_start), 0.25) * 4))
            for i in range(1,21):
                if i == time_factor:
                    self.view_todo.hbox.get_style_context().add_class('yellow' + str(i))
                else:
                    self.view_todo.hbox.get_style_context().remove_class('yellow' + str(i))
            self.view_todo.queue_draw()
            return True
        else:
            for i in range(1,21):
                self.view_todo.hbox.get_style_context().remove_class('yellow' + str(i))
            self.view_todo.queue_draw()
            return False

    def ease(self, factor): return (factor - 1)**3 + 1

    def get_markdown(self):
        return '- [' + ('x' if self.is_done else ' ') + '] ' + self.text


