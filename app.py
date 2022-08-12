#! /usr/bin/python3

from custom_modules.ArgumentManager import filtered, filtered_count
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.MacGenerator import (
    random_mac as make_mac,
    mac_pretty_print as pretty,
)
from custom_modules.IPSpoofer import spoof_conn as spoof

mac = make_mac()
p_mac = pretty(mac)

if filtered_count == 5:
    src = filtered[0]
    tgt = filtered[1]
    seq = int(filtered[2])
    sport = int(filtered[3])
    dport = int(filtered[4])
    try:
        spoof(src, tgt, seq, sport, dport)
    except Exception as ve:
        print(ve)
