import serial
import time

arduino = serial.Serial('com3', 9600)

while True:
    var = input("write 1 ")

    var = var.encode('utf-8')
    arduino.write(var)
    time.sleep(1)
                        

