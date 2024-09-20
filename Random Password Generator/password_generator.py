import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    if not any([use_uppercase, use_lowercase, use_numbers, use_symbols]):
        messagebox.showerror("Error", "Please select at least one character set.")
        return

    character_set = ""
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    password = ''.join(random.choice(character_set) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.config(bg="lightblue")

# Title Label
title_label = tk.Label(root, text="Random Password Generator", font=("Helvetica", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Password Length
length_label = tk.Label(root, text="Password Length:", bg="lightblue", font=("Arial", 12))
length_label.pack(pady=5)
length_entry = tk.Entry(root, width=5)
length_entry.pack()

# Character Set Options
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, bg="lightblue", font=("Arial", 10)).pack()
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var, bg="lightblue", font=("Arial", 10)).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, bg="lightblue", font=("Arial", 10)).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="lightblue", font=("Arial", 10)).pack()

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="green", fg="white")
generate_button.pack(pady=10)

# Password Entry
password_entry = tk.Entry(root, width=30, font=("Arial", 14), justify="center")
password_entry.pack(pady=5)

# Copy to Clipboard Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="orange", fg="white")
copy_button.pack(pady=10)

root.mainloop()
