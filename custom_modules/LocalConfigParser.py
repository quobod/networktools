#! /usr/bin/python3

from scapy.all import *
from pandas import DataFrame as df, Series as sd
from custom_modules.PlatformConstants import LINE_SEP as lsep, SEP as sep


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

    data = {"Interface": [interface], "Address": [address], "Gateway": [gateway]}

    data_frame = df(data, index=["1."])
    return data_frame


""" Prints the local network interface's route.
    Prints DataFrame
"""


def print_routing_table():
    route_info = conf.route.route()
    interface = route_info[0]
    address = route_info[1]
    gateway = route_info[2]
    _index = [1, 2, 3]

    data = {"Interface": [interface], "Address": [address], "Gateway": [gateway]}

    data_frame = df(data, index=["1."])

    print("{}".format(data_frame))


""" Returns the network interface's name
    Returns: string
"""


def get_network_interface_name():
    return conf.iface


""" Prints the network interface's name """


def print_network_interface_name():
    print("\n{}".format(conf.iface))
