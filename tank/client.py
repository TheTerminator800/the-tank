# PC IS THE CLIENT

import socket
import serial
import keyboard
import time

port = "COM7"
baudrate = 9600

UDP_IP = '192.168.1.7'
UDP_PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with serial.Serial(port=port, baudrate=baudrate, timeout=1) as port_serie:
    if port_serie.isOpen():
        port_serie.flush()
        while True:
            if keyboard.is_pressed('q'):
                break
            try:
                fire = False
                ligne = port_serie.readline()
                if 'FIRE' in str(ligne):
                    fire = True
                elif 'HOLD' in str(ligne):
                    fire = False
                op = str(ligne).replace('FIRE', '').replace('HOLD', '').split(',')
                left = 'L' + op[0].split("'")[1]
                right = 'R' + op[1].split("\\")[0].strip()

                # with open('output.txt', 'a') as opf:
                #     #opf.write(f"{left},{right},{fire}\n")
                #     pass
                #print(f"Left: {left}, Right: {right}, Fire?: {fire}")

                s.sendto(bytes(fire), (UDP_IP, UDP_PORT))
                print(fire)
                s.sendto(left.encode('utf-8'), (UDP_IP, UDP_PORT))
                print(left)
                s.sendto(right.encode('utf-8'), (UDP_IP, UDP_PORT))
                print(right)

            except:
                # with open('output.txt', 'a') as opf:
                #    # opf.write("0,0\n")
                pass
                # #print("OFF")
        port_serie.close()

    