import reflex as rx
from app.auth import signup, login
from app.course import create_course, course_list
from app.dashboard import user_dashboard
from app.database import create_tables
from app.review import review_form
from app.utils import get_current_user_id

create_tables()

def signup_form():
    return rx.form([
        rx.input(placeholder="Username"),
        rx.input(type="password", placeholder="Password"),
        rx.button("Sign Up", type="submit")
    ], on_submit=lambda form_data: signup(form_data['Username'], form_data['Password']))

def login_form():
    return rx.form([
        rx.input(placeholder="Username"),
        rx.input(type="password", placeholder="Password"),
        rx.button("Log In", type="submit")
    ], on_submit=lambda form_data: login(form_data['Username'], form_data['Password']))

def course_creation_form():
    return rx.form([
        rx.input(placeholder="Title"),
        rx.textarea(placeholder="Description"),
        rx.input(type="file", name="video"),
        rx.button("Create Course", type="submit")
    ], on_submit=create_course)

app = rx.App()

app.add_component(rx.text("Welcome to Udemy Clone", font_size="2em"))
app.add_component(signup_form)
app.add_component(login_form)
app.add_component(course_list())
app.add_component(course_creation_form)

user_id = get_current_user_id()  # Placeholder
app.add_component(user_dashboard(user_id))

if __name__ == "__main__":
    app.run()
