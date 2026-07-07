from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from config import *

app = Flask(__name__)
app.secret_key = SECRET_KEY


# ------------------------
# Database Connection
# ------------------------
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# ------------------------
# Home
# ------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ------------------------
# Dashboard
# ------------------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ------------------------
# Register Student
# ------------------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        usn = request.form["usn"]
        department = request.form["department"]

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO students(name, usn, department)
            VALUES (?, ?, ?)
        """, (name, usn, department))

        conn.commit()
        conn.close()

        flash("Student Registered Successfully!")

        return redirect(url_for("students"))

    return render_template("register.html")


# ------------------------
# Student List
# ------------------------
@app.route("/students")
def students():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    conn.close()

    return render_template("students.html", students=data)


# ------------------------
# Attendance Page
# ------------------------
@app.route("/attendance")
def attendance():
    return render_template("attendance.html")


@app.route("/start_attendance")
def start_attendance():
    os.system("python attendance/attendance.py")
    flash("Attendance Process Started")
    return redirect(url_for("attendance"))


# ------------------------
# Emotion Detection
# ------------------------
@app.route("/emotion")
def emotion():
    return render_template("emotion.html")


@app.route("/start_emotion")
def start_emotion():
    os.system("python emotion/emotion_detector.py")
    flash("Emotion Detection Started")
    return redirect(url_for("emotion"))


# ------------------------
# Automatic Notes
# ------------------------
@app.route("/notes")
def notes():
    return render_template("notes.html")


@app.route("/generate_notes")
def generate_notes():
    os.system("python notes/speech_to_text.py")
    flash("Lecture Notes Generated")
    return redirect(url_for("notes"))


# ------------------------
# Quiz Generator
# ------------------------
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/generate_quiz")
def generate_quiz():
    os.system("python quiz/quiz_generator.py")
    flash("Quiz Generated Successfully")
    return redirect(url_for("quiz"))


# ------------------------
# Performance Prediction
# ------------------------
@app.route("/prediction")
def prediction():
    return render_template("prediction.html")


@app.route("/predict")
def predict():
    os.system("python prediction/predictor.py")
    flash("Prediction Completed")
    return redirect(url_for("prediction"))


# ------------------------
# Reports
# ------------------------
@app.route("/reports")
def reports():

    conn = get_db()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")

    attendance = cursor.fetchall()

    conn.close()

    return render_template(
        "reports.html",
        attendance=attendance
    )


# ------------------------
# About
# ------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# ------------------------
# Exit
# ------------------------
@app.route("/exit")
def exit_app():
    flash("Thank you for using AI Virtual Classroom")
    return redirect(url_for("home"))


# ------------------------
# Main
# ------------------------
if __name__ == "__main__":

    if not os.path.exists("database"):
        os.makedirs("database")

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
