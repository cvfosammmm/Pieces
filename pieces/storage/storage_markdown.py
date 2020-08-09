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

import os
import shutil
import re
from pathlib import Path

import pieces.todolist.todolist as todolist_model
import pieces.item.item as item_model
from pieces.app.service_locator import ServiceLocator


class StorageMarkdown(object):

    def __init__(self, workspace):
        self.workspace = workspace
        self.pathname = ServiceLocator.get_data_folder()
        self.settings = ServiceLocator.get_settings()

        self.filenames = dict()

        try: os.mkdir(self.pathname)
        except FileExistsError: pass
        self.todolist_item_regex = re.compile('- \[(x| )\] (.*)')

    def populate_todolists(self):
        path = os.path.join(self.pathname, 'projects')
        try: os.mkdir(path)
        except FileExistsError: pass

        latest_modified_date = 0
        latest_modified = None
        for direntry in os.scandir(path):
            if direntry.is_file():
                filename = direntry.name
                title = filename.rsplit('.md', 1)[0].rsplit('~', 1)[0]
                last_modified = os.path.getmtime(direntry)

                with open(direntry, 'r') as file:
                    items_todo = []
                    items_done = []
                    for match in self.todolist_item_regex.finditer(file.read()):
                        text = match.group(2).strip()
                        is_done = True if match.group(1) == 'x' else False
                        item = item_model.Item(is_done, text)
                        if is_done:
                            items_done.append(item)
                        else:
                            items_todo.append(item)
                    items_todo.reverse()
                    items_done.reverse()

                    todolist = todolist_model.Todolist(title, last_modified, items_todo, items_done)
                    self.filenames[todolist] = filename
                    self.workspace.add_todolist(todolist)

                if last_modified > latest_modified_date:
                    latest_modified_date = last_modified
                    latest_modified = todolist

        if latest_modified != None:
            self.workspace.set_active_todolist(latest_modified)

    def init_writer(self):
        for todolist in self.workspace.todolists: todolist.register_observer(self)
        self.workspace.register_observer(self)
        self.settings.register_observer(self)

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'new_todolist':
            todolist = parameter
            filename = self.get_filename_from_title(todolist.get_title())
            self.filenames[todolist] = filename
            self.save_todolist(todolist)
            todolist.register_observer(self)

        if change_code == 'todolist_removed':
            todolist = parameter
            pathname = os.path.join(self.pathname, 'projects', self.filenames[todolist])
            os.remove(pathname)
            del(self.filenames[todolist])

        if change_code == 'title_changed':
            todolist = notifying_object
            title = parameter
            filename_old = self.filenames[todolist]
            filename_new = self.get_filename_from_title(title, filename_old)
            if filename_old != filename_new:
                pathname_old = os.path.join(self.pathname, 'projects', filename_old)
                pathname_new = os.path.join(self.pathname, 'projects', filename_new)
                os.rename(pathname_old, pathname_new)
                self.filenames[todolist] = filename_new

        if change_code == 'last_modified_changed':
            todolist = notifying_object
            self.save_todolist(todolist)

        if change_code == 'settings_changed' and parameter[0] == 'preferences' and parameter[1] == 'data_folder':
            old_pathname = self.pathname
            self.pathname = ServiceLocator.get_data_folder()
            shutil.move(os.path.join(old_pathname, 'projects'), os.path.join(self.pathname, 'projects'))

    def save_todolist(self, todolist):
        pathname = os.path.join(self.pathname, 'projects', self.filenames[todolist])
        try: filehandle = open(pathname, 'w')
        except IOError: pass
        else:
            for (i, item) in enumerate(reversed(todolist.items_done + todolist.items_todo)):
                if i == 0:
                    filehandle.write(item.get_markdown())
                else:
                    filehandle.write('\n' + item.get_markdown())

    def get_filename_from_title(self, title, filename_old=None):
        if filename_old != None and filename_old.split('.')[0].split('~')[0] == title:
            return filename_old
        if os.path.isfile(os.path.join(self.pathname, 'projects', title + '.md')):
            count = 2
            while os.path.isfile(os.path.join(self.pathname, 'projects', title + '~' + str(count) + '.md')):
                count += 1
            return title + '~' + str(count) + '.md'
        else:
            return title + '.md'


