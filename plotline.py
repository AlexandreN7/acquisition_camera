#!/usr/bin/python2
 # -*- coding: latin-1 -*-

import serial
import time
import io
from pylab import *
import matplotlib.pyplot as plt
#pacman -S python-matplotlib

ser=serial.Serial(
port='/dev/ttyACM0',
baudrate=115200,
)

plt.ion()



abscisse =[]
for i in range(0,128) :
    abscisse.append(i)

plt.figure(1)
ser.isOpen()
while 1 :
    x = ser.read()
    y = x.decode(encoding='UTF-8')
    print('debug')
    if y=='S':
        pixel =[]
        while y!='E':
            x=ser.read()
            y=x.decode(encoding='UTF-8')
            pixel.append(y)
        print('une trame traitée !')
        datas = ''.join(pixel).split(',')
        datas.pop()
        values=list(map(int,datas))

        plt.grid(True)
        plt.clf()

        plt.plot(values)
        plt.ylim(0,20000)
        plt.show(block=False)
        plt.pause(0.0001)

        #time.sleep(0.05)
        #input("entrer")
        #time.sleep(1)
