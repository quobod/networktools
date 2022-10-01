#! /usr/bin/env python3

import sys, os, socket, tqdm
from apps.custom_modules.PatternConstants import (
    is_a_number as ian,
    is_port_range as ipr,
)
from apps.custom_modules.ArgumentManager import (
    filtered as args,
    filtered_count as argsc,
)
from apps.custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from apps.custom_modules.PlatformConstants import SEP as sep, CUR_DIR as cdir
from apps.custom_modules.FileDialog import open_file as of
from apps.custom_modules.Utils import (
    am_pm,
    time_zone,
    minute,
    time_stamp,
    date_stamp,
    numbered_date_time_stamp as dtstamp,
)

cus = cms["custom"]

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # send 4096 bytes each time step


def start():
    ap = am_pm()
    tz = time_zone()
    min = minute()
    print("{}\n".format(dtstamp()))


def exit_prog(ec=0):
    sys.exit(ec)


def init_prog():
    print(" " * 55 + "\n" + " " * 26 + "Program Started\n")
    start()


def end_prog():
    print(" " * 55 + "\n" + " " * 26 + " Program Ended\n")
    exit_prog()


init_prog()


end_prog()
