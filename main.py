import face_recognition
import cv2
import numpy as np
import os 
from datetime import datetime

#Load images from the directorys

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg=  face_recognition.load_image_file(f'{path}/{cl}')
   
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
    

# Function to encode images list

def findEncodings(images):
    encodelist = []
    for img in images:
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)   
    return encodelist

# Mark attendance in a csv file


def mark_attendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
 
    
    
    
    
encodelistKnown = findEncodings(images)


# Face recognition function

def start_face_recognition():
    try:
        
        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            
            
            
            
            imgS = cv2.resize(img,(0,0),None,0.25,0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
    
            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodelistKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodelistKnown, encodeFace)
        
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()

                    y1,x2,y2,x1 = faceLoc
                    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    mark_attendance(name)
            
            
            cv2.imshow('Webcam',img)
            cv2.waitKey(1)
            if cv2.getWindowProperty('Webcam', cv2.WND_PROP_VISIBLE) < 1:
                break
            
            
        cap.release()
        cv2.destroyAllWindows()
    
    except Exception as e:
        print(f"[ERROR] {e}")
        try:
            from tkinter import messagebox
            messagebox.showerror("Camera Error", str(e))
        except:
            pass
           

if __name__ == "__main__":
    from interface import launch_interface
    launch_interface()



