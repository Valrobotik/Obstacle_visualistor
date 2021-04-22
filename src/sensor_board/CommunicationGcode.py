# coding: utf-8
# @author S6ril & Starfunx

"""
Cette classe permet de gérer la communication Gcode entre un robot et un ordinateur.
Pour trouver le port :

- Avec l'arduino débranchée
ls /dev/tty*

- Avec l'arduino branchée
ls /dev/tty*

- On recherche le nouveau port connecté ;)
"""
import serial


class CommunicationGcode(object):
    """
    Classe communication sur le port serial.
    """

    def __init__(self, portserial, bauderate):
        """Initialisation des variables internes de la classe.

        Args:
            portserial (char): Port USB de l'arduino
            bauderate (float): bauderate de la carte
        """
        super(CommunicationGcode, self).__init__()
        self.serial = serial.Serial()
        self.serial.port = portserial
        self.serial.baudrate = bauderate
        self.serial.timeout = 0
        self.serial.open()

    def __del__(self):
        """
        Destructeur de la classe.
        Permet de fermer le port Serial.
        """
        self.serial.close()
        print("Serial close")

    def cleanSerial(self):
        """
        Nettoyage du buffer pour éviter une saturation.
        On appelle cette fonction après chaques commandes Gcode executées.
        """
        self.serial.flushInput()
        self.serial.flushOutput()
    
    
    def decode_serial(self):
        """
        Fonction pour lire, décoder, et mettre les données de la sérial dans une liste
        """
        message = self.serial.readline()  # Lecture du port serial

        message = message.decode()  # Conversion bytes en str
        message = message.rstrip()  # Enlève \n
        message = message.split(" ")  # Conversion str en list

        return message