#! /usr/bin/python3


from scapy.all import sr1, IP, ICMP
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms


def ping(host_address):
    cus = cms["custom"]
    try:
        p = sr1(IP(dst=host_address) / ICMP())
        if p:
            p.show()
    except SystemExit as se:
        p = None
        cus = None
        msg = "{}".format(se)
        cmsg = cus(255, 255, 255, msg)
        print("\t{}\n".format(cmsg))
    except KeyboardInterrupt as ki:
        p = None
        cus = None
        msg = "{}".format(ki)
        cmsg = cus(255, 255, 255, msg)
        print("\t{}\n".format(cmsg))
