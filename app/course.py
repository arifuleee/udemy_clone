import sqlite3
import reflex as rx
from .s3 import upload_video_to_s3

def create_course(form_data):
    title = form_data['title']
    description = form_data['description']
    video_file = form_data['video']
    video_url = upload_video_to_s3(video_file, 'your-bucket-name')
    
    conn = sqlite3.connect('udemy_clone.db')
    c = conn.cursor()
    c.execute('INSERT INTO courses (title, description, video_url) VALUES (?, ?, ?)', (title, description, video_url))
    conn.commit()
    conn.close()

def course_component(course):
    return rx.box([
        rx.text(course['title'], font_size="1.5em"),
        rx.text(course['description']),
        rx.button("Enroll", on_click=lambda: enroll(course['id']))
    ])

def course_list():
    conn = sqlite3.connect('udemy_clone.db')
    c = conn.cursor()
    c.execute('SELECT * FROM courses')
    courses = c.fetchall()
    conn.close()
    return rx.box([course_component(course) for course in courses])

def enroll(course_id):
    # Assume a user_id is available from session management
    #user_id = get_current_user_id()
    conn = sqlite3.connect('udemy_clone.db')
    c = conn.cursor()
    #c.execute('INSERT INTO enrollments (user_id, course_id) VALUES (?, ?)', (user_id, course_id))
    conn.commit()
    conn.close()
