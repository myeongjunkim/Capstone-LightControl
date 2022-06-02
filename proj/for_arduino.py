import serial
import time

arduino = serial.Serial('com3', 9600)

while True:
    var = input("theta,radius : ")
    var = var.encode('utf-8')
    arduino.write(var)
    time.sleep(1)

    if var == "end":
        break
                        

