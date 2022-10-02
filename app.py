#! /usr/bin/env python3

import sys, os, socket, tqdm
from apps.custom_modules.PatternConstants import (
    is_a_number as ian,
    is_a_number_or_float as ianof,
    has_ext as he,
    valid_ipv4 as is_ipv4,
    valid_mac as is_mac,
)
from apps.custom_modules.ArgumentManager import (
    filtered as args,
    filtered_count as argsc,
)
from apps.custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from apps.custom_modules.PlatformConstants import (
    SEP as sep,
    CUR_DIR as cdir,
    PATH_SEP as psep,
)
from apps.custom_modules.FileOperator import (
    write_list_to_file as wltf,
    append_list_to_file as altf,
)

cus = cms["custom"]
file_path = "{}{}test-file.txt".format(cdir, sep)
seps = print("Path Sep: {}\nSep: {}\nCur dir: {}".format(psep, sep, cdir))

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # send 4096 bytes each time step


def start():
    print("\n")


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
