

from Class_Serial import Communication_Gcode


class Carte_detecteur_obstacle(Communication_Gcode):
    """Api for using the robot.

    Args:
        Communication_Gcode inherite from serial class
    """

    def __init__(self, portserial, bauderate) -> None:
        Communication_Gcode.__init__(self, portserial, bauderate)
        self.distance_capteur = [0]*8

    def get_distance(self, capteur):
        """Fonction qui met à jour la position actuelle du robot dans la classe.

        Returns:
            Pose2D: Position actuelle du robot.
        """
        if (self.serial.is_open):
            self.serial.write(b'S')
            self.serial.write(str(capteur).encode())
            self.serial.write(b'\n')

            message = self.decode_serial()
            # print(message)

            if message[0] != '':
                if capteur == "A":
                    #TODO
                    pass
                else:
                    distance = float(message[0])
                    self.distance_capteur[capteur] = distance
                
                    return distance
            
            return 0


if __name__ == "__main__":
    import time

    carte = Carte_detecteur_obstacle("COM7", 9600)

    while True:
        print(carte.get_distance(0))

        time.sleep(0.2)
