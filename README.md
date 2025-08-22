# 🎭 Real-time Emotion Detection with Flask + DeepFace

This project is a **real-time facial emotion detection web app** built using **Flask, OpenCV, and DeepFace**.  
It captures video from your webcam, detects faces, analyzes emotions, and streams results to a **beautiful animated frontend**.

---

## ✨ Features
- 🎥 **Real-time video feed** using OpenCV + Flask streaming  
- 🎨 **Interactive & animated frontend** with dynamic backgrounds and emoji effects  
- 📊 Displays **dominant emotion** in real-time  
- ⚡ Lightweight and runs locally with your webcam  

---

## 📂 Project Structure

facial-emotion-detection-with-animated-emojes-/
│── app.py # Flask backend
│── templates/
│ └── index.html # Frontend UI
│── requirements.txt # Dependencies
│── README.md # Project documentation


---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   [git clone https://github.com/your-username/emotion-detection-app.git](https://github.com/Arfasil/facial-emotion-detection-with-animinated-emojes-.git)
   cd facial-emotion-detection-with-animinated-emojes-
2.Create a virtual environment (recommended)
  python -m venv venv
  source venv/bin/activate    # On Mac/Linux
  venv\Scripts\activate       # On Windows

3.Install dependencies

  pip install -r requirements.txt

4.🚀 Running the App

   Start the Flask server:

    python app.py


By default, it runs on http://127.0.0.1:5000/

🖼️ Demo Preview

The app opens in your browser.

Your webcam feed appears.

Detected emotions are shown with animated emojis & text.

Background gradients & effects change based on emotions.


⚠️ Troubleshooting

Camera not opening?
Make sure no other app is using your webcam.
On Linux/Mac, check cv2.VideoCapture(0) and try changing to cv2.VideoCapture(1) if multiple cameras.

DeepFace errors?
First-time use downloads pretrained models. Keep internet on for the first run.

Page not loading?
Ensure Flask server is running at http://127.0.0.1:5000/.

🤝 Contributing

Pull requests and issues are welcome!
If you have feature ideas (e.g., multi-person emotion tracking, saving logs, dashboard), feel free to contribute.

📜 License

This project is licensed under the MIT License.
You’re free to use and modify it as long as attribution is given.

👨‍💻 Author

Developed by A R Mohammed Fasil
 ✨




