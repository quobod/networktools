#! /usr/bin/python3

from apps.custom_modules.FileOperator import (
    append_to_file as atf,
    write_list_to_file as wltf,
    append_list_to_file as altf,
    write_to_file as wtf,
    delete_file as df,
    save_new_file as snf,
)
from apps.custom_modules.ArgumentManager import (
    filtered as args,
    filtered_count as argsc,
)
from apps.custom_modules.PlatformConstants import (
    CUR_DIR as cdir,
    SEP as sep,
    USER_DIR as udir,
)
from apps.custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms

cus = cms["custom"]
file_path = "{}{}test-file.txt".format(cdir, sep)


def test_write_list_to_file():
    nums = [x for x in range(1, 13)]
    saved = wltf(file_path, nums)

    if saved:
        s_msg = cus(120, 255, 120, "Success")
        print("{}\n".format(s_msg))
    else:
        f_msg = cus(255, 120, 120, "Failed")
        print("{}\n".format(f_msg))


def test_append_list_to_file():
    nums = [x for x in range(13, 26)]
    saved = altf(file_path, nums)

    if saved:
        s_msg = cus(120, 255, 120, "Success")
        print("{}\n".format(s_msg))
    else:
        f_msg = cus(255, 120, 120, "Failed")
        print("{}\n".format(f_msg))
