import nmap
from multiprocessing.pool import ThreadPool
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.TypeTester import (
    arg_is_a_string,
)

custom = cms["custom"]

""" 
    Connects to given host at the given port to deteremine whether the host is up and state of the port.
    @Param host String: IP address or range 
    @Param port Striing: The connection port or port range
"""


def is_port_open(host, port):
    nm_scanner = nmap.PortScanner()
    nm_scanner.scan(str(host), str(port))
    return nm_scanner


def scan_network(network, port):
    return_list = []
    nm = nmap.PortScanner()
    a = nm.scan(hosts=network, ports=str(port), arguments="sn")

    for k, v in a["scan"].items():
        if str(v["status"]["state"]) == "up":
            try:
                return_list.append(
                    [str(v["addresses"]["ipv4"]), str(v["addresses"]["mac"])]
                )
            except:
                pass
    if len(return_list) > 0:
        return {"status": True, "data": return_list}
    else:
        return {"status": False, "reason": "Failed to detect any hosts"}


def stealth_scan_network(network, port):
    return_list = []
    nm = nmap.PortScanner()
    a = nm.scan(hosts=network, ports=str(port), arguments="ss")

    for k, v in a["scan"].items():
        if str(v["status"]["state"]) == "up":
            try:
                return_list.append(
                    [str(v["addresses"]["ipv4"]), str(v["addresses"]["mac"])]
                )
            except:
                pass
    if len(return_list) > 0:
        return {"status": True, "data": return_list}
    else:
        return {"status": False, "reason": "Failed to detect any hosts"}


def is_port_open_thread(host, port):
    pool = ThreadPool(processes=3)
    async_result = pool.apply_async(is_port_open, (host, port))
    return async_result.get()


def scan_network_thread(network, port):
    pool = ThreadPool(process=1)
    async_results = pool.apply_async(scan_network, (network, port))
    return async_results.get()


def stealth_scan_network_thread(network, port):
    pool = ThreadPool(process=1)
    async_results = pool.apply_async(stealth_scan_network, (network, port))
    return async_results.get()
