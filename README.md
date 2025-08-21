🎯 Face Recognition Attendance System

A simple Face Recognition Attendance System built with Python.
It uses computer vision and machine learning to detect and recognize faces for attendance logging.

🚀 Technologies Used

face_recognition
 → Facial detection & encoding

OpenCV → Webcam access & image processing

Tkinter + ttk → Modern graphical interface

CSV → Attendance logging

✨ Features

✅ Add a new user by taking a photo with the webcam
✅ Scan faces in real-time to log attendance
✅ Automatically record the date & time of attendance
✅ Store user photos in the ImagesAttendance/ folder
✅ View and update attendance in the Attendance.csv file

🛠️ How It Works

The program loads all images from ImagesAttendance/ and generates facial encodings.

When you click "Scan Face", the webcam opens and scans for faces.

If a match is found:

The user’s name + timestamp is saved in Attendance.csv (only once per session).

You can add a new user by clicking "Add User", entering their name, and taking a photo.

📂 Project Structure
📁 project_root/
│── interface.py        # Tkinter GUI + add_user function
│── main.py             # Face recognition logic
│── ImagesAttendance/   # Folder to store user images
│── Attendance.csv      # CSV file to log attendance
│── requirements.txt    # Project dependencies
│── README.md           # Project documentation

⚙️ Installation

Clone the repository

git clone https://github.com/RamyGarici/FaceRecognitionAttendanceSystem.git
cd FaceRecognitionAttendanceSystem


Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


⚠️ If you face issues installing dlib (a dependency of face_recognition), check the official guide:
👉 face_recognition installation instructions

▶️ Running the App
python main.py

📝 Notes

Ensure your webcam is connected.

New user images are saved in ImagesAttendance/ with the provided name.

You can manually inspect or reset Attendance.csv when needed.


👤 Author

Ramy Garici
