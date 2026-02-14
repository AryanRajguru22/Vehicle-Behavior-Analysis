import cv2
import yt_dlp
from config import *
from modules.detector import Detector
from modules.tracker import TrackerMemory
from modules.speed_estimator import SpeedEstimator
from modules.jam_detector import JamDetector
from modules.vehicle_counter import VehicleCounter


# ============================================================
# YOUTUBE STREAM
# ============================================================
def get_youtube_stream(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio/best[ext=mp4]/best',
        'quiet': True,
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        if "url" in info:
            return info["url"]

        # If live stream
        if "formats" in info:
            for f in info["formats"]:
                if f.get("ext") == "mp4" and f.get("vcodec") != "none":
                    return f["url"]

        raise Exception("Could not extract stream URL")



# ============================================================
# VIDEO SOURCE
# ============================================================

def get_video_source():
    if SOURCE_TYPE == "video":
        return cv2.VideoCapture(VIDEO_PATH)

    elif SOURCE_TYPE == "youtube":
        print("Opening YouTube Live Stream...")
        stream_url = get_youtube_stream(YOUTUBE_URL)
        cap = cv2.VideoCapture(stream_url)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        return cap

    elif SOURCE_TYPE == "rtsp":
        return cv2.VideoCapture(RTSP_URL)

    elif SOURCE_TYPE == "webcam":
        return cv2.VideoCapture(WEBCAM_INDEX)


cap = get_video_source()

if not cap.isOpened():
    print("Error opening source")
    exit()


# ============================================================
# INITIALIZE MODULES
# ============================================================

detector = Detector()
tracker = TrackerMemory()
speed_estimator = SpeedEstimator()
jam_detector = JamDetector()
counter = VehicleCounter()


cv2.namedWindow("Traffic AI", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Traffic AI", DISPLAY_WIDTH, DISPLAY_HEIGHT)

frame_count = 0


# ============================================================
# MAIN LOOP
# ============================================================

while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    if frame_count % FRAME_SKIP != 0:
        continue

    frame = cv2.resize(frame, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
    frame_height = frame.shape[0]

    results = detector.detect(frame)

    slow_count = 0
    total_vehicles = 0

    counter.reset()

    if results and results[0].boxes is not None:

        for box in results[0].boxes:

            if box.id is None:
                continue

            cls = int(box.cls[0])
            if cls not in vehicle_classes:
                continue

            is_person = (cls == 0)


            track_id = int(box.id[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            # Add to counter with lane classification
            counter.add(track_id, center_y, frame_height)
            total_vehicles += 1

            # ================= SPEED =================
            if not is_person:
                speed = speed_estimator.calculate(track_id, center_x, center_y, tracker)
                speed = tracker.smooth_speed(track_id, speed)
            else:
                speed = 0
            if speed < JAM_SPEED_THRESHOLD:
                slow_count += 1

            # ================= COLOR LOGIC =================
            color = (0, 255, 0)
            if speed > SPEED_LIMIT:
                color = (0, 0, 255)

            # ================= DRAW =================
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            cv2.putText(
                frame,
                f"{int(speed)} km/h",
                (x1, y1 - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

    # ================= JAM DETECTION =================
    if jam_detector.check(total_vehicles, slow_count):
        cv2.putText(
            frame,
            "TRAFFIC JAM DETECTED",
            (50, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

    # ================= DISPLAY INFO =================
    lane_counts = counter.lane_count()

    cv2.putText(
        frame,
        f"Vehicles In Frame: {counter.count()}",
        (50, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Top Lane: {lane_counts['top']}  Bottom Lane: {lane_counts['bottom']}",
        (50, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 200, 0),
        2
    )

    cv2.imshow("Traffic AI", frame)

    # Cleanup old tracking IDs (important for long CCTV use)
    tracker.cleanup()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
