#! /usr/bin/python3

from custom_modules.FileOperator import append_file as af
from custom_modules.ArgumentManager import filtered as args, filtered_count as argsc
from custom_modules.PlatformConstants import (
    CUR_DIR as cdir,
    SEP as sep,
    USER_DIR as udir,
)

n_list = []

for i in range(33):
    n_list.append(str(i))

file_path = "{}{}fileoperatortest.txt".format(cdir, sep)

res = af(file_path, n_list)

# print(n_list)

file_path = "{}{}Documents{}prog-data{}arp-who-has-results.txt".format(
    udir, sep, sep, sep
)

print(file_path)
