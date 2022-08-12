#! /usr/bin/python3

from custom_modules.ArgumentManager import filtered, filtered_count
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.MacGenerator import (
    random_mac as make_mac,
    mac_pretty_print as pretty,
)

mac = make_mac()
p_mac = pretty(mac)

print("MAC: \t\t{}\nPretty MAC:\t\t{}".format(mac, p_mac))
