import socket

def listener():
    host = "127.0.0.1"
    port = 4444

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"In ascolto su {host}:{port}...")
    client_socket, addr = server.accept()
    print(f"Connessione stabilita da {addr}")

    while True:
        command = input("Comando> ")
        if command.lower() == 'exit':
            client_socket.send(command.encode('utf-8'))
            break
        else:
            client_socket.send(command.encode('utf-8'))
            # Riceve l'output dal client
            output = client_socket.recv(4096).decode('utf-8')
            print(output)

    client_socket.close()
    server.close()

if __name__ == "__main__":
    listener()
