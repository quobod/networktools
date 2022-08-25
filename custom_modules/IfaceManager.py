from distutils.sysconfig import customize_compiler
from scapy.all import sniff
import os
import sys
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms

global cus

cus = cms["custom"]


def mon_mode(iface=None):
    msg = "{} is in Monitor Mode".format(iface)
    s_msg = cus(190, 255, 190, msg)

    print(s_msg)
    sys.exit(0)


def man_mode(iface=None):
    msg = "{} is in Manage Mode".format(iface)
    s_msg = cus(190, 255, 190, msg)

    print(s_msg)
    sys.exit(0)


def pro_mode(iface=None):
    msg = "{} is in Promiscuous Mode".format(iface)
    s_msg = cus(190, 255, 190, msg)

    print(s_msg)
    sys.exit(0)


modes = {
    "mon": mon_mode,
    "man": man_mode,
    "pro": pro_mode,
    "monitor": mon_mode,
    "manage": man_mode,
    "promiscuous": pro_mode,
}


def set_mode(iface=None, mode=None):
    if not iface == None:
        try:
            if not mode == None:
                mode = mode.strip()
                _mode = modes[mode]
                _mode(iface)
            else:
                msg = cus(
                    255, 255, 255, "Expected mode name but received [{}]".format(mode)
                )
                e_msg_header = cus("Error:")
                e_msg = "{}\t{}".format(e_msg_header, msg)
                print("{}".format(e_msg))
        except KeyError as ie:
            msg = ""
            if len(mode) == 0:
                msg = cus(255, 255, 255, "Expected mode name but received nothing")
            else:
                msg = cus(255, 255, 255, "[{}] mode is not available".format(mode))
            e_msg_header = cus(255, 100, 100, "Error:")
            e_msg = "{}\t{}".format(e_msg_header, msg)
            print("{}".format(e_msg))
        except Exception as ex:
            msg = cus(255, 255, 255, ex)
            e_msg_header = cus(255, 190, 190, "Error:")
            e_msg = "{}\t{}".format(e_msg_header, msg)
            print("{}".format(e_msg))
    else:
        msg = cus(
            255,
            255,
            255,
            "Expected network interface name but received [{}]".format(iface),
        )
        e_msg_header = cus("Error:")
        e_msg = "{}\t{}".format(e_msg_header, msg)
        print("{}".format(e_msg))
    sys.exit(0)
