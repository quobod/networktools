#! /usr/bin/python3

from custom_modules.ArgumentManager import filtered as args, filtered_count as argsc
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.HostListReader import run_nmap_vuln_scan as rnvc

cus = cms["custom"]


if argsc == 1:
    arg = args[0]
    try:
        rnvc(arg)
    except Exception as exc:
        print("{}".format(exc))
