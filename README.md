#  Vehicle Behavior Analysis & Intelligent Traffic Monitoring System  


##  Project Presentation

🔗 PPT : [View Presentation](https://docs.google.com/presentation/d/1o89KxDN3CUS8ysNKERa8RecxQSOQQMDO/edit?slide=id.p1#slide=id.p1)


##  Overview

This project implements a real-time intelligent traffic monitoring system using deep learning and computer vision.

Unlike traditional systems that only detect isolated violations, this system focuses on vehicle behaviour analysis to understand traffic flow and congestion patterns.

The prototype supports:

- Real-time vehicle detection  
- Persistent ID tracking  
- Speed estimation  
- Congestion (Jam) detection  
- Speed violation monitoring  
- Vehicle counting  
- Experimental wrong-side detection  

The system is designed with a modular architecture, GPU acceleration, and Smart City scalability in mind.

---

##  System Architecture

Video Input  
↓  
Frame Preprocessing  
↓  
YOLOv8 Detection (GPU)  
↓  
Persistent Tracking  
↓  
Behaviour Analysis Engine  
↓  
Violation & Event Classification  
↓  
Visualization / Dashboard  

---

##  Features Implemented

✔ Real-time vehicle detection using YOLOv8  
✔ CUDA-based GPU acceleration  
✔ Multi-source input support (Video / RTSP / YouTube / Webcam)  
✔ Persistent vehicle ID tracking  
✔ Real-time speed estimation (Pixel-to-Meter calibrated)  
✔ Speed violation detection  
✔ Intelligent jam detection (ratio + time threshold based)  
✔ Vehicle counting per frame  
✔ Frame skipping optimization  
✔ Speed smoothing using Exponential Moving Average  
✔ Modular and scalable project structure  

---

##  Wrong-Side Detection (Experimental)

The system includes a direction-based wrong-side detection module that:

- Analyzes horizontal displacement (Δx) of tracked vehicles  
- Compares movement with configured allowed road direction  
- Flags opposite motion as potential violation  

Current Status:
- Works best when road direction is horizontally aligned  
- May produce inaccurate results in diagonal or complex road layouts  
- Currently under refinement for improved vector-based motion analysis  

---

##  Speed Estimation Method

1. Track vehicle center movement across frames  
2. Compute Euclidean pixel distance  
3. Apply perspective compensation  
4. Convert pixel → meter using calibration constant  
5. Speed = Distance / Time  
6. Apply exponential smoothing to reduce noise  
7. Filter unrealistic speed spikes  

---

##  Intelligent Jam Detection Logic

A traffic jam is confirmed only when:

- Majority of vehicles are moving below a defined speed threshold  
- Minimum number of slow vehicles is present  
- Condition persists for a defined time duration  

This prevents false detection during:
- Temporary slowdowns  
- Traffic signal stops  
- High-density but smooth traffic  

---

##  Accident Detection & SOS Alert (Future Enhancement)

Future versions will include an Accident Detection Module designed to identify high-risk collision scenarios.

Proposed Detection Criteria:
- Sudden speed drop  
- Vehicle immobilization in active lane  
- Congestion forming behind stopped vehicle  
- Bounding box overlap between vehicles  

Planned integration includes:
- SMS alerts (Twilio API)  
- Email notifications  
- API-based alerts to traffic authorities  
- Location + timestamp reporting  

Currently part of roadmap — not yet implemented.

---

##  Planned Behaviour-Based Enhancements

Wrong Turn Detection  
- Illegal turn identification  
- Trajectory angle analysis  

Rash Driving Detection  
- Zig-zag motion patterns  
- Aggressive acceleration/deceleration  
- Abnormal lane switching detection  

Pedestrian-Aware Congestion Analysis  
- Integrate pedestrian density detection  
- Differentiate between vehicle-induced jams and pedestrian-induced slowdowns  
- Reduce false congestion alerts in mixed traffic environments  

---

##  Current Limitations

- Pixel-to-meter calibration is approximate (manual calibration)  
- Wrong-side detection depends on camera orientation  
- No explicit collision classification model yet  
- Jam detection is speed-based and may misclassify pedestrian-heavy areas  
- Performance depends on lighting and camera positioning  
- Wrong turn & rash driving detection not yet implemented  

---

##  Technologies Used

- Python 3.11  
- YOLOv8 (Ultralytics)  
- PyTorch + CUDA 12.1  
- OpenCV  
- NumPy  
- Flask  
- yt-dlp  
- NVIDIA RTX 3050 GPU  

---

##  Project Structure

Vehicle-Behavior-Analysis/  
├── modules/  
│   ├── detector.py  
│   ├── tracker.py  
│   ├── speed_estimator.py  
│   ├── jam_detector.py  
│   ├── vehicle_counter.py  
│   ├── wrong_side_detector.py  
├── config.py  
├── main.py  
├── requirements.txt  
├── dashboard/  
├── database/  

---

##  How to Run

1. Clone Repository  
git clone https://github.com/AryanRajguru22/Vehicle-Behavior-Analysis.git  
cd Vehicle-Behavior-Analysis  

2. Install Dependencies  
pip install -r requirements.txt  

3. Configure Video Source  
Edit config.py  

4. Run Application  
python main.py  

---

##  Performance (GPU Mode)

- FPS: ~28–35  
- GPU Usage: ~40–50%  
- CPU Usage: ~20–30%  
- Stable real-time processing  

---

##  Industry Roadmap

Phase 1 – Behaviour-Based Monitoring (Completed)  
Phase 2 – Multi-lane Analysis  
Phase 3 – Violation Intelligence (Wrong Turn & Rash Driving)  
Phase 4 – Accident Detection & Emergency Alerts  
Phase 5 – Smart City Deployment  

---

##  Author

Aryan Rajguru  
School of Computer Science & Engineering  

---

##  Project Vision

To evolve into a Smart City–ready Intelligent Traffic Management System capable of automated enforcement, emergency response, and data-driven traffic optimization.
