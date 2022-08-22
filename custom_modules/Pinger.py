#! /usr/bin/python3


from scapy.all import sr1, IP, ICMP


def ping(host_address):
    try:
        p = sr1(IP(dst=host_address) / ICMP())
        if p:
            p.show()
    except SystemExit as se:
        print("{}\n".format(se))
        p = None
    except KeyboardInterrupt as ki:
        print("You killed the ping process")
        p = None
