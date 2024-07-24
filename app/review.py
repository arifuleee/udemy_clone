import sqlite3
import reflex as rx

def review_form(course_id):
    return rx.form([
        rx.input(placeholder="Rating (1-5)"),
        rx.textarea(placeholder="Comment"),
        rx.button("Submit Review", type="submit")
    ], on_submit=lambda form_data: submit_review(course_id, form_data))

def submit_review(course_id, form_data):
    rating = int(form_data['rating'])
    comment = form_data['comment']
    #user_id = get_current_user_id()  # Assuming you have a way to get the logged-in user's ID
    
    conn = sqlite3.connect('udemy_clone.db')
    c = conn.cursor()
    #c.execute('INSERT INTO reviews (user_id, course_id, rating, comment) VALUES (?, ?, ?, ?)', (user_id, course_id, rating, comment))
    conn.commit()
    conn.close()
