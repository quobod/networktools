#! /usr/bin/python3

from custom_modules.ArgumentManager import filtered, filtered_count
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.SocketSniffer import sniff


if filtered_count == 1:
    tgt = filtered[0]
    sniff(tgt)
