import json
import os
import streamlit as st
import re
import hashlib


session_state = st.session_state
if "user_index" not in st.session_state:
    st.session_state["user_index"] = 0

st.set_page_config(
    page_title="Wave2Lip App",
    page_icon="favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded",
)



def user_exists(email, json_file_path):
    # Function to check if user with the given email exists
    with open(json_file_path, "r") as file:
        users = json.load(file)
        for user in users["users"]:
            if user["email"] == email:
                return True
    return False


def signup(json_file_path="data.json"):
    st.title("Signup Page")
    with st.form("signup_form"):
        st.write("Fill in the details below to create an account:")
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        age = st.number_input("Age:", min_value=0, max_value=120)
        sex = st.radio("Sex:", ("Male", "Female", "Other"))
        password = st.text_input("Password:", type="password")
        confirm_password = st.text_input("Confirm Password:", type="password")
        if st.form_submit_button("Signup"):
            if not name:
                st.error("Name field cannot be empty.")
            elif not email:
                st.error("Email field cannot be empty.")
            elif not re.match(r"^[\w\.-]+@[\w\.-]+$", email):
                st.error("Invalid email format. Please enter a valid email address.")
            elif user_exists(email, json_file_path):
                st.error(
                    "User with this email already exists. Please choose a different email."
                )
            elif not age:
                st.error("Age field cannot be empty.")
            elif not password or len(password) < 6:  # Minimum password length of 6
                st.error("Password must be at least 6 characters long.")
            elif password != confirm_password:
                st.error("Passwords do not match. Please try again.")
            else:
                user = create_account(
                        name,
                        email,
                        age,
                        sex,
                        password,
                        json_file_path,
                    )
                session_state["logged_in"] = True
                session_state["user_info"] = user
                st.success("Signup successful. You are now logged in!")



def check_login(username, password, json_file_path="data.json"):
    try:
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        for user in data["users"]:
            if user["email"] == username and user["password"] == password:
                session_state["logged_in"] = True
                session_state["user_info"] = user
                st.success("Login successful!")
                return user
        return None
    except Exception as e:
        st.error(f"Error checking login: {e}")
        return None


def initialize_database(json_file_path="data.json"):
    try:
        if not os.path.exists(json_file_path):
            data = {"users": []}
            with open(json_file_path, "w") as json_file:
                json.dump(data, json_file)

    except Exception as e:
        print(f"Error initializing database: {e}")


def create_account(
    name, email, age, sex, password, json_file_path="data.json"
):
    try:
        if not os.path.exists(json_file_path) or os.stat(json_file_path).st_size == 0:
            data = {"users": []}
        else:
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)

        # Append new user data to the JSON structure
        email = email.lower()
        password = hashlib.md5(password.encode()).hexdigest()
        user_info = {
            "name": name,
            "email": email,
            "age": age,
            "sex": sex,
            "password": password,
        }

        data["users"].append(user_info)

        with open(json_file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        st.success("Account created successfully! You can now login.")
        return user_info
    except json.JSONDecodeError as e:
        st.error(f"Error decoding JSON: {e}")
        return None
    except Exception as e:
        st.error(f"Error creating account: {e}")
        return None


def login(json_file_path="data.json"):
    st.title("Login Page")
    username = st.text_input("Email:")
    password = st.text_input("Password:", type="password")
    password = hashlib.md5(password.encode()).hexdigest()
    username = username.lower()

    login_button = st.button("Login")

    if login_button:
        user = check_login(username, password, json_file_path)
        if user is not None:
            session_state["logged_in"] = True
            session_state["user_info"] = user
        else:
            st.error("Invalid credentials. Please try again.")


def get_user_info(email, json_file_path="data.json"):
    try:
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
            for user in data["users"]:
                if user["email"] == email:
                    return user
        return None
    except Exception as e:
        st.error(f"Error getting user information: {e}")
        return None


def render_dashboard(user_info, json_file_path="data.json"):
    try:
        st.title(f"Welcome to the Dashboard, {user_info['name']}!")
        st.subheader("User Information:")
        st.write(f"Name: {user_info['name']}")
        st.write(f"Sex: {user_info['sex']}")
        st.write(f"Age: {user_info['age']}")

    except Exception as e:
        st.error(f"Error rendering dashboard: {e}")


def main():
    st.title("Wave2Lip App")
    page = st.sidebar.radio(
        "Go to",
        (
            "Signup/Login",
            "Dashboard",
            "Wave2Lip",
        ),
        key="page",
    )

    if page == "Signup/Login":
        st.title("Signup/Login Page")
        login_or_signup = st.radio(
            "Select an option", ("Login", "Signup"), key="login_signup"
        )
        if login_or_signup == "Login":
            login()
        else:
            signup()

    elif page == "Dashboard":
        if session_state.get("logged_in"):
            render_dashboard(session_state["user_info"])
        else:
            st.warning("Please login/signup to view the dashboard.")

    elif page == "Wave2Lip":
        if session_state.get("logged_in"):

            st.title("Wave2Lip App")
            st.write("Upload the audio and video files below to start the process:")
            
            audio_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])
            video_file = st.file_uploader("Upload video file", type=["mp4", "avi", "mov"])
            if audio_file and video_file:
                with open(audio_file.name, "wb") as f:
                    f.write(audio_file.getbuffer())
                with open(video_file.name, "wb") as f:
                    f.write(video_file.getbuffer())
                st.success("Files uploaded successfully!")
                with st.spinner("Processing..."):
                    # if os.path.exists("results//result_voice.mp4"):
                    #     os.remove("results//result_voice.mp4")
                    os.system(f"python inference.py --checkpoint_path wav2lip_gan.pth --face {video_file.name} --audio {audio_file.name}")
                    st.markdown(
                                f"<p style='color:green; font-size:20px;'>Output video saved successfully</p>",
                                unsafe_allow_html=True,
                            )
                st.video("results//result_voice.mp4")
        else:
            st.warning("Please login/signup to access this page.")
if __name__ == "__main__":
    initialize_database()
    main()
