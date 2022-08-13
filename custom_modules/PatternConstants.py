import re


""" IPv4 address """


def valid_ipv4(address=None):
    if not address == None:
        IPv4 = re.compile(r"([0-9]{1,3}\.){3}([0-9]{1,3})$")
        matched = re.search(IPv4, address)
        return not matched == None


""" Network range  """


def valid_network_range(address=None):
    if not address == None:
        IPv4_network = re.compile(r"([0-9]{1,3}\.){3}([0-9]{1,3})/[1-9]{1,3}$")
        matched = re.search(IPv4_network, address)
        return not matched == None


""" File extensions """


def has_ext(string=None):
    if not string == None:
        FILE_EXTENSION = re.compile(r"(.)+(\.[a-z]{2,3})$")
        matched = re.search(FILE_EXTENSION, string)
        return not matched == None
