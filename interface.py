import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import cv2
import os


IMAGE_DIR = 'ImagesAttendance'


#Function to add a new user

def add_user():
    name = simpledialog.askstring("User Name", "Enter the user's name:")
    if not name:
        return

    cap = cv2.VideoCapture(0)
    messagebox.showinfo("Capture", "Press 's' to capture the photo, 'q' to quit.")

    while True:
        success, frame = cap.read()
        if not success:
            break
        cv2.imshow("Add User", frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            filename = os.path.join(IMAGE_DIR, f"{name}.jpg")
            cv2.imwrite(filename, frame)
            messagebox.showinfo("Success", f"Image saved as {filename}")
            break
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Funtion to launch the face recognition scan

def scan_face():
    try:
        import main  
        main.start_face_recognition() 
    except Exception as e:
        messagebox.showerror("Error", f"Error during scan: {e}")

# Main interface

def launch_interface():
    root = tk.Tk()
    root.title("Face Recognition System")
    root.geometry("400x300")
    root.configure(bg="#2c3e50")

    style = ttk.Style(root)
    style.configure("TButton", font=("Segoe UI", 12), padding=10)

    ttk.Label(root, text="Face Recognition Attendance", font=("Segoe UI", 16), background="#2c3e50", foreground="white").pack(pady=20)

    ttk.Button(root, text="Add User", command=add_user).pack(pady=10)
    ttk.Button(root, text="Scan Face", command=scan_face).pack(pady=10)
    ttk.Button(root, text="Show Attendance", command=show_attendance).pack(pady=10)


    root.mainloop()
    
    

# Show the attendance table
def show_attendance():
    window = tk.Toplevel()
    window.title("Attendance Records")
    window.geometry("400x300")
    
    tree = ttk.Treeview(window, columns=("Name", "Time"), show="headings")
    tree.heading("Name", text="Name")
    tree.heading("Time", text="Time")
    tree.column("Name", width=150)
    tree.column("Time", width=100)
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    try:
        with open("Attendance.csv", "r") as f:
            for line in f:
                values = line.strip().split(",")
                if len(values) == 2:
                    tree.insert("", "end", values=values)
    except FileNotFoundError:
        messagebox.showerror("Error", "Attendance file not found.")

