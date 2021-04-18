# coding: utf-8
# @author S6ril & Starfunx



from Class_Serial import Communication_Gcode



class Robot(Communication_Gcode):
    """Api for using the robot.

    Args:
        Communication_Gcode inherite from serial class
    """
    def __init__(self, portserial, bauderate) -> None:
        Communication_Gcode.__init__(self, portserial, bauderate)
        self.r


   

    def get_pose(self):
        """Fonction qui met à jour la position actuelle du robot dans la classe.

        Returns:
            Pose2D: Position actuelle du robot.
        """
        if (self.serial.is_open):
            self.serial.write(b'M114\n')  # Demande la position au robot

            message = self.decode_serial()
            # print(message)
            # Répartition des valeurs dans la variable position.
            if (len(message) >= 6):
                self.robotPose.x = float(message[1])
                self.robotPose.y = float(message[3])
                self.robotPose.theta = float(message[5])
            

        return self.robotPose

   



if __name__ == "__main__":
    import time
    
    robot = Robot("COM9", 112500)



    while 1:
        print("-------------------------")
        A = robot.get_pose()
        P = [A.x, A.y, A.theta]
        print(P, time.strftime("%H:%M:%S", time.gmtime()))

        input()
