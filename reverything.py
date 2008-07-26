#!/usr/bin/env python
# -*- utf-8 -*-
#
# reverything.py
#
# Copyright 2008 Francesco Frassinelli <fraph24@gmail.com>
# 
#    This file is part of Reverything.
#    
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from os import getcwd, listdir, path, rename
from re import search
from sys import argv

# Syntax like: '%(0)s' % {'0':res.group(0)}

class Reverything:
    def __init__(self, regex, name, directory=getcwd()):
        self.regex = regex
        self.name = name
        self.directory = directory
    def ls(self):
        items = {}
        for item in listdir(self.directory):
            re = search(self.regex, item)
            if not re: continue
            res = re.groups()
            replace = dict(zip([str(n) for n in xrange(len(res))], res))
            items[item] = self.name % replace
        return items
    def rename(self, items):
        for item in items:
            rename(path.join(self.directory, item),
                   path.join(self.directory, items[item]))

def main():
    if len(argv) not in (3, 4):
        print 'Usage: %s <filter> <name> [directory]' % argv[0]
        raise SystemExit
    
    rename = Reverything(*argv[1:])
    items = rename.ls()
    if len(items):
        print 'Preview (into %s):' % rename.directory
        for item in items:
            print '  %s -> %s' % (item, items[item])
    else:
        print 'Nothing to rename.'
        raise SystemExit
    
    if raw_input('Rename? [y/n] ').lower() == 'y': rename.rename(items)

if __name__ == "__main__":
    main()

