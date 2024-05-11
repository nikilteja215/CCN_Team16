# Team16 - Wav2Lip: Precision Lip-syncing for Real-world Videos"
Contributors - Sai Nikil Teja Swarna, Bhargavi Potu, Sruthi Bandi, Manoj Aitha

*About*
----------
This repository hosts the code for "A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild". It provides a comprehensive toolkit for generating accurate lip movements from speech in diverse real-world scenarios. With this technology, achieve seamless lip-syncing for any speech input, offering a versatile solution for various applications.

*Highlights*
----------
 - The visual quality discriminator's weights have been recently revised in the readme.
 - Achieve precise lip-syncing in videos to match any target speech with utmost accuracy :100:.
 - Compatible with all identities, voices, and languages, including CGI faces and synthetic voices. :sparkles: .
 - Access comprehensive training code, inference code, and pretrained models :boom:
 - Alternatively, get started quickly using the Google Colab Notebook [Link](https://colab.research.google.com/drive/1VHof_jhHvWlCtIeQNLFBGqJzDqCdJ9U4?usp=sharing).
 - Link to the original github [Link](https://github.com/Rudrabha/Wav2Lip)

*Prerequisites*
-------------
- Python 3.6 
- ffmpeg: sudo apt-get install ffmpeg
- Install necessary packages using `pip install -r requirements.txt`. Alternatively, instructions for using a docker image is provided [here](https://gist.github.com/xenogenesi/e62d3d13dadbc164124c830e9c453668). Have a look at [this comment](https://github.com/Rudrabha/Wav2Lip/issues/131#issuecomment-725478562) and comment on [the gist](https://gist.github.com/xenogenesi/e62d3d13dadbc164124c830e9c453668) if you encounter any issues. 
- Face detection [pre-trained model](https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth) should be downloaded to face_detection/detection/sfd/s3fd.pth. 

*Getting the weights:*
----------
| Model  | Description |  Link to the model | 
| :-------------: | :---------------: | :---------------: |
| Wav2Lip  | Highly accurate lip-sync | [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/Eb3LEzbfuKlJiR600lQWRxgBIY27JZg80f7V9jtMfbNDaQ?e=TBFBVW)  |
| Wav2Lip + GAN  | Slightly inferior lip-sync, but better visual quality | [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA?e=n9ljGW) |
| Expert Discriminator  | Weights of the expert discriminator | [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EQRvmiZg-HRAjvI6zqN9eTEBP74KefynCwPWVmF57l-AYA?e=ZRPHKP) |
| Visual Quality Discriminator  | Weights of the visual disc trained in a GAN setup | [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EQVqH88dTm1HjlK11eNba5gBbn15WMS0B0EZbDBttqrqkg?e=ic0ljo) |

*Easily lip-sync videos with the pre-trained models (Inference)*
-------
You can lip-sync any video to any audio 🗣️:
```bash
python inference.py --checkpoint_path <ckpt> --face <video.mp4> --audio <an-audio-source> 
```
- Synchronized video is saved by default in results/result_voice.mp4.
- Options allow specifying output location and other parameters.
- Supported audio sources include *.wav, *.mp3, or even video files, with automatic audio extraction.

#### Tips for better results:
- Experiment with the `--pads` argument for better face detection by adjusting bounding boxes. You might need to increase the bottom padding to include the chin region, e.g., `--pads 0 20 0 0`.
- Use `--nosmooth` to prevent over-smoothing if mouth positions appear dislocated or show duplicate mouths.
- Adjust `--resize_factor` for lower-resolution videos, potentially enhancing results for 720p compared to 1080p.
- For Wav2Lip model without GAN, further parameter tuning may be needed for optimal results, which can sometimes surpass other models.

*Train!*
----------
There are two major steps: 
(i) Train the expert lip-sync discriminator, 
(ii) Train the Wav2Lip model(s).

#### (i) Training the expert discriminator
- You can download [the pre-trained weights](#getting-the-weights) if you want to skip this step. To train it:
```bash
python color_syncnet_train.py --data_root lrs2_preprocessed/ --checkpoint_dir <folder_to_save_checkpoints>
```
#### (ii) Training the Wav2Lip models
- You can either train the model without the additional visual quality discriminator (< 1 day of training) or use the discriminator (~2 days). For the former, run: 
```bash
python wav2lip_train.py --data_root lrs2_preprocessed/ --checkpoint_dir <folder_to_save_checkpoints> --syncnet_checkpoint_path <path_to_expert_disc_checkpoint>
```

To train with the visual quality discriminator, you should run `hq_wav2lip_train.py` instead. The arguments for both files are similar. In both cases, you can resume training as well. Look at `python wav2lip_train.py --help` for more details. You can also set additional less commonly-used hyper-parameters at the bottom of the `hparams.py` file.

*Training on datasets other than LRS2*
------------------------------------
- Adapting the code for training on datasets other than LRS2 may be necessary.
- Achieving satisfactory results with minimal data or single-speaker samples is a complex research challenge we have yet to address.
- Prior to Wav2Lip training, it's essential to train the expert discriminator specifically for your dataset.
- If using a dataset obtained from the internet, synchronization correction is typically required.
- Take into account the FPS (frames per second) of your dataset's videos, as altering this parameter may necessitate significant code adjustments.
- For optimal outcomes, aim for an expert discriminator eval loss of approximately 0.25 and a Wav2Lip eval sync loss of around 0.2.

*Wave2Lip Application*
------------------------------------
This Streamlit application is designed to synchronize lip movements in a video with specified audio using the Wave2Lip model.

*Getting Started*
------------------------------------
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or later
- pip (Python package installer)
- Git (optional, only for cloning repository)


*Steps to execute the app*
------------------------------------
1. **Install Streamlit**: Install it using pip:`pip install streamlit` (Streamlit is essential for running the application)
2. Navigate to the `Wav2Lip` folder/directory
3. Run `streamlit run app.py`

### Real-Time Lip-Syncing App with Streamlit
To run this Streamlit app, ensure you have Python installed along with necessary dependencies such as Streamlit and hashlib. Follow these steps to get the application running:

*Key Components of the Application*
------------------------------------
### 1.) User Authentication System:

- **Initialization of Database:** Checks if the user data file (data.json) exists; if not, it creates one. This setup helps store user data securely.
- **Signup:** Users can create an account by entering their details. The system checks for existing users, validates email formats, and ensures password security by hashing passwords.
- **Login:** Users can log in with their credentials. The system validates the username and password against the stored data and allows access if the credentials are correct.
- **User Data Management:** Functions are provided to retrieve and manage user data, such as checking if a user exists or fetching user info from the database.

### 2.) Wave2Lip Functionality:

- **File Uploads:** Users can upload both audio and video files.
- **Processing:** The backend processes the uploaded files by invoking a system command that runs the Wave2Lip model, producing a lip-synced video.
- **Video Display:** Once the video is processed, it is displayed within the application.

### 3.) Page Layout and Navigation:

- **Main Function:** The main driver of the application, which initializes the database and manages the page layout.
- **Page Navigation:** Uses Streamlit's sidebar to navigate between Signup/Login, Dashboard, and Wave2Lip pages.
- **Dashboard Rendering:** Displays user-specific information if the user is logged in.

```python
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
```

*Detailed Steps and Functions*
------------------------------------

- `initialize_database(json_file_path="data.json")`: Ensures the JSON file for storing user data exists.
- `signup(json_file_path="data.json")`: Handles user registration, including form handling and validation.
- `login(json_file_path="data.json")`: Manages user login, including form handling and session management.
- `check_login(username, password, json_file_path="data.json")`: Checks login credentials against stored data.
- `create_account(name, email, age, sex, password, json_file_path="data.json")`: Registers a new user and adds them to the JSON database.
- `render_dashboard(user_info, json_file_path="data.json")`: Displays user information on the dashboard if the user is logged in.
- `main()`: Sets up the Streamlit page configurations and navigation, and manages page-specific functionalities.

*Guide to run the Streamlit application*
------------------------------------
- **Step 1**: Install Python from the official [Python website](https://www.python.org/downloads/) if not already installed.
- **Step 2**: Clone the application repository with `git clone https://github.com/Rudrabha/Wav2Lip.git`.
- **Step 3**: Change directory to the project folder: `cd path_to_streamlit_project`.
- **Step 4**: Create a virtual environment:
    - **Windows**: `python -m venv venv` and `venv\Scripts\activate`.
    - **macOS/Linux**: `python3 -m venv venv` and `source venv/bin/activate`.
- **Step 5**: Install required packages: `pip install -r requirements.txt`.
- **Step 6**: Ensure the user data file (`data.json`) is initialized by the app.
- **Step 7**: Start the application with `streamlit run app.py`.
- **Step 8**: Open a web browser and go to `http://localhost:8501` to access the app.
- **Step 9**: Use the app to sign up, log in, and access the Wave2Lip functionality.
- **Step 10**: To stop the application, press CTRL+C in the terminal.

*Evaluation*
----------
Please check the `evaluation/` folder for the instructions.
