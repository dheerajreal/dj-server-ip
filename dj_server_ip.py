import json
import socket
import subprocess
from urllib.request import urlopen


def get_public_ip():
    with urlopen('http://httpbin.org/ip') as response:
        data = json.loads(response.read())
        return data.get('origin')


def get_socket_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
        connection.connect(("1.1.1.1", 80))
        ip = connection.getsockname()[0]
        return ip


def get_local_ip():
    return ['127.0.0.1', '0.0.0.0']


def get_host_ip():
    ip_list = subprocess.getoutput('hostname -I')
    ip_list = [ip for ip in ip_list.split(" ") if ip]
    return ip_list


def server_ip():
    public_ip = [get_public_ip()]
    socket_ip = [get_socket_ip()]
    local_ip = get_local_ip()
    host_ip = get_host_ip()

    ips = public_ip + socket_ip + local_ip + host_ip
    return list(set(ips))
