import sqlite3
import reflex as rx

def user_dashboard(user_id):
    conn = sqlite3.connect('udemy_clone.db')
    c = conn.cursor()
    
    # Fetch enrolled courses
    c.execute('''SELECT courses.title, courses.description
                 FROM enrollments
                 JOIN courses ON enrollments.course_id = courses.id
                 WHERE enrollments.user_id=?''', (user_id,))
    enrolled_courses = c.fetchall()
    
    # Fetch user reviews
    c.execute('''SELECT courses.title, reviews.rating, reviews.comment
                 FROM reviews
                 JOIN courses ON reviews.course_id = courses.id
                 WHERE reviews.user_id=?''', (user_id,))
    reviews = c.fetchall()
    
    conn.close()
    
    return rx.box([
        rx.text("My Courses", font_size="1.5em"),
        rx.box([rx.text(f"{course[0]}: {course[1]}") for course in enrolled_courses]),
        rx.text("My Reviews", font_size="1.5em"),
        rx.box([rx.text(f"{review[0]}: {review[1]} stars - {review[2]}") for review in reviews])
    ])
