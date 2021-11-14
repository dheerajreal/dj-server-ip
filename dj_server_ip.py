import json
import socket
import subprocess
from urllib.request import urlopen


def get_public_ip():
    data = urlopen('http://httpbin.org/ip').read()
    data = json.loads(data)
    return data.get('origin')

def get_socket_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def get_host_ip():
    ip_list = subprocess.getoutput('hostname -i')
    return ip_list.split(" ")
