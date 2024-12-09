## Flight Simulator: Tilt Correction
This project simulates the tilt correction of an airplane's roll angle (the angle between the airplane's wings and the ground). The goal is to model how an airplane reacts to turbulence and stabilizes its orientation.

#### Task Desciption
The program continuously simulates random turbulence that affects the airplane's roll angle. After each turbulence event, a correction is calculated and applied to stabilize the plane. The simulation runs in an infinite loop and outputs the current roll angle along with the applied correction. The loop continues until the user manually stops it.

#### Task requirements
- The roll angle changes randomly at each step, following a Gaussian distribution:
random.gauss(0, 2 * rate_of_correction)
- The program calculates and applies tilt corrections after each turbulence event.
- The program prints the current roll angle and the correction applied after each step.
- The simulation runs in infinite loop until the user interrupts it.

  
