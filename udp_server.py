import socket
import struct
import sys

message = 'Multicast server is working!'
multicast_group = ('224.3.29.71', 10000)

# create datagram socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set a timeout to avoid block indefinitely when trying to receive data
socket.settimeout(0.2)

# time to live controls how many networks will receive the packet
ttl = struct.pack('b', 1) # pack value 1 to byte

# set options: IP protocol level / set multicats ttl
socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    print("Sending..")
    sent = socket.sendto(message, multicast_group)

    # look for responses from all recepients
    while True:
        print("Waiting for receive")
        try:
            data, server = socket.recvfrom(16)
        except socket.timeout:
            print("Timeout, no more responses")
            break
        else:
            print(f"Received from {server}: {data}")
finally:
    print("Closing socket")
    socket.close()


