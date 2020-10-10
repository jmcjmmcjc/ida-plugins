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

def jmc_list_func_name():
    ea = idc.here();
    while True:
        ea = idc.get_next_func(ea)
        if ea == 0xffffffffL:
            print("There is no func!")
            break

        print(idc.GetFunctionName(ea))


def jmc_list_func_prefix_with(prefix=""):
    if not prefix:
        print("prefix is space")
        return

    for ea in idautils.Functions():
        func_name = idc.GetFunctionName(ea)
        if func_name.startswith(prefix):
            print("%s, %s" %(hex(ea), func_name))


def jmc_find_and_rename_func_prefix_with(prefix="", new_prefix=""):
    if not prefix or not new_prefix:
        print("prefix or new_prefix is space")
        return
    
    for ea in idautils.Functions():
        func_name = idc.GetFunctionName(ea)
        if func_name.startswith(prefix):
            new_func_name = func_name.replace(prefix, new_prefix)
            print("%s, %s -> %s" %(hex(ea), func_name, new_func_name))
            idaapi.set_name(ea, new_func_name, idaapi.SN_CHECK)


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
