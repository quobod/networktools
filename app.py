#! /usr/bin/python3

import sys
from custom_modules.PatternConstants import is_a_number as ian, is_port_range as ipr
from custom_modules.ArgumentManager import filtered as args, filtered_count as argsc
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.PlatformConstants import SEP as sep, CUR_DIR as cdir
from custom_modules.IfaceManager import (
    bring_down_if as bd,
    bring_up_if as bu,
    set_mode as sm,
    check_iface_exist as cie,
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
    elif argsc == 1:
        arg = args[0]
        i = cie(arg)

        if i:
            print("{} is valid".format(arg))
        else:
            print("network interface named [{}] does not exist".format(arg))


def test_is_a_number():
    if argsc > 0:
        for a in args:
            print("{} is a number? {}".format(a, ian(a)))


def test_is_port_range():
    if argsc > 0:
        for a in args:
            print("{} is a number range? {}".format(a, ipr(a)))


# print("{}\n{}".format(sep, cdir))

test_is_port_range()
