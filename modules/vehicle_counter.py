class VehicleCounter:

    def __init__(self):
        self.current_ids = set()
        self.lane_counts = {"top": set(), "bottom": set()}

    # ==========================================
    # RESET PER FRAME
    # ==========================================
    def reset(self):
        self.current_ids.clear()
        self.lane_counts["top"].clear()
        self.lane_counts["bottom"].clear()

    # ==========================================
    # ADD VEHICLE
    # ==========================================
    def add(self, track_id, center_y=None, frame_height=None):

        self.current_ids.add(track_id)

        # Optional lane classification
        if center_y is not None and frame_height is not None:
            lane_divider = frame_height // 2

            if center_y < lane_divider:
                self.lane_counts["top"].add(track_id)
            else:
                self.lane_counts["bottom"].add(track_id)

    # ==========================================
    # TOTAL COUNT
    # ==========================================
    def count(self):
        return len(self.current_ids)

    # ==========================================
    # LANE-WISE COUNT
    # ==========================================
    def lane_count(self):
        return {
            "top": len(self.lane_counts["top"]),
            "bottom": len(self.lane_counts["bottom"])
        }
