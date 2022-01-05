import ipaddress

from dj_server_ip import (get_host_ip, get_local_ip, get_public_ip,
                          get_socket_ip, server_ip)


def test_public_ip():
    ip = get_public_ip()
    assert ip is not None
    ip = ipaddress.IPv4Address(ip)
    assert ip.is_private is False


def test_socket_ip():
    ip = get_socket_ip()
    assert ip is not None
    ip = ipaddress.IPv4Address(ip)
    assert ip.is_private is True


def test_local_ip():
    ips = get_local_ip()
    ips = [ipaddress.IPv4Address(item) for item in ips]
    assert all(ips) is True


def test_host_ip():
    ips = get_host_ip()
    ips = [ipaddress.IPv4Address(item) for item in ips]
    assert all(ips) is True


def test_server_ip():
    ips = server_ip()
    ips = [ipaddress.IPv4Address(item) for item in ips]
    assert all(ips) is True
    print(ips)
