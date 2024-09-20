import sqlite3

print("Starting chat_history.py script...")

# Create the chat.db database and table
def create_chat_db():
    print("Creating chat.db...")
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    
    # Create the chat table
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sender TEXT NOT NULL,
                        receiver TEXT,
                        message TEXT NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                      )''')
    
    conn.commit()
    conn.close()
    print("Chat history database created successfully!")

# Function to save a message
def save_message(sender, receiver, message):
    print(f"Saving message from {sender}...")
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)", (sender, receiver, message))
    conn.commit()
    conn.close()
    print("Message saved successfully!")

# Function to retrieve message history
def retrieve_history():
    print("Retrieving chat history...")
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute("SELECT * FROM messages")
    rows = c.fetchall()
    conn.close()
    return rows

# Function to load chat history
def load_chat_history():
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages ORDER BY timestamp")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Create the database and table when running this script
if __name__ == "__main__":
    create_chat_db()
    
    # # For testing: Save a message and retrieve history
    # save_message("Alice", "Bob", "Hello, Bob!")
    
    # # Retrieve and print chat history
    # history = load_chat_history()
    # print("Chat History:")
    # for row in history:
    #     print(row)
