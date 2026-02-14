# ===============================
# SOURCE CONFIG
# ===============================

SOURCE_TYPE = "video"   # video | youtube | rtsp | webcam

VIDEO_PATH = "Dhurandhar.mp4"
YOUTUBE_URL = "https://www.youtube.com/watch?v=8JCk5M_xrBs"
RTSP_URL = "rtsp://username:password@ip:port/stream"
WEBCAM_INDEX = 0

# ===============================
# MODEL CONFIG
# ===============================

MODEL_PATH = "yolov8n.pt"
CONFIDENCE = 0.35
IMG_SIZE = 512

vehicle_classes = [0,2, 3, 5, 7]   # car, motorcycle, bus, truck

# ===============================
# GPU CONFIG
# ===============================

USE_GPU = True  # Set False if debugging CPU

# ===============================
# SPEED CONFIG
# ===============================

SPEED_LIMIT = 60
PIXEL_TO_METER = 0.009      # Adjust carefully (real-world calibration needed)
MIN_PIXEL_MOVEMENT = 5     # Ignore jitter
MAX_REASONABLE_SPEED = 150
SPEED_SMOOTHING = 0.7      # 0.7 previous + 0.3 new

# ===============================
# JAM CONFIG
# ===============================

JAM_SPEED_THRESHOLD = 10       # Vehicles considered slow below this
JAM_VEHICLE_COUNT = 5          # Minimum slow vehicles
JAM_TIME_THRESHOLD = 5         # Seconds of continuous slow traffic

# ===============================
# WRONG SIDE CONFIG
# ===============================

ENABLE_WRONG_SIDE = True
ALLOWED_DIRECTION = "RIGHT"   # RIGHT or LEFT
WRONG_SIDE_THRESHOLD = 5      # minimum pixel movement to consider

# ===============================
# DISPLAY
# ===============================

FRAME_SKIP = 3
DISPLAY_WIDTH = 960
DISPLAY_HEIGHT = 540
