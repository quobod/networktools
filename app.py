#! /usr/bin/env python3

import sys
from apps.custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from apps.custom_modules.PacketSender import stage_sender as spkt

cus = cms["custom"]


def exit_prog(exit_code=0):
    sys.exit(exit_code)


try:
    spkt({"host": "192.168.1.1", "port": "5447", "flag": "ack", "verbose": True})
except ValueError as ve:
    print(ve)
