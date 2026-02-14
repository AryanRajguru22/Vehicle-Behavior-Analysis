class WrongSideDetector:

    def __init__(self, allowed_direction="RIGHT"):
        self.allowed_direction = allowed_direction

    def check(self, track_id, prev_x, current_x):

        movement = current_x - prev_x

        if abs(movement) < 5:
            return False

        # If allowed direction is RIGHT, movement should be positive
        if self.allowed_direction == "RIGHT" and movement < 0:
            return True

        # If allowed direction is LEFT, movement should be negative
        if self.allowed_direction == "LEFT" and movement > 0:
            return True

        return False
