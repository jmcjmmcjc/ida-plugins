# -*- coding: utf-8 -*
__author__ = 'Joshua Muzhong Zhong'
__version__ = '0.1'

import idaapi
import idautils
import idc


def list_func():
    for ea in idautils.Functions():
        print("%s, %s" %(hex(ea), idc.GetFunctionName(ea)))


def list_func_from_current_ea():
    ea = idc.here()
    while True:
        ea = idc.get_next_func(ea)
        if ea == idc.BADADDR:
            print("There is no other functions!")
            break

        print(idc.GetFunctionName(ea))


def list_func_prefix(prefix=""):
    if not prefix:
        print("prefix is spaces!")
        return

    for ea in idautils.Functions():
        func_name = idc.GetFunctionName(ea)
        if func_name.startswith(prefix):
            print("%s, %s" %(hex(ea), func_name))


def find_and_rename_func_prefix(prefix="", new_prefix=""):
    if not prefix or not new_prefix:
        print("prefix or new_prefix is spaces!")
        return
    
    for ea in idautils.Functions():
        func_name = idc.GetFunctionName(ea)
        if func_name.startswith(prefix):
            new_func_name = func_name.replace(prefix, new_prefix)
            print("%s, %s -> %s" %(hex(ea), func_name, new_func_name))
            idaapi.set_name(ea, new_func_name, idaapi.SN_CHECK)

class IdaJmc(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = "IdaJmc Lib"

    help = ""
    wanted_name = "IdaJmc"
    wanted_hotkey=""

    def init(self):
        return idaapi.PLUGIN_SKIP


    def run(self, arg):
        return

    def term(self):
        return

# noinspection PyPep8Naming
def PLUGIN_ENTRY():
    return IdaJmc()
