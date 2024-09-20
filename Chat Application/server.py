import socket
import threading
import sqlite3
from cryptography.fernet import Fernet

# Load encryption key
def load_key():
    return open("secret.key", "rb").read()

key = load_key()
cipher = Fernet(key)

def encrypt_message(message):
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message).decode()

def save_message_to_db(sender, receiver, message):
    print(f"Saving message from {sender} to {receiver}...")
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)", (sender, receiver, message))
    conn.commit()
    conn.close()
    print("Message saved successfully!")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            decrypted_message = decrypt_message(message)
            # Assuming you have a way to determine the sender and receiver
            # You might need to adjust this part depending on your implementation
            sender = 'some_sender'  # replace with actual sender
            receiver = 'some_receiver'  # replace with actual receiver
            save_message_to_db(sender, receiver, decrypted_message)
            broadcast(encrypt_message(decrypted_message), client_socket)
        except Exception as e:
            print(f"Error: {e}")
            break
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def start_server():
    print("Server started...")
    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

start_server()
