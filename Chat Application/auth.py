import sqlite3
import bcrypt

print("Starting auth.py script...")

# Create the users.db database and table
def create_user_db():
    print("Creating users.db...")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create the users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password_hash TEXT NOT NULL
                      )''')
    
    conn.commit()
    conn.close()
    print("User database created successfully!")

# Function to add a new user (register)
def register_user(username, password):
    print(f"Registering user {username}...")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Hash the password before storing it
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        print(f"User {username} registered successfully!")
    except sqlite3.IntegrityError:
        print(f"Username {username} is already taken!")
    
    conn.close()

# Function to authenticate a user
def authenticate_user(username, password):
    print(f"Authenticating user {username}...")
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE username=?", (username,))
    stored_password_hash = c.fetchone()
    conn.close()
    
    if stored_password_hash and bcrypt.checkpw(password.encode('utf-8'), stored_password_hash[0]):
        print(f"User {username} authenticated successfully!")
        return True
    print(f"Authentication failed for user {username}.")
    return False

# Create the database and optionally register a test user when running this script
if __name__ == "__main__":
    create_user_db()
    # Example: Register a test user
    # register_user("testuser", "password123")
    # Example: Authenticate a test user
    # authenticate_user("testuser", "password123")
