import sqlite3

def create_tables():
    conn = sqlite3.connect('udemy_clone.db')
    c = conn.cursor()
    
    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY,
                 username TEXT NOT NULL UNIQUE,
                 password TEXT NOT NULL)''')

    # Create courses table
    c.execute('''CREATE TABLE IF NOT EXISTS courses (
                 id INTEGER PRIMARY KEY,
                 title TEXT NOT NULL,
                 description TEXT NOT NULL,
                 video_url TEXT NOT NULL)''')

    # Create enrollments table
    c.execute('''CREATE TABLE IF NOT EXISTS enrollments (
                 user_id INTEGER,
                 course_id INTEGER,
                 FOREIGN KEY (user_id) REFERENCES users(id),
                 FOREIGN KEY (course_id) REFERENCES courses(id))''')

    # Create reviews table
    c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                 id INTEGER PRIMARY KEY,
                 user_id INTEGER,
                 course_id INTEGER,
                 rating INTEGER,
                 comment TEXT,
                 FOREIGN KEY (user_id) REFERENCES users(id),
                 FOREIGN KEY (course_id) REFERENCES courses(id))''')
    
    conn.commit()
    conn.close()

create_tables()
