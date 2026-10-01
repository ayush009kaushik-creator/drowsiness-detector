# 🚗 Drowsiness Detector

A Python-based real-time drowsiness detection system designed to detect driver fatigue and provide an alarm alert.

## 📌 About the Project

The Drowsiness Detector uses computer vision to monitor the driver's face and eyes. When signs of drowsiness are detected, the system triggers an alarm to alert the driver.

## ✨ Features

- 👁️ Eye detection
- 🙂 Face detection
- 🚨 Alarm alert when drowsiness is detected
- ⚡ Real-time detection using webcam
- 🐍 Built with Python and OpenCV

## 🛠️ Technologies Used

- Python
- OpenCV
- Haar Cascade Classifiers
- Computer Vision

## 📂 Project Structure

```text
drowsiness-detector/
│
├── main.py
├── alarm.wav
├── haarcascade_eye.xml
├── haarcascade_frontalface_default.xml
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Installation
Clone the repository:
git clone https://github.com/ayush009kaushik-creator/drowsiness-detector.git
Go to the project folder:
cd drowsiness-detector
Install the required packages:
pip install -r requirements.txt
▶️ How to Run
Run the following command:
python main.py
Make sure your webcam is connected and working.
🚨 How It Works
The webcam captures the driver's face.
The system detects the eyes and face.
It monitors signs of drowsiness.
If drowsiness is detected, an alarm is triggered.
👨‍💻 Author
Ayush
📄 License
This project is for educational purposes.


