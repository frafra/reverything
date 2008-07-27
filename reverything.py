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

''' Rename multiple files and/or directories using 2 regex
    Syntax example: 'dsc(\d+)' -> 'photo-%(1)s' % {'1':res.group(0)}
    See also: http://docs.python.org/lib/re-syntax.html'''

import os, re, sys

class Reverything:
    ''' Rename multiple files and/or directories using 2 regex '''
    def __init__(self, regex_in, regex_out, dirs):
        self.regex_in, self.regex_out = regex_in, regex_out
        self.dirs = dirs
        self.map = {}
    def preview(self):
        ''' Get a map with current names and new names over directories '''
        # How to store data: {directory1:{file1:new1, file2:new2}}
        self.map = {}
        for folder in self.dirs:
            tmp = {}
            for item in os.listdir(folder):
                res = re.search(self.regex_in, item)
                if not res:
                    continue
                res = res.groups()
                replace = dict((str(e+1), i) for e, i in enumerate(res))
                tmp[item] = self.regex_out % replace
            if tmp:
                self.map[folder] = tmp
    def apply(self):
        ''' Rename everything '''
        for folder in self.map:
            for item in self.map[folder]:
                os.rename(os.path.join(folder, item),
                          os.path.join(folder, self.map[folder][item]))

def main():
    ''' Example code for use Reverything class '''
    if len(sys.argv) < 3:
        print 'Usage: %s <filter> <name> [directories]' % sys.argv[0]
        sys.exit(0)
    if len(sys.argv) < 4:
        dirs = [os.getcwd()]
    else:
        dirs = sys.argv[3:]
    rename = Reverything(sys.argv[1], sys.argv[2], dirs)
    rename.preview()
    if rename.map:
        for folder in rename.map:
            print 'Preview (into %s):' % folder
            for item in rename.map[folder]:
                print '    %s -> %s' % (item, rename.map[folder][item])
        if raw_input('Rename? [y/n] ').lower() == 'y':
            rename.apply()
    else:
        print 'Nothing to rename.'

if __name__ == '__main__':
    main()

