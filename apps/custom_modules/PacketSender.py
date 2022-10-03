#! /usr/bin/python

import logging
from scapy.all import *
from .ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from .Flags import FLAGS as flags
from .PatternConstants import (
    valid_ipv4 as vip4,
    is_a_number as isnum,
    is_port_range as isportrange,
    is_a_number_or_float as isnumorfloat,
)
from .TypeTester import (
    arg_is_an_int as aiai,
    arg_is_none as ain,
    arg_is_a_dict as aiad,
    arg_is_a_tuple as aiat,
    arg_is_a_list as aial,
)


logging.basicConfig(filemode="scapy-info-log", level=logging.INFO)
logging.basicConfig(filemode="scapy-warning-log", level=logging.WARNING)
logging.basicConfig(filemode="scapy-error-log", level=logging.ERROR)
logging.basicConfig(filemode="scapy-critical-log", level=logging.CRITICAL)

cus = cms["custom"]

""" Send packet to target 
    @param host: The target host
    @param port: The target's port
    @param flag: The packet flag
    @param timeout: The number of seconds before giving up
"""


def stage_sender(objData=None):
    logging.info("Method stage_send invoked\n")
    _host = None
    _port = None
    _flag = None
    _timeout = None
    _src_port = RandShort()

    """ Validate parameters """

    validate_mandatory_parameters(objData)

    _timeout = validate_optional_parameters(objData) or 10
    _host = objData["host"]
    _port = objData["port"]
    _flag = objData["flag"]

    print(
        "Packet parameters:\n\tHost: {}\n\tPort: {}\n\tFlag: {}\n\tTimeout: {}\n".format(
            _host, _port, _flag, _timeout
        )
    )


def validate_optional_parameters(objData):
    if "timeout" in objData:
        timeout = objData["timeout"]
        if isnumorfloat(timeout):
            return timeout
    return None


def validate_mandatory_parameters(objData):
    if objData == None:
        e_msg_header = cus(255, 112, 112, "Error")
        e_msg_body = cus(255, 255, 255, "Expecting a dict but received nothing")
        e_msg = "{} {}".format(e_msg_header, e_msg_body)
        raise ValueError(e_msg)

    if "host" not in objData:
        e_msg_header = cus(255, 112, 112, "Error")
        e_msg_body = cus(
            255,
            255,
            255,
            "Expected a host key in the dict parameter but received nothing",
        )
        e_msg = "{} {}".format(e_msg_header, e_msg_body)
        raise ValueError(e_msg)

    host = objData["host"]

    if not vip4(host):
        e_msg_header = cus(255, 112, 112, "Error")
        e_msg_body = cus(
            255,
            255,
            255,
            "Expected a valid IPv4 host address but received [{}]".format(host),
        )
        e_msg = "{} {}".format(e_msg_header, e_msg_body)
        raise ValueError(e_msg)

    if "port" not in objData:
        e_msg_header = cus(255, 112, 112, "Error")
        e_msg_body = cus(
            255,
            255,
            255,
            "Expected a port key in the dict parameter but received nothing",
        )
        e_msg = "{} {}".format(e_msg_header, e_msg_body)
        raise ValueError(e_msg)

    port = objData["port"]

    if not isnum(port):
        e_msg_header = cus(255, 112, 112, "Error")
        e_msg_body = cus(
            255,
            255,
            255,
            "Expected a valid port number but received [{}]".format(port),
        )
        e_msg = "{} {}".format(e_msg_header, e_msg_body)
        raise ValueError(e_msg)

    if "flag" not in objData:
        e_msg_header = cus(255, 112, 112, "Error")
        e_msg_body = cus(
            255,
            255,
            255,
            "Expected a flag key in the dict parameter but received nothing",
        )
        e_msg = "{} {}".format(e_msg_header, e_msg_body)
        raise ValueError(e_msg)

    flag = objData["flag"]

    if flag not in flags:
        e_msg_header = cus(255, 112, 112, "Error")
        e_msg_body = cus(
            255,
            255,
            255,
            "Expected a valid flag but [{}] is not available".format(flag),
        )
        e_msg = "{} {}".format(e_msg_header, e_msg_body)
        raise ValueError(e_msg)
