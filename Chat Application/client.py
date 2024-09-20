import socket
import threading
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import sqlite3
import emoji  # Import the emoji library

# Load encryption key
def load_key():
    return open("secret.key", "rb").read()

key = load_key()
cipher = Fernet(key)

def encrypt_message(message):
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message).decode()

def send_message():
    message = entry.get()
    if message:
        # Convert emojis in the message to their actual emoji characters
        message = emoji.emojize(message)
        encrypted_message = encrypt_message(message)
        client.send(encrypted_message)
        entry.delete(0, tk.END)
        
def attach_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "rb") as file:
            data = file.read()
            client.send(encrypt_message(f"FILE:{file_path}"))
            client.send(data)

def receive_message():
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            decrypted_message = decrypt_message(message)
            # Convert emojis in the message to their textual representation
            decrypted_message = emoji.demojize(decrypted_message)
            chat_window.insert(tk.END, f"Friend: {decrypted_message}\n")
        except Exception as e:
            print(f"Error: {e}")
            break
    client.close()

def load_chat_history():
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages ORDER BY timestamp")
    rows = cursor.fetchall()
    conn.close()
    return rows

def display_chat_history():
    history = load_chat_history()
    history_window = tk.Toplevel(root)
    history_window.title("Chat History")
    history_window.geometry("400x300")  # Adjust size as needed
    
    chat_history = tk.Text(history_window, height=15, width=50)
    chat_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scroll_y = tk.Scrollbar(history_window, orient=tk.VERTICAL, command=chat_history.yview)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
    
    chat_history.config(yscrollcommand=scroll_y.set)
    
    for row in history:
        chat_history.insert(tk.END, f"{row[1]} to {row[2]}: {row[3]}\n")

def resize_image(image_path, size):
    with Image.open(image_path) as img:
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

def show_history():
    display_chat_history()

def toggle_dark_mode():
    global is_dark_mode
    if is_dark_mode:
        root.config(bg="white")
        chat_window.config(bg="white", fg="black")
        entry.config(bg="lightgray", fg="black")
        frame.config(bg="white")
        send_button.config(bg="lightgray")
        attach_button.config(bg="lightgray")
        history_button.config(bg="lightgray")
        dark_mode_button.config(bg="lightgray")
        is_dark_mode = False
    else:
        root.config(bg="#2E2E2E")
        chat_window.config(bg="#2E2E2E", fg="white")
        entry.config(bg="#4B4B4B", fg="white")
        frame.config(bg="#2E2E2E")
        send_button.config(bg="#4B4B4B")
        attach_button.config(bg="#4B4B4B")
        history_button.config(bg="#4B4B4B")
        dark_mode_button.config(bg="#4B4B4B")
        is_dark_mode = True

# Initialize dark mode state
is_dark_mode = False

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

# GUI setup
root = tk.Tk()
root.title("Chat Application")

chat_window = tk.Text(root, height=20, width=50)
chat_window.pack()

# Frame for entry and buttons
frame = tk.Frame(root)
frame.pack(fill=tk.X, padx=5, pady=5)

entry = tk.Entry(frame, width=20)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_icon = resize_image("send_icon.png", (30, 30))
send_button = tk.Button(frame, image=send_icon, command=send_message)
send_button.pack(side=tk.LEFT)

attach_icon = resize_image("attach_icon.png", (20, 20))
attach_button = tk.Button(root, image=attach_icon, command=attach_file)
attach_button.pack(side=tk.LEFT)

history_button = tk.Button(root, text="Show Chat History", command=show_history)
history_button.pack(pady=5)

dark_mode_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode)
dark_mode_button.pack(pady=5)

# Start the thread for receiving messages
threading.Thread(target=receive_message, daemon=True).start()

root.mainloop()
