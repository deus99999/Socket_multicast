import socket


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.10', 5000))                    # сокет привязывается к локальному адресу 127.0.0.1 и порту 2000
    server.listen(5)                                    # сервер может принимать до 5 ожидающих подключений в очереди

    while True:
        print("Server TCP: Working...")
        client, address = server.accept()               # сервер ждет подключение клиента
        print(f"Server TCP: Connection from {address} has been established.")

        client.send(bytearray(b"\nServer TCP: This message was received from TCP server."))

        # data = client.recv(1024)


start_server()