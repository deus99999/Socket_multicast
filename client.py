import socket


def connect_tcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.10', 5000))

    #  socket is going to attempt to receive data, in a buffer size of 1024 bytes at a time
    server_message = s.recv(1024)
   # print(type(server_message))
    server_message = bytearray(server_message)
    print(server_message)
   # print(type(server_message))

    print(server_message.decode("utf-8"))

    print("\nEnter 'exit' to stop sending messages\n ")
    while True:
        msg = input()
        s.sendall(msg.encode())

        if msg == "exit":
            print("Connection was closed.")
            break


def connect_udp():
    pass

def choice():
    print("\n1. TCP\n2. Multicast\n")
    choose = input("Choose number of connection: ")

    if choose.isdigit() and int(choose) in [1, 2]:
        if choose == "1":
            connect_tcp()

    else:
        print("Incorrect data. Try again.")
        choice()


choice()
