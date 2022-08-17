#! /usr/bin/python3

from scapy.all import *
from custom_modules.PlatformConstants import LINE_SEP as lsep, SEP as sep
from custom_modules.TypeTester import (
    arg_is_a_dict as aiad,
    arg_is_a_list as aial,
    arg_is_a_tuple as aiat,
)
from custom_modules.Utils import print_dict_values as pdv


""" Gets the local network interface's route. 
    List: Network Interface Name, it's address and the gateway.
    Returns: DataFrame
"""


def get_routing_table():
    route_info = conf.route.route()
    interface = route_info[0]
    address = route_info[1]
    gateway = route_info[2]
    _index = [1, 2, 3]

    data = {"Interface": interface, "Address": address, "Gateway": gateway}

    return data


""" Prints the local network interface's route.
    Prints DataFrame
"""


def print_routing_table():
    route_info = conf.route.route()
    interface = route_info[0]
    address = route_info[1]
    gateway = route_info[2]
    _index = [1, 2, 3]

    data = {"Interface": interface, "Address": address, "Gateway": gateway}

    if aiad(data):
        pdv(data)


""" Returns the network interface's name
    Returns: string
"""


def get_network_interface_name():
    return conf.iface


""" Prints the network interface's name """


def print_network_interface_name():
    print("\n{}".format(conf.iface))


""" Prints the network interface's hardware address """


def get_network_interface_hardware_address():
    iface = get_network_interface_name
    return get_if_hwaddr(conf.iface)
