import time
from config import SPEED_SMOOTHING

class TrackerMemory:

    def __init__(self):
        self.prev_positions = {}
        self.speed_memory = {}
        self.last_seen = {}

        # Remove IDs not seen for this many seconds
        self.cleanup_threshold = 5  

    # ==========================================
    # POSITION TRACKING
    # ==========================================
    def update_position(self, track_id, x, y, timestamp):
        self.prev_positions[track_id] = (x, y, timestamp)
        self.last_seen[track_id] = time.time()

    def get_previous(self, track_id):
        return self.prev_positions.get(track_id, None)

    # ==========================================
    # SPEED SMOOTHING
    # ==========================================
    def smooth_speed(self, track_id, new_speed):

        if track_id not in self.speed_memory:
            self.speed_memory[track_id] = new_speed
        else:
            self.speed_memory[track_id] = (
                SPEED_SMOOTHING * self.speed_memory[track_id] +
                (1 - SPEED_SMOOTHING) * new_speed
            )

        return self.speed_memory[track_id]

    # ==========================================
    # CLEANUP OLD IDS
    # ==========================================
    def cleanup(self):
        current_time = time.time()

        to_remove = []

        for track_id, last_time in self.last_seen.items():
            if current_time - last_time > self.cleanup_threshold:
                to_remove.append(track_id)

        for track_id in to_remove:
            self.prev_positions.pop(track_id, None)
            self.speed_memory.pop(track_id, None)
            self.last_seen.pop(track_id, None)
