#! /usr/bin/python3

import argparse
import os
import sys
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.PortScanner import is_port_open_thread as ipot
from custom_modules.NmapPortScanner import (
    is_port_open_thread as nmap,
    scan_network as nscanner,
)
from custom_modules.ArpCommander import get_routing_table as return_route
from custom_modules.PortScannerResultsHandler import (
    handle_results as handler,
    print_nmap_report as pnr,
    print_report as pr,
)
from custom_modules.PlatformConstants import LINE_SEP as lsep
from custom_modules.PatternConstants import (
    valid_ipv4 as vip4,
    valid_network_range as vnr,
)

cus = cms["custom"]
msg = None
timeout = None
verbose = None
report = None
port_range = False
sport = None
eport = None
route_data = return_route()
netface = route_data["interface"]
local_addr = route_data["address"]
host = route_data["gateway"]
scan_results = ""

desc = "This program scans the given port(s) of the given host"
epil = "Scan a port or range of ports of hosts on the network"
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

# run program silently
group.add_argument(
    "-q", "--quiet", help="Silently run the program", action="store_true"
)

""" positional arguments """

# host address
parser.add_argument(
    "-a",
    "--addr",
    help="The target host's IP address; e.g. -a 110.2.77.83. Defaults to 192.168.1.1",
    default=host,
)

# connection timeout
parser.add_argument(
    "-t",
    "--timeout",
    type=float,
    help="Set connection time out in seconds; e.g. -t 0.2 or -t 10.",
)

# port or port range
parser.add_argument(
    "-p",
    "--ports",
    help="Select which port or range of ports to scan; e.g. -p 22 or -p 1-1024.",
)

# use nmap port scanning
parser.add_argument(
    "-n",
    "--nmap",
    action="store_true",
    help="Use Nmap port scanning. Can take a single address or a range of addresses: e.g. 192.168.1.21, 10.1.10.1/8 or 192.168.1.0/24",
)

# print results to file
parser.add_argument(
    "-r", "--report", help="Prints scan results to file", action="store_true"
)

# scan the host or network using nmap scanner
parser.add_argument(
    "-s",
    "--scan",
    help="Scan the host/network returns list. Expects ipv4 or network range argument.",
    nargs=1,
    dest="scan",
)

# parse arguments
args = parser.parse_args()


def run_verbose_mode(cust, args):
    global timeout
    global sport, eport, ports
    global port_range
    report = False
    data = []

    if args.addr:
        host = args.addr

    if args.timeout:
        timeout = args.timeout

    if args.report:
        report = True

    if args.ports:
        if "-" in args.ports:
            ports_split = args.ports.split("-")
            sport = int(ports_split[0])
            eport = int(ports_split[1])

            if eport < sport:
                port_range = False
            else:
                ports = range(sport, eport)
                port_range = True
        else:
            sport = int(args.ports)

    msg = "Port Scanner"
    cmsg = cus(177, 200, 177, msg)
    print("\n\t\t\t\t{}\n".format(cmsg) + "-" * 75)
    data.append("{}\t\t\t\t{}{}".format(lsep, cmsg, lsep) + "-" * 75)

    if port_range:
        msg_host = "Scanning Host: {}".format(host)
        cus_msg_host = cus(170, 170, 255, msg_host)
        msg_ports = "Ports: {}-{}".format(sport, eport)
        cus_msg_ports = cus(200, 200, 245, msg_ports)
        print("{}{}{}".format(cus_msg_host, cus_msg_ports, lsep))
        data.append("{}{}{}".format(cus_msg_host, cus_msg_ports, lsep))

        for port in ports:
            port_open = ipot(host, port, verbose, timeout)
            if port_open:
                msg_port_open = "Port {} is open".format(port)
                cus_msg_port_open = cus(255, 255, 255, msg_port_open)
                print("{}".format(cus_msg_port_open))
                data.append("{}{}".format(cus_msg_port_open, lsep))

            else:
                msg_port_closed = "Port {} is closed".format(port)
                cus_msg_port_closed = cus(100, 100, 100, msg_port_closed)
                print("{}".format(cus_msg_port_closed))
                data.append("{}{}".format(cus_msg_port_closed, lsep))
    else:
        msg_host = "Scanning Host: {}".format(host)
        cus_msg_host = cus(170, 170, 255, msg_host)
        msg_port = "Port: {}".format(sport)
        cus_msg_port = cus(200, 200, 245, msg_port)
        print("{}{}{}".format(cus_msg_host, cus_msg_port, lsep))
        data.append("{}{}{}".format(cus_msg_host, cus_msg_port, lsep))

        port_open = ipot(host, sport, verbose, timeout)

        if port_open:
            msg_port_open = "Port {} is open".format(sport)
            cus_msg_port_open = cus(255, 255, 255, msg_port_open)
            print("{}".format(cus_msg_port_open))
            data.append("{}{}".format(cus_msg_port_open, lsep))
        else:
            msg_port_closed = "Port {} is closed".format(sport)
            cus_msg_port_closed = cus(100, 100, 100, msg_port_closed)
            print("{}".format(cus_msg_port_closed))
            data.append("{}{}".format(cus_msg_port_closed, lsep))

    if report:
        pr(data)


def run_default_mode(cus, args):
    global timeout
    global sport, eport, ports
    global port_range
    report = False
    data = []

    if args.addr:
        host = args.addr

    if args.timeout:
        timeout = args.timeout

    if args.report:
        report = True

    if args.ports:
        if "-" in args.ports:
            ports_split = args.ports.split("-")
            sport = int(ports_split[0])
            eport = int(ports_split[1])

            if eport < sport:
                port_range = False
            else:
                ports = range(sport, eport)
                port_range = True
        else:
            sport = int(args.ports)

    msg = "Port Scanner"
    cmsg = cus(177, 200, 177, msg)
    data.append("{}\t\t\t\t{}{}".format(lsep, cmsg, lsep) + "-" * 75)

    msg_host = "Scanning Host: {}".format(host)
    cus_msg_host = cus(170, 170, 255, msg_host)
    msg_ports = "Ports: {}-{}".format(sport, eport)
    cus_msg_ports = cus(200, 200, 245, msg_ports)
    data.append("{}{}{}".format(cus_msg_host, cus_msg_ports, lsep))

    if port_range:

        for port in ports:
            port_open = ipot(host, port, verbose, timeout)
            if port_open:
                msg_port_open = "Port {} is open".format(port)
                cus_msg_port_open = cus(255, 255, 255, msg_port_open)
                print("{}".format(cus_msg_port_open))
                data.append("{}{}".format(cus_msg_port_open, lsep))
    else:
        port_open = ipot(host, sport, verbose, timeout)

        if port_open:
            msg_port_open = "Port {} is open".format(sport)
            cus_msg_port_open = cus(255, 255, 255, msg_port_open)
            print("{}".format(cus_msg_port_open))
            data.append("{}{}".format(cus_msg_port_open, lsep))

    if report:
        pr(data)


def print_nscanner_results(results):
    if not results == None:
        status = results["status"]

        if status:
            _data = results["data"]
            s_msg_header = cus(90, 255, 90, "Success:")
            s_msg_body = cus(255, 255, 255, "... printing results")
            s_msg = "{}\t{}".format(s_msg_header, s_msg_body)
            print("{}".format(s_msg))
            print(*_data, sep="\n")
        else:
            f_msg_header = cus(255, 90, 90, "Failure:")
            f_msg_body = cus(255, 255, 255, results["reason"])
            f_msg = "{}\t{}".format(f_msg_header, f_msg_body)
            print("{}".format(f_msg))


# Use Nmap
if args.nmap:
    if args.addr:
        host = args.addr

    if args.timeout:
        timeout = args.timeout

    if args.report:
        report = True

    if args.ports:
        ports = args.ports

    scan_results = nmap(host, ports)

    handler(scan_results)

    if report:
        report = pnr(scan_results)

        if report:
            print("Report Printed")
        else:
            print("Report Error")

# Nmap network scanner
elif args.scan:
    network = args.scan[0]
    network = str(network).strip()

    if vnr(network):
        print("Scanning network: {}".format(network))
        results = nscanner(network)
        sys.exit(0)
    else:
        a_msg_header = cus(255, 90, 90, "Error:")
        a_msg_body = cus(
            255,
            255,
            255,
            "{} is not a valid network range. Expecting xxx.xxx.xxx.xxx/xx.".format(
                network
            ),
        )
        a_msg = "{}\t{}".format(a_msg_header, a_msg_body)
        print("{}".format(a_msg))

# Quiet mode
elif args.quiet:
    run_default_mode(cus, args)

# Verbose mode
elif args.verbose:
    run_verbose_mode(cus, args)

# Default mode run silently
else:
    run_default_mode(cus, args)
