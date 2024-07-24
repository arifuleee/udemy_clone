import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def signup(username, password):
    conn = sqlite3.connect('udemy_clone.db')
    c = conn.cursor()
    hashed_password = generate_password_hash(password)
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        return "User registered successfully"
    except sqlite3.IntegrityError:
        return "Username already exists"
    finally:
        conn.close()

def login(username, password):
    conn = sqlite3.connect('udemy_clone.db')
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username=?', (username,))
    result = c.fetchone()
    conn.close()
    if result and check_password_hash(result[0], password):
        return "Login successful"
    return "Invalid username or password"
