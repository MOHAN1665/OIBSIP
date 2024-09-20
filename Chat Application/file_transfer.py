import socket
import os

def send_file(filename, client_socket):
    filesize = os.path.getsize(filename)
    client_socket.send(f"{filename}{SEPARATOR}{filesize}".encode())

    with open(filename, "rb") as file:
        bytes_read = file.read(1024)
        while bytes_read:
            client_socket.send(bytes_read)
            bytes_read = file.read(1024)

def receive_file(server_socket):
    received = server_socket.recv(1024).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    with open(filename, "wb") as file:
        bytes_read = server_socket.recv(1024)
        while bytes_read:
            file.write(bytes_read)
            bytes_read = server_socket.recv(1024)
