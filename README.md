# Face Recognition Attendance System

This project is a simple **Face Recognition Attendance System** built with Python using the following technologies:
- `face_recognition` for facial detection and encoding
- `OpenCV` for webcam access and image processing
- `Tkinter` and `ttk` for a modern graphical interface
- `CSV` file to log attendance

## Features

✅ Add a new user by taking a photo with the webcam  
✅ Scan faces in real time to log attendance  
✅ Automatically record the date and time of attendance  
✅ Store user photos in the `ImagesAttendance` folder  
✅ View and update attendance in the `Attendance.csv` file

## How It Works

1. The program loads all images from the `ImagesAttendance/` folder and generates facial encodings.
2. When the user clicks **"Scan Face"**, the webcam opens and tries to match detected faces with known encodings.
3. If a match is found, the user's name and the current time are saved in `Attendance.csv` (only once per session).
4. New users can be added by clicking **"Add User"**, entering their name, and taking a photo.

## File Structure

📁 project_root/
├── interface.py # Tkinter GUI and add_user function
├── main.py # Face recognition logic
├── ImagesAttendance/ # Folder to store user images
├── Attendance.csv # CSV file to log attendance
├── requirements.txt # List of dependencies


## Installation

1. Make sure Python 3.7+ is installed.
2. Install required packages from `requirements.txt`:


pip install -r requirements.txt
If you face issues with dlib (dependency of face_recognition), refer to platform-specific installation instructions on the face_recognition GitHub.

Running the App
Launch the main script to start the interface:

python main.py

Notes
Make sure your webcam is properly connected.

The user photo will be saved with the name provided in ImagesAttendance/.

You can manually inspect or clear Attendance.csv as needed.

Author
Ramy Garici
https://github.com/RamyGarici

