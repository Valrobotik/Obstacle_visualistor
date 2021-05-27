import sys
import glob
import serial


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def user_select_port_loop():
    """Boucle d'attente de l'utilisateur pour obtenir le port de la carte arduino

    Returns:
        str: Port de la carte
    """
    ports = serial_ports()
    r = [str(_) for _ in range(len(ports))]
    port_user = None

    while(port_user not in r):

        print("--------------")
        for nb, port in zip(r, ports):
            print(nb, ".", port)

        print("--------------")
        print("A . Actualiser")
        print("S . Simulation")
        print("E . Exit")
        print("--------------")
        
        port_user = input("Entrer le port désiré : ")
        if (port_user == "E"):
            sys.exit()
        
        if (port_user == "S"):
            return ""
        
        if (port_user == "A"):
            ports = serial_ports()
            r = [str(_) for _ in range(len(ports))]

    return ports[int(port_user)]



if __name__ == '__main__':
    print(user_select_port_loop())
