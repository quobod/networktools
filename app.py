#! /usr/bin/python3

from custom_modules.ArgumentManager import filtered as args, filtered_count as argsc
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.IfaceManager import set_mode

cus = cms["custom"]


if argsc == 2:
    iface = args[0]
    mode = args[1]
    set_mode(iface, mode)
