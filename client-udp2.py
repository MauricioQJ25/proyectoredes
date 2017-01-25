#!/usr/bin/env python
'''
    udp socket client
    Silver Moon
'''
#create a sensor interface
from mpu6050 import mpu6050
from time import sleep
sensor = mpu6050(0x68)
 
import socket   #for sockets
import sys  #for exit
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = 'localhost';
port = 8888;
 
while(1) :
    accel_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()
    temp = sensor.get_temp()

    print("Accelerometer data")
    print("x: " + str(accel_data['x']))
    a = "x: " + str(accel_data['x'])
    print("y: " + str(accel_data['y']))
    b = "y: " + str(accel_data['y'])
    print("z: " + str(accel_data['z']))
    c = "z: " + str(accel_data['z'])

    print("Gyroscope data")
    print("x: " + str(gyro_data['x']))
    d = "x: " + str(gyro_data['x'])
    print("y: " + str(gyro_data['y']))
    e = "y: " + str(gyro_data['y'])
    print("z: " + str(gyro_data['z']))
    f = "z: " + str(gyro_data['z'])

    print("Temp: " + str(temp) + " C")
    t = "Temperatura data: " + str(temp) + " C"
    n = "\n"
    msg = n + "Acelerometro data:" + n + a + n + b + n + c +n+"Giroscopio data:"+ n + d + n + e + n + f + n + t + n 
 
    #msg = raw_input('Enter message to send : ')
     
    try :
        #Set the whole string
        s.sendto(msg, (host, port))
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print 'Server reply : ' + reply
     
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    sleep(1) #tiempo de 1 segundo
