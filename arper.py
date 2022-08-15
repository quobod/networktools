#! /usr/bin/python3

import argparse
from ast import arguments
import re
import os
import sys
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.PatternConstants import valid_ipv4, valid_network_range, has_ext
from custom_modules.PlatformConstants import SEP as psep, USER_DIR as udir
from custom_modules.FileOperator import write_dataframe_to_file, write_to_file as wtf
from custom_modules.LocalConfigParser import (
    print_routing_table as prt,
    get_routing_table as grt,
    print_network_interface_name as pnin,
    get_network_interface_name as gnin,
)

_verbose = False
_save = False
cus = cms["custom"]


def error_handler(*args):
    cus = cms["custom"]

    for a in args:
        cargs = cus(254, 64, 74, a)
        print("{}\n".format(cargs))

    sys.exit(os.EX_USAGE)


def warning_handler(*args):
    cus = cms["custom"]
    arg = args[0]
    cargs = cus(254, 224, 224, arg)
    print("{}".format(cargs))
    sys.exit(os.EX_USAGE)


desc = "A tool that displays and can print reports about the hosts connected to the network."
epil = "This program needs adminstrative access to perform many, if not, all of it's tasks."


parser = argparse.ArgumentParser(description=desc, epilog=epil)

parser.error = error_handler

""" group optional arguments """

group = parser.add_mutually_exclusive_group()

# Increase verbosity
group.add_argument(
    "-v",
    "--verbose",
    dest="verbose",
    action="store_true",
    help="Increase output verbosity",
)


""" positional arguments """

# Saves output to file in the user's home dir
parser.add_argument("-s", "--save", help="Save output to file", action="store_true")

# Print info to the console
parser.add_argument("-r", "--route", help="Print routing info", action="store_true")

# Prints the local network interfae name
parser.add_argument(
    "-n",
    "--name",
    help="Prints the name of local network interface",
    action="store_true",
)

args = parser.parse_args()

if args.verbose:
    _verbose = True

if args.save:
    _save = True

if args.route:
    data = grt()
    file_path = "{}{}Documents{}prog-data{}routing_table.txt".format(
        udir, psep, psep, psep
    )

    if _verbose:
        if _save:
            _title = "Routing info"
            c_title = cus(255, 255, 255, _title)
            print("\t\t{}\n".format(c_title))
            print("{}\n".format(data))

            _action = "... Saving to file"
            c_action = cus(255, 255, 255, _action)
            print("\t\t{}\n".format(c_action))
            success = write_dataframe_to_file(file_path, data)

            if success:
                _action_success = "Info saved to file"
                c_action_success = cus(90, 255, 90, _action_success)
                print("\t\t{}\n".format(c_action_success))
            else:
                _action_failure = "Error saving to file"
                c_action_failure = cus(255, 90, 90, _action_failure)
                print("\t\t{}\n".format(c_action_failure))
        else:
            _title = "Routing info"
            c_title = cus(255, 255, 255, _title)

            print("\t\t{}\n".format(c_title))
            print("{}\n".format(data))
    else:
        if _save:
            # Save output to file
            success = write_dataframe_to_file(file_path, data)

            _title = "Routing info"
            c_title = cus(255, 255, 255, _title)

            print("\t\t{}\n".format(c_title))
            print("{}\n".format(data))

            if not success:
                _action_failure = "Error saving to file"
                c_action_failure = cus(255, 90, 90, _action_failure)
                print("\n\t\t{}\n".format(c_action_failure))
        else:
            _title = "Routing info"
            c_title = cus(255, 255, 255, _title)

            print("\t\t{}\n".format(c_title))
            print("{}\n".format(data))

if args.name:
    data = gnin()

    if _verbose:
        _title = "Network Interface Name"
        c_title = cus(255, 255, 255, _title)

        print("\t\t{}\n".format(c_title))
        print("{}\n".format(data))

        if args.save:
            print("... Saving info to file\n")

            file_path = "{}{}Documents{}prog-data{}local-netface-name.txt".format(
                udir, psep, psep, psep
            )

            success = wtf(file_path, data)

        if success:
            _action_success = "Successfully saved info the file"
            c_action_success = cus(88, 255, 88, _action_success)
            print("{}\n".format(c_action_success))
        else:
            _action_failure = "Error saving to file"
            c_action_failure = cus(255, 90, 90, _action_failure)
            print("\n\t\t{}\n".format(c_action_failure))
    else:
        c_data = cus(255, 255, 255, data)
        print("{}\n".format(c_data))

        if args.save:
            file_path = "{}{}Documents{}prog-data{}local-netface-name.txt".format(
                udir, psep, psep, psep
            )

            success = wtf(file_path, data)

            if not success:
                _action_failure = "Error saving to file"
                c_action_failure = cus(255, 90, 90, _action_failure)
                print("\n\t\t{}\n".format(c_action_failure))
