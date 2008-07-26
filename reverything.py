#!/usr/bin/env python
# -*- utf-8 -*-
#
# reverything.py
#
# Copyright 2008 Francesco Frassinelli <fraph24@gmail.com>
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

from os import getcwd, listdir, rename
from re import search
from sys import argv

def main():
    if len(argv) not in (3, 4):
        print 'Usage: %s <filter> <name> [working directory]' % argv[0]
        raise SystemExit

    regex = argv[1]
    name = argv[2]
    if len(argv) == 4:
        workingdir = argv[3]
    else:
        workingdir = getcwd()

    items = {}
    for item in listdir(workingdir):
        res = search(regex, item)
        if res:
            # Syntax like: '%(0)s' % {'0':res.group(0)}
            groups = res.groups()
            replace = dict(zip([str(n) for n in xrange(len(groups))], groups))
            items[item] = name % replace

    if len(items) > 0:
        print 'Preview:'
        for item in items:
            print '  %s -> %s' % (item, items[item])
    else:
        print 'Nothing to rename.'
        raise SystemExit
    
    if raw_input('Rename? [y/n] ').lower() != 'y': raise SystemExit

    for item in items:
        rename(item, items[item])

if __name__ == "__main__":
    main()

