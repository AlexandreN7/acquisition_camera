#!/usr/bin/python2
 # -*- coding: latin-1 -*-

import serial
import time
import io
from pylab import *
import matplotlib.pyplot as plt
#pacman -S python-matplotlib

ser=serial.Serial(
port='/dev/ttyUSB0',
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
    #print('debug')
    try :
        if y=='S':
            x = ser.read()
            y = x.decode(encoding='UTF-8')
            if y=='1':
                pixel =[]
                while y!='E':
                    x=ser.read()
                    y=x.decode(encoding='UTF-8')
                    pixel.append(y)
                print('une trame traitée !')
                datas = ''.join(pixel).split(',')
                datas.pop()
                values1=list(map(int,datas))

                plt.grid(True)
                plt.clf()
            plt.subplot(2,1,1)
            plt.plot(values1)
            plt.title('Camera 1')
                #plt.ylim(0,20000)

            if y=='2':
                pixel =[]
                while y!='E':
                    x=ser.read()
                    y=x.decode(encoding='UTF-8')
                    pixel.append(y)
                print('une trame traitée !')
                datas = ''.join(pixel).split(',')
                datas.pop()
                values2=list(map(int,datas))

                plt.grid(True)
                plt.clf()
            plt.subplot(2,1,2)
            plt.plot(values2)
            plt.title('Camera 2')
                #plt.ylim(0,20000)

        plt.show(block=False)
        plt.pause(0.0001)
    except Exception :
        print("fail")

