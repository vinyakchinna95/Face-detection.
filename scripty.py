import cv2
import streamlit as st
import numpy as np

# Load the Haar cascade file for face detection
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return image, len(faces)

def main():
    st.title("🕵️ Real-Time Face Detection with Streamlit & OpenCV")

    run = st.checkbox("Start Webcam")

    if run:
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            st.error("Could not open webcam. Please check your camera settings.")
            return
        
        stframe = st.empty()

        while run:
            ret, frame = video_capture.read()
            if not ret:
                st.error("Failed to capture image.")
                break
            
            frame, faces_count = detect_faces(frame)

            # Convert frame to RGB (OpenCV uses BGR by default)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display the video frame
            stframe.image(frame, channels="RGB", use_column_width=True)

            st.write(f"Detected Faces: {faces_count}")

        video_capture.release()

if __name__ == "__main__":
    main()
