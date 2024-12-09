import random
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Plane:
    def __init__(self, direction, rate_of_correction = 1.0):
        self.current_orientation = 0.0
        self.environment = Environment(direction, rate_of_correction)
        self.action = Action(rate_of_correction)
        self.tilt_angle = 0
        self.tilt_correction = 0

    def fly(self):
        try:
            while True:
                self.simulate_correction()
                yield self.display_plane_info()
                time.sleep(0.5)
        except KeyboardInterrupt:
            logging.info(f'Simulation interupted')

    def simulate_correction(self):
        self.current_orientation += self.environment.simulate_turbulance()
        self.correct_tilt()
        self.correct_orientation()

    def correct_tilt(self):
        if self.current_orientation < 0:
            self.correct_left_tilt()
        elif self.current_orientation > 0:
            self.correct_right_tilt()
        else:
            pass
    
    def correct_left_tilt(self):
        self.tilt_correction = self.action.left_tilt_correction(self.current_orientation)
        logging.debug(f"Applying left tilt correction. Turning right.")
    
    def correct_right_tilt(self):
        self.tilt_correction = self.action.right_tilt_correction(self.current_orientation)
        logging.debug(f"Applying right tilt correction. Turning left.")

    def correct_orientation(self):
        self.current_orientation += self.tilt_correction

    def display_plane_info(self):
        return f"Current orientation:{self.current_orientation:5.2f}°, applied tilt correction: {self.tilt_correction:5.2f}°\n"

class Environment:
    def __init__(self, direction, rate_of_correction):
        self.rate_of_correction = rate_of_correction
        self.direction = direction

    def simulate_turbulance(self):
        self.angle = random.gauss(0, 2 * self.rate_of_correction)
        logging.info(f"The plane to {self.direction} experiencing turbulences {self.angle:.2f}°.")
        return self.angle

class Action:
    def __init__(self, rate_of_correction):
        self.rate_of_correction = rate_of_correction
    
    def right_tilt_correction(self, tilt_angle):
        if tilt_angle > self.rate_of_correction:
            return -self.rate_of_correction
        else:
            return -tilt_angle
    
    def left_tilt_correction(self, tilt_angle): 
        if tilt_angle < -self.rate_of_correction:
            return self.rate_of_correction
        else:
            return -tilt_angle

def simulate_flight(plane):
    for step in plane.fly():
            print(step)

if __name__ == "__main__":
    plane = Plane("Berlin", 1.5)
    simulate_flight(plane)