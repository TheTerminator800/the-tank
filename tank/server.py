# RASPBERRY PI IS THE SERVER
import time
import socket
from gpiozero import Servo, LED

UDP_IP = '0.0.0.0'
UDP_PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))

motorA = Servo(17) #left
motorB = Servo(27) #left
motorC = Servo(23) #right
motorD = Servo(24) #right
laser = LED(25)

while True:
    data, addr = s.recvfrom(500)
    
    motion_str = ''
    try:
        if data==bytes(True):
            motion_str += '1'
            laser.on()
        elif data==bytes(False):
            motion_str += '0'
            laser.off()

        elif data.decode('utf-8').startswith('L'):
            left = int(data.decode('utf-8').strip('L'))
            if left >= 510:
                motion_str += 'L1'
                motorA.mid()
                motorA.max()
                motorB.mid()
                motorB.max()
            elif 0 <= left <= 410:
                motion_str += 'L-1'
                motorA.mid()
                motorA.max()
                motorB.mid()
                motorB.max()
            else:
                motion_str += 'L0'
                motorA.mid()
                motorB.mid()

        elif data.decode('utf-8').startswith('R'):
            right = int(data.decode('utf-8').strip('R'))
            if right >= 830:
                motion_str += 'R1'
                motorC.mid()
                motorC.value = 0.9
                motorD.mid()
                motorD.value = 0.9
            elif 0 <= right <= 715:
                motion_str += 'R-1\n'
                motorC.mid()
                motorC.value = -0.9
                motorD.mid()
                motorD.value = -0.9
            else:
                motion_str += 'R0\n'
                motorC.mid()
                motorD.mid()
        
        print(motion_str)

    except:
        pass