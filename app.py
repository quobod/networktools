#! /usr/bin/python3

import sys
from custom_modules.ArgumentManager import filtered as args, filtered_count as argsc
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.IfaceManager import (
    bring_down_if as bd,
    bring_up_if as bu,
    set_mode as sm,
)

cus = cms["custom"]


def test_mode_change():
    if argsc == 2:
        iface = args[0]
        mode = args[1]
        sm(iface, mode)


def test_up_down():
    if argsc == 2:
        iface = args[0]
        state = args[1]

        if state.strip().lower() == "up":
            bu(iface)
        elif state.strip().lower() == "down":
            bd(iface)


test_up_down()
