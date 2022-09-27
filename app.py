#! /usr/bin/env python3

import sys, os
from custom_modules.PatternConstants import is_a_number as ian, is_port_range as ipr
from custom_modules.ArgumentManager import filtered as args, filtered_count as argsc
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.PlatformConstants import SEP as sep, CUR_DIR as cdir

cus = cms["custom"]


def exit_prog(ec=0):
    sys.exit(ec)
