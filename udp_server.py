import socket
import struct
import time

message = b'Server UDP: This message was received from UDP server.'
multicast_group = ('224.3.29.71', 10000)

# create datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set a timeout to avoid block indefinitely when trying to receive data
sock.settimeout(10)

# time to live controls how many networks will receive the packet
ttl = struct.pack('b', 1) # pack value 1 to byte

# set options: IP protocol level / set multicast ttl
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

print("Sending..")
while True:
    time.sleep(1)
    sent = sock.sendto(message, multicast_group)


# print("Closing socket")
# sock.sendto(b"Closing socket", multicast_group)
#
# sock.close()


