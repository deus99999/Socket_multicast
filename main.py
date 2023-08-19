import socket

group = "224.1.1.1"
port = 5004

# максимальное количество маршрутизаторов, через которое пакеты могут проходить
ttl = 2

# IPv4 / UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

client.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# sent smth datas
client.sendto(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n", (group, port))

#  ожидание ответа от сервера 
response = client.recv(4096)
print(response.decode())
client.close()
