import socket
import struct
import sys


def connect_tcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.10', 5000))

    #  socket is going to attempt to receive data, in a buffer size of 1024 bytes at a time
    server_message = s.recv(1024)
   # print(type(server_message))
    server_message = bytearray(server_message)
    # print(server_message)
   # print(type(server_message))

    print("\n", server_message.decode("utf-8"))

    print("\nClient: Enter '3' to change server")
    while True:
        msg = input()
        # s.sendall(msg.encode())

        if msg == "3":
            print("Client: Connection was closed.")
            break

    choice_of_server()

    
def connect_udp():
    multicast_group = '224.3.29.71'

    # empty string means that server will listen all net interfaces
    server_address = ('', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)

    # add the socket to the multicast group on all interfaces

    # change IP of group to binary code
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    # print(mreq)

    # set options for work with multicast
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    try:
        while True:
            print("\nClient: Waiting for message..\n")
            data, address = sock.recvfrom(1024)

            byte_array_data = bytearray(data)
            print(byte_array_data)

            # sock.sendto(bytes("\nServer TCP: This message was received from TCP server.",
            #                   encoding='utf-8'), address)

            msg = input()
            if msg == "3":
                print("Client: Connection was closed.")
                break

    # except KeyboardInterrupt as ki:
    #     if ki:
    #         # Обработка прерывания (Ctrl+C)
    except:
        print("Disconnecting from multicast group...")
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)

        sock.close()
        choice_of_server()


def choice_of_server():
    print("\n1. TCP\n2. Multicast UDP\n")
    choose = input("Client: Choose 1 or 2 to connect: ")

    if choose.isdigit() and int(choose) in [1, 2]:
        if choose == "1":
            connect_tcp()
        if choose == "2":
            connect_udp()

    else:
        print("Client: Incorrect data. Try again.")
        choice_of_server()


choice_of_server()

