# -*- coding: utf-8 -*
__author__ = 'Joshua Muzhong Zhong'
__version__ = '0.1'

import idaapi
import idautils
import idc
import os
import sys
import re

try:
    # Python 2.
    xrange
except NameError:
    # Python 3.
    xrange = range

class JmcBatchRename(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = "batch rename subroutines' name"

    help = ""
    wanted_name = "JmcBatchRename"
    wanted_hotkey=""

    def __init__(self):
        super(JmcBatchRename, self).__init__()
        self._data = None
        self.view = None

    def init(self):
        print("dfadfadfasd1")
        return idaapi.PLUGIN_OK


    def run(self, arg):
        print("dfadfadfasd")
        return

    def term(self):
        self._data = None


# noinspection PyPep8Naming
def PLUGIN_ENTRY():
    return JmcBatchRename()
