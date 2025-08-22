from flask import Flask, render_template, Response, jsonify
import cv2
from deepface import DeepFace
import numpy as np
import base64

app = Flask(__name__)

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Global variable to store current emotion
current_emotion = "No emotion detected"

def generate_frames():
    global current_emotion
    cap = cv2.VideoCapture(0)
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Convert grayscale frame to RGB format
        rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            # Extract the face ROI (Region of Interest)
            face_roi = rgb_frame[y:y + h, x:x + w]
            
            try:
                # Perform emotion analysis on the face ROI
                result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
                
                # Determine the dominant emotion
                current_emotion = result[0]['dominant_emotion']
                
                # Draw rectangle around face and label with predicted emotion
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, current_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            except Exception as e:
                print(f"Error in emotion detection: {e}")
        
        # Encode frame to base64 for sending to frontend
        _, buffer = cv2.imencode('.jpg', frame)
        frame_base64 = base64.b64encode(buffer).decode('utf-8')
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + base64.b64decode(frame_base64) + b'\r\n')
    
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_emotion')
def get_emotion():
    return jsonify({"emotion": current_emotion})

if __name__ == '__main__':
    app.run(debug=True)
