import json
from urllib.request import urlopen


def get_public_ip():
    data = urlopen('http://httpbin.org/ip').read()
    data = json.loads(data)
    return data.get('origin')
