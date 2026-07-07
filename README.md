AI Virtual Classroom

📚 Overview

AI Virtual Classroom is an AI-powered smart classroom system that automates attendance, monitors student engagement, generates lecture notes, creates quizzes, and predicts student performance. It combines Computer Vision, Natural Language Processing (NLP), Speech Recognition, and Machine Learning into a single web application.

---

🚀 Features

- 🎯 Face Recognition Attendance
- 😊 Real-time Emotion Detection
- 🎤 Automatic Speech-to-Text Notes
- 📝 AI Quiz Generation from Lecture Notes
- 📊 Student Performance Prediction
- 👨‍🎓 Student Registration
- 📋 Attendance Reports
- 💾 SQLite Database
- 🌐 Flask Web Dashboard

---

🛠️ Technologies Used

- Python
- Flask
- OpenCV
- face_recognition
- DeepFace
- Whisper (Speech-to-Text)
- Hugging Face Transformers
- Scikit-learn
- SQLite
- HTML
- CSS
- JavaScript

---

📂 Project Structure

AI_Virtual_Classroom/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── attendance/
│   ├── attendance.py
│   ├── register_student.py
│   └── faces/
│
├── emotion/
│   └── emotion_detector.py
│
├── notes/
│   ├── speech_to_text.py
│   ├── summarizer.py
│   └── pdf_notes.py
│
├── quiz/
│   ├── quiz_generator.py
│   └── evaluate.py
│
├── prediction/
│   ├── train_model.py
│   ├── predictor.py
│   └── student_dataset.csv
│
├── database/
│   ├── database.py
│   └── classroom.db
│
├── static/
│
└── templates/

---

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/AI_Virtual_Classroom.git

Open the project folder:

cd AI_Virtual_Classroom

Install the required libraries:

pip install -r requirements.txt

Create the database:

python database/database.py

Run the application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000

---

📸 Modules

1. Face Recognition Attendance

- Detects registered students.
- Marks attendance automatically.
- Stores attendance in the database.

2. Emotion Detection

- Detects emotions such as Happy, Sad, Angry, Neutral, Fear, and Surprise.
- Displays student engagement in real time.

3. Automatic Notes

- Converts teacher speech into text.
- Generates summarized lecture notes.
- Saves notes as PDF.

4. Quiz Generator

- Generates multiple-choice questions from lecture notes.
- Evaluates student answers.

5. Performance Prediction

- Uses attendance, quiz scores, and assignment marks.
- Predicts student performance using Machine Learning.

---

📦 Required Libraries

- Flask
- OpenCV
- face_recognition
- DeepFace
- TensorFlow
- NumPy
- Pandas
- Scikit-learn
- Whisper
- Transformers
- Torch
- ReportLab
- python-docx

---

🎯 Future Enhancements

- Online Live Classroom
- Teacher Login
- Student Login
- Parent Dashboard
- Google Classroom Integration
- Email Notifications
- Voice Assistant
- Hand Raise Detection
- Eye Gaze Tracking
- Cheating Detection During Exams
- Mobile Application

---

👨‍💻 Author

Akash B R

Final Year Engineering Project

---

📄 License

This project is intended for educational and academic purposes.
