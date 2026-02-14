import time
from config import *

class JamDetector:

    def __init__(self):
        self.jam_start_time = None

    def check(self, total_vehicles, slow_count):

        # Not enough vehicles → no jam
        if total_vehicles < 3:
            self.jam_start_time = None
            return False

        # Calculate slow ratio
        slow_ratio = slow_count / total_vehicles

        # Jam only if majority vehicles are slow
        if slow_ratio >= 0.6 and slow_count >= JAM_VEHICLE_COUNT:

            if self.jam_start_time is None:
                self.jam_start_time = time.time()

            elif time.time() - self.jam_start_time >= JAM_TIME_THRESHOLD:
                return True

        else:
            self.jam_start_time = None

        return False
