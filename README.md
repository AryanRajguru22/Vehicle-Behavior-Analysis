🚦 Vehicle Behavior Analysis System
AI-Based Traffic Monitoring using YOLOv8 + OpenCV + PyTorch
📌 Project Overview

Vehicle Behavior Analysis is an AI-powered real-time traffic monitoring system that:

Detects vehicles and pedestrians

Estimates vehicle speed

Detects over-speeding

Detects traffic congestion

Detects wrong-side driving

Counts vehicles in lanes

Supports Live CCTV / YouTube / RTSP / Local video

Built using:

YOLOv8 (Ultralytics)

OpenCV

PyTorch (CUDA GPU enabled)

Python 3.11

🎯 Problem Statement

Traditional traffic monitoring systems rely heavily on manual supervision.

This project provides:

Automated traffic rule violation detection

Real-time analytics

Scalable AI-based monitoring system

Foundation for Smart City Infrastructure

⚙️ Features Implemented (MTE Version)
✅ Vehicle & Person Detection

YOLOv8-based object detection

Real-time multi-object tracking

✅ Speed Estimation

Pixel-to-meter conversion

Smoothed speed calculation

Over-speed detection

✅ Traffic Jam Detection

Detects slow-moving vehicle clusters

Time-based congestion logic

✅ Lane-Based Counting

Counts vehicles currently present in frame

Top and bottom lane classification

✅ Wrong-Side Driving Detection

Direction-based motion tracking

Flags vehicles moving opposite to allowed direction

✅ Multiple Input Sources

Local Video

YouTube Live Stream

RTSP CCTV

USB Webcam

🧠 System Architecture

Video Input
→ YOLOv8 Detection
→ Tracking
→ Speed Estimation
→ Jam Detection
→ Wrong-Side Detection
→ Frame Visualization

🖥️ Hardware Used

NVIDIA GeForce RTX 3050 6GB Laptop GPU

CUDA 12.1 Enabled

Python 3.11

📂 Project Structure
Vehicle-Behavior-Analysis/
│
├── modules/
│   ├── detector.py
│   ├── tracker.py
│   ├── speed_estimator.py
│   ├── jam_detector.py
│   ├── vehicle_counter.py
│   ├── wrong_side_detector.py
│
├── dashboard/
├── database/
├── data/
│
├── config.py
├── main.py
├── requirements.txt
└── README.md

🚀 How to Run
1️⃣ Clone Repository
git clone https://github.com/AryanRajguru22/Vehicle-Behavior-Analysis.git
cd Vehicle-Behavior-Analysis

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Application
python main.py

🔧 Configuration

Edit config.py to change:

Video source type

Speed limits

Jam thresholds

Model path

Frame skip

Allowed direction for wrong-side detection

📊 Current Performance

GPU Utilization: ~45%

Real-time detection with frame skipping

Optimized for 720p live streams

📈 Future Scope (End-Term Vision)

Automatic violation image capture

ANPR (Number Plate Recognition)

Database logging system

Flask-based monitoring dashboard

Deployment on edge devices

Cloud integration

REST API service

Multi-camera scaling

Docker containerization

🏆 Academic Context

Developed as part of:

Problem Based Learning (PBL)
Semester 4 – Mini Project Evaluation (MTE)

👨‍💻 Author

Aryan Rajguru
B. Tech. Computer Science and Engineering

GitHub:
https://github.com/AryanRajguru22