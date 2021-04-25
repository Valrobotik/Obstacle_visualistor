if __name__ == "__main__":
    # Pour executer le code en local et avoir les bon import
    import sys
    import os
    sys.path.append(os.getcwd() + "\\src")

from sensor_board.CommunicationGcode import CommunicationGcode
import numpy as np

class CarteDetecteurObstacle(CommunicationGcode):
    """Api for using the robot.

    Args:
        Communication_Gcode inherite from serial class
    """

    def __init__(self, portserial, bauderate) -> None:
        CommunicationGcode.__init__(self, portserial, bauderate)


    def get_distance(self, capteur):
        """Fonction qui met à jour la position actuelle du robot dans la classe.
        """
        if (self.serial.is_open):
            self.serial.write(b'S')
            self.serial.write(str(capteur).encode())
            self.serial.write(b'\n')

            message = self.decode_serial(separator="; ")
            # print(message)

            if message[0] != '':
                if capteur == "A":
                    return np.array(message, dtype=float)
                else:
                    return float(message[0])

            return -1


if __name__ == "__main__":
    import time

    carte = CarteDetecteurObstacle("COM8", 9600)

    while True:
        # print(carte.get_distance(0))
        A = carte.get_distance("A")
        print(A)
        # time.sleep(0.2)
