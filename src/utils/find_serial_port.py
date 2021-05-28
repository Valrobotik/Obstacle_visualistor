import sys
import glob
import serial
import serial.tools.list_ports


def user_select_port_loop():
    """Boucle d'attente de l'utilisateur pour obtenir le port de la carte arduino

    Returns:
        str: Port de la carte
    """
    liste_ports = serial.tools.list_ports.comports()
    ports = [port[0] for port in sorted(liste_ports)]
    r = [str(i) for i in range(len(ports))]
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
            liste_ports = serial.tools.list_ports.comports()
            ports = [port[0] for port in sorted(liste_ports)]
            r = [str(i) for i in range(len(ports))]

    return ports[int(port_user)]



if __name__ == '__main__':
    port = user_select_port_loop()
    print(port)
    print(type(port))
