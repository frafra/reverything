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

import os, re, sys

# Syntax example: 'dsc(\d+)' -> 'photo-%(1)s' % {'1':res.group(0)}
# See also: http://docs.python.org/lib/re-syntax.html

class Reverything:
    ''' Rename multiple files and/or directories using 2 regex '''
    def __init__(self, regex_in, regex_out, dirs):
        self.regex_in, self.regex_out = regex_in, regex_out
        self.dirs = dirs
    def preview(self):
        ''' See what files match with the given regex and memorize new names '''
        self.items = {}
        for d in self.dirs:
            # Calls re.search(self.regex_in, i), we should optimize it
            old = [i for i in os.listdir(d) if re.search(self.regex_in, i)]
            new = []
            for item in old:
                res = re.search(self.regex_in, item).groups()
                replace = dict(zip([str(n+1) for n in xrange(len(res))], res))
                new.append(self.regex_out % replace)
            self.items[d] = dict(zip(old, new))
        # We need to implement a cleanup action for empty results
    def apply(self):
        ''' Rename everything '''
        for d in self.items:
            for item in self.items[d]:
                os.rename(os.path.join(d, item),
                          os.path.join(d, self.items[d][item]))

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
    for d in rename.items:
        print 'Preview (into %s):' % d
        for item in rename.items[d]:
            print '    %s -> %s' % (item, rename.items[d][item])
    
    if raw_input('Rename? [y/n] ').lower() == 'y':
        rename.apply()

if __name__ == '__main__':
    main()

