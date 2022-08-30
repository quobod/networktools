#! /usr/bin/python3

import argparse
import os
import sys
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.NmapPortcannerHelpers import (
    handle_results as handler,
    print_nmap_report as pnr,
    print_report as pr,
)
from custom_modules.PlatformConstants import LINE_SEP as lsep
from custom_modules.PortScannerUtils import (
    test_network_address as tna,
    test_port_arg as tpa,
    test_host_address as tha,
    test_ipv4 as ti4,
    exit_prog as exp,
    is_host_address as iha,
    is_network_address as ina,
    is_not_port_range as inpr,
    is_port_range as ipr,
    is_valid_timeout as ivt,
    make_range as mr,
)
from custom_modules.PortScannerHelpers import scan_port_range, scan_port
from custom_modules.PortScanner import is_port_open_thread as ipot
from custom_modules.NmapPortScanner import (
    is_port_open_thread as nmap,
    scan_network_thread as nscan,
    stealth_scan_network_thread as snscan,
)
from custom_modules.ArpCommander import get_routing_table as return_route

cus = cms["custom"]
route_data = return_route()
netface_name = route_data["interface"]
local_ipv4_addr = route_data["address"]
gateway = route_data["gateway"]


desc = "This program scans the given port(s) of the given host"
epil = "Scan a port or range of ports. E.g. portscanner --scan <address> --timeout <seconds> --report --ports <n|n-n>."
vers = "%prog 0.1"


def error_handler(*args):
    cus = cms["custom"]
    arg = args[0]
    cargs = cus(254, 64, 4, arg)
    print("{}".format(cargs))
    os.system("exit")


parser = argparse.ArgumentParser(description=desc, epilog=epil)

parser.error = error_handler

parser.version = vers

group = parser.add_mutually_exclusive_group()

""" group arguments """

# verbosity level
group.add_argument(
    "-v",
    "--verbose",
    help="Increase output verbosity. Does not work with the -n option.",
    action="store_true",
)

""" positional arguments """

# start program
parser.add_argument(
    "-s",
    "--scan",
    nargs=1,
    help="Scan host/network. Expects a host address but can accept an address range with -n option. E.g. 10.1.10.1 or 10.1.10.1/8.",
)

# connection timeout
parser.add_argument(
    "-t",
    "--timeout",
    nargs=1,
    help="Set connection time out in seconds, defaults to 10. E.g. -t 0.2 or -t 10.",
)

# print results to file
parser.add_argument(
    "-r", "--report", help="Prints scan results to file", action="store_true"
)

# port or port range
parser.add_argument(
    "-p",
    "--ports",
    nargs=1,
    help="Set port or range of ports to scan; e.g. -p 22 or -p 1-1024.",
)

# use nmap port scanning
parser.add_argument(
    "-n",
    "--nmap",
    action="store_true",
    help="Use Nmap port scanning. Accepts a single address or a range of addresses: e.g. 192.168.1.21, 10.1.10.1/8 or 192.168.1.0/24",
)

parser.add_argument(
    "--stealth",
    help="Use Nmap stealth scanning. Expects network address and port(s)",
    nargs=2,
)

# parse arguments
args = parser.parse_args()


def run_port_scan_verbose_mode():
    address = None
    timeout = 10
    ports = None
    port_range = False
    report = False
    verbose = False

    if args.scan[0]:
        address = args.scan[0]
        valid_address = ti4(address)

        if args.timeout:
            valid_timeout = ivt(args.timeout[0])

            if valid_timeout:
                timeout = args.timeout[0]

        if args.report:
            report = True

        if args.verbose:
            verbose = True

        if valid_address:

            if args.ports:
                ports = args.ports[0]
                tpa(ports)

                port_range = ipr(ports)

                print("Verbose mode turned on\n")
                print(
                    "Host: {} port(s): {} timeout: {} report: {} verbose: {}\n".format(
                        address, ports, timeout, report, verbose
                    )
                )

                if port_range:
                    ports = mr(ports)
                    scan_port_range(address, ports, timeout, report, verbose)
                elif inpr(ports):
                    ports = int(ports)
                    scan_port(address, ports, timeout, report, verbose)


def run_port_scan_default_mode():
    address = None
    timeout = 10
    ports = None
    port_range = False
    report = False
    verbose = False

    if args.scan:
        address = args.scan[0]
        valid_address = ti4(address)

        if args.timeout:
            valid_timeout = ivt(args.timeout[0])

            if valid_timeout:
                timeout = args.timeout[0]

        if args.report:
            report = True

        if args.verbose:
            verbose = True

        if valid_address:

            if args.ports:
                ports = args.ports[0]
                tpa(ports)

                port_range = ipr(ports)

                if port_range:
                    ports = mr(ports)
                    scan_port_range(address, ports, timeout, report, verbose)
                elif inpr(ports):
                    ports = int(ports)
                    scan_port(address, ports, timeout, report, verbose)


def run_port_scan_nmap_mode():
    address, ports, results, report = None, None, None, False

    if args.scan:
        address = args.scan[0]
        valid_address = tna(address)

        if args.report:
            report = True

        if valid_address:
            print("Nmap mode\nScan {}".format(address))

            if args.timeout:
                valid_timeout = ivt(args.timeout[0])

                if valid_timeout:
                    timeout = args.timeout[0]
                    print("Timeout {}".format(timeout))

            if args.ports:
                ports = args.ports[0]
                tpa(ports)

                port_range = ipr(ports)

                if port_range:
                    print("Ports {}".format(ports))
                elif inpr(ports):
                    print("Port {}".format(ports))

                results = nmap(address, ports)
                handler(results)

                if report:
                    pnr(results)


def run_nmap_stealth_scan_mode():
    address, ports, results, port_range = None, None, None, False

    if args.stealth:
        address = args.stealth[0]
        ports = args.stealth[1]

        valid_address = tna(address)

        if valid_address:
            print("Nmap stealth scan mode{}".format(lsep))

            tpa(ports)

            port_range = ipr(ports)

            if port_range:
                print("Ports {}".format(ports))
            elif inpr(ports):
                print("Port {}".format(ports))

            results = snscan(address, ports)

            status = results["status"]

            if status:
                data = results["data"]
                print(*data, sep="{}".format(lsep))
            else:
                reason = results["reason"]
                print(reason)


if not args.nmap:
    if not args.verbose:
        run_port_scan_default_mode()
    else:
        run_port_scan_verbose_mode()
else:
    if args.stealth:
        run_nmap_stealth_scan_mode()
    else:
        run_port_scan_nmap_mode()
