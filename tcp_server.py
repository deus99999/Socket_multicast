import socket


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.10', 5000))                    # сокет привязывается к локальному адресу 127.0.0.1 и порту 2000
    server.listen(5)                                    # сервер может принимать до 5 ожидающих подключений в очереди

    while True:
        print("Working...")
        client, address = server.accept()               # сервер ждет подключение клиента
        print(f"Connection from {address} has been established.")

        client.send(bytes("TCP server is ready to listen client .", encoding='utf-8'))
        data = client.recv(1024)
       # data = data.decode('utf-8')
        # print(f"data: {data.decode()}")

        print(data)


start_server()