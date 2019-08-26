# Import requests and regex library
import requests
import re
import socket
import ipaddress


# def get_external_ip():
#     # Make a request to checkip.dyndns.org as proposed
#     # in https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery#DNS_Addresses
#     response = requests.get('http://checkip.dyndns.org').text
#     # Filter the response with a regex for an IPv4 address
#     ip = re.search("(?:[0-9]{1,3}\.){3}[0-9]{1,3}", response).group()
#     return ip
#
#
# external_ip = get_external_ip()
# print("network ip address", external_ip)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(IPAddr)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

ip = ipaddress.ip_address('192.0.2.1')
ip1 = ipaddress.ip_network('192.0.2.1', strict=True)
ip2 = ipaddress.ip_interface('192.0.2.1')
# ip1 = ipaddress.ip_address('2001:DB8::1')
# ip2 = ipaddress.ip_address(3221286)
# print(ip2)
print("ip address:", ip)
print('ip network:', ip1)
print('ip interface:', ip2)
# print(ip1)
print(type(ip))

# print(type(ip2))
# print(type(ip1))
print(ipaddress.ip_address(u'192.168.0.250'))
print(type(ipaddress.ip_address(u'192.168.0.250')))
