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
from apps.custom_modules.PlatformConstants import (
    SEP as sep,
    CUR_DIR as cdir,
    PATH_SEP as psep,
)
from apps.custom_modules.FileDialog import open_file as of
from apps.custom_modules.FileOperator import write_list_to_file as wltf

cus = cms["custom"]
file_path = "{}{}test-file.txt".format(cdir, sep)

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # send 4096 bytes each time step


def start():
    # print("Path Sep: {}\nSep: {}\nCur dir: {}".format(psep, sep, cdir))
    test_f()


def test_f():
    nums = [x for x in range(1, 13)]
    saved = wltf(file_path, nums)

    if saved:
        s_msg = cus(120, 255, 120, "Success")
        print("{}\n".format(s_msg))
    else:
        f_msg = cus(255, 120, 120, "Failed")
        print("{}\n".format(f_msg))


def read_file():
    file = of()

    if file:
        with open(file, "r") as f:
            for line in f.readlines():
                line_split = line.split(",")
                ip = line_split[0].strip()
                mac = line_split[1].strip()
                print("IP    {}\t\t\tMAC {}".format(ip, mac))


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
