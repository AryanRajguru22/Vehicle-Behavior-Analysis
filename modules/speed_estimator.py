import math
from config import *

class SpeedEstimator:

    def __init__(self):
        self.frame_times = {}
        self.prev_positions = {}

    def calculate(self, track_id, center_x, center_y, tracker):

        current_time = tracker.get_previous(track_id)

        # If first time seeing this ID
        if current_time is None:
            tracker.update_position(track_id, center_x, center_y, 0)
            return 0

        prev_x, prev_y, prev_time = current_time

        # Use frame-based delta instead of real-time clock
        # This avoids speed spikes
        frame_time = 1 / 30  # assume 30 FPS baseline

        pixel_distance = math.sqrt(
            (center_x - prev_x) ** 2 +
            (center_y - prev_y) ** 2
        )

        # Ignore tiny movement (jitter)
        if pixel_distance < MIN_PIXEL_MOVEMENT:
            tracker.update_position(track_id, center_x, center_y, 0)
            return 0

        # Perspective compensation:
        # Objects higher in frame move slower in pixels
        perspective_scale = 1 + (center_y / DISPLAY_HEIGHT)

        adjusted_distance = pixel_distance * perspective_scale

        distance_m = adjusted_distance * PIXEL_TO_METER
        speed_mps = distance_m / frame_time
        speed_kmh = speed_mps * 3.6

        # Prevent unrealistic spikes
        if speed_kmh > MAX_REASONABLE_SPEED:
            speed_kmh = 0

        tracker.update_position(track_id, center_x, center_y, 0)

        return speed_kmh
