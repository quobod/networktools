#! /usr/bin/python3

import unittest, sys
from os.path import exists, isfile, isdir
from os import unlink
from custom_modules.FileOperator import (
    append_to_file as atf,
    write_list_to_file as wltf,
    append_list_to_file as altf,
    write_to_file as wtf,
    delete_file as df,
    save_new_file as snf,
)
from custom_modules.PlatformConstants import (
    CUR_DIR as cdir,
    SEP as sep,
    USER_DIR as udir,
)
from custom_modules.PatternConstants import has_ext as he
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms

cus = cms["custom"]
write_list = "write-list-to-file-test"
append_list = "append-list-to-file-test"
default_test_file = "{}{}test-file.txt".format(cdir, sep)


def end():
    if exists("{}.txt".format(write_list)):
        unlink("{}.txt".format(write_list))

    if exists("{}.txt".format(append_list)):
        unlink("{}.txt".format(append_list))

    if exists(default_test_file):
        unlink(default_test_file)


def make_file_path(name=None):
    if name:
        if "." in name:
            name = name.split(".")[0]
        return "{}{}{}.txt".format(cdir, sep, name)
    else:
        return default_test_file


def dump(file_path=None):
    if file_path:
        _list = []

        if exists(file_path):
            with open(file_path, "r") as f:
                for line in f.readlines():
                    _list.append(int(line.strip()))
            return _list
    return False


def test_write_list_to_file():
    file_path = make_file_path(write_list)
    nums = [x for x in range(1, 13)]
    return wltf(file_path, nums), file_path


def test_append_list_to_file():
    file_path = make_file_path(append_list)
    nums = [x for x in range(13, 26)]
    return altf(file_path, nums), file_path


class Tests(unittest.TestCase):
    @classmethod
    def tearDownClass(self):
        end()

    def test_write_list_to_file(self):
        results, file_path = test_write_list_to_file()
        nums = dump(file_path)
        self.assertTrue(results)
        self.assertTrue(exists(file_path))
        self.assertTrue(isfile(file_path))
        self.assertEqual(int(sum(nums)), 78)

    def test_append_list_to_file(self):
        results, file_path = test_append_list_to_file()
        nums = dump(file_path)
        self.assertTrue(results)
        self.assertTrue(exists(file_path))
        self.assertTrue(isfile(file_path))
        self.assertEqual(int(sum(nums)), 247)


if __name__ == "__main__":
    unittest.main()
