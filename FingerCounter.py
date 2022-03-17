from __future__ import division
import cv2
import time
import os

import time
#from picamera import  Color
import socket
import time
PORT=8888
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address=('10.2.47.167',PORT)
server_socket.bind(address)
server_socket.settimeout(10)



#import demjson

import cv2
import base64
import pprint
#import Adafruit_PCA9685
import socket

#import RPi.GPIO as GPIO

IN1 = 5
IN2 = 6
IN3 = 19
IN4 = 20
mode = 1
locationX = 320
locationY = 240
locationx = 320
locationy = 240
pTime = 0
tipIds = [4, 8, 12, 16, 20]
flag=0
i=0
def timeplus():
    i=i+1
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(IN1,GPIO.OUT)
# GPIO.setup(IN2,GPIO,OUT)
# GPIO.setup(IN3,GPIO.OUT)
# GPIO.setup(IN4,GPIO.OUT)
# PWMIN1=GPIO.PWM(IN1,500)
# PWMIN2=GPIO.PWM(IN2,500)
# PWMIN3=GPIO.PWM(IN3,500)
# PWMIN4=PGIO.PWM(IN4,500)
# GPIO.output(IN1,GPIO.LOW)
# GPIO.output(IN2,GPIO.LOW)
# GPIO.output(IN3,GPIO.LOW)
# GPIO.output(IN4,GPIO.LOW)
# def run():
#     GPIO.output(IN1,GPIO.HIGH)
#     GPIO.output(IN2,GPIO.LOW)
#     GPIO.output(IN3,GPIO.HIGH)
#     GPIO.output(IN4,GPIO.LOW)
#     time.sleep(0.3)
#     GPIO.output(IN1,GPIO.LOW)
#     GPIO.output(IN2,GPIO.LOW)
#     GPIO.output(IN3,GPIO.LOW)
#     GPIO.output(IN4,GPIO.LOW)
# def left():
#     GPIO.output(IN1,GPIO.LOW)
#     GPIO.output(IN2,GPIO.HIGH)
#     GPIO.output(IN3,GPIO.HIGH)
#     GPIO.output(IN4,GPIO.LOW)
#     time.sleep(0.3)
#     GPIO.output(IN1,GPIO.LOW)
#     GPIO.output(IN2,GPIO.LOW)
#     GPIO.output(IN3,GPIO.LOW)
#     GPIO.output(IN4,GPIO.LOW)
# def right():
#     GPIO.output(IN1,GPIO.HIGH)
#     GPIO.output(IN2,GPIO.LOW)
#     GPIO.output(IN3,GPIO.LOW)
#     GPIO.output(IN4,GPIO.HIGH)
#     time.sleep(0.3)
#     GPIO.output(IN1,GPIO.LOW)
#     GPIO.output(IN2,GPIO.LOW)
#     GPIO.output(IN3,GPIO.LOW)
#     GPIO.output(IN4,GPIO.LOW)
# def stop():
#     GPIO.output(IN1,GPIO.LOW)
#     GPIO.output(IN2,GPIO.LOW)
#     GPIO.output(IN3,GPIO.LOW)
#     GPIO.output(IN4,GPIO.LOW)
#     time.sleep(0.3)
#     GPIO.output(IN1,GPIO.LOW)
#     GPIO.output(IN2,GPIO.LOW)
#     GPIO.output(IN3,GPIO.LOW)
#     GPIO.output(IN4,GPIO.LOW)
# def back():
#     GPIO.output(IN1,GPIO.LOW)
#     GPIO.output(IN2,GPIO.HIGH)
#     GPIO.output(IN3,GPIO.LOW)
#     GPIO.output(IN4,GPIO.HIGH)
#     time.sleep(0.3)
#     GPIO.output(IN1,GPIO.LOW)
#     GPIO.output(IN2,GPIO.LOW)
#     GPIO.output(IN3,GPIO.LOW)
#     GPIO.output(IN4,GPIO.LOW)
# def pwmrun():
#     GPIO.output(IN4, GPIO.LOW)
#     PWMIN3.ChangeDutyCycle((locationY - locationy) / 4.8)
#     time.sleep(0.6)
#     PWMIN3.ChangeDutyCycle(0)
# def pwmleft():
#     PWMIN1.ChangeDutyCycle((locationX - locationx) / 6.4)
#     GPIO.output(IN2, GPIO.LOW)
#     time.sleep(0.6)
#     PWMIN1.ChangeDutyCycle(0)
# def pwmright():
#     PWMIN2.ChangeDutyCycle((locationx - locationX) / 6.4)
#     GPIO.output(IN1, GPIO.LOW)
#     time.sleep(0.6)
#     PWMIN2.ChangeDutyCycle(0)
# def pwmback():
#     GPIO.output(IN3, GPIO.LOW)
#     PWMIN4.ChangeDutyCycle((locationy - locationY) / 4.8)
#     time.sleep(0.6)
#     PWMIN4.ChangeDutyCycle((locationy - locationY) / 4.8)
print("Please choose your mode")
print("Mode 1 figure control")
print("Mode 2 location control")
print("Mode 3 remote control")
while True:
    try:
        now = time.time()
        receive_data, client = server_socket.recvfrom(1024)
        # print(receive_data.decode())
        t = receive_data.decode()
        # print(t)
        if (t == '0'):
            print("stop")
        if (t == '1'):
            print("run")
        if (t == '2'):
            print("back")
        if (t == '3'):
            print("left")
        if (t == '4'):
            print("right")
    except socket.timeout:
        print("time out")
    if i%20==0:
        if len(lmList) != 0:
            fingers = []
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            totalFingers = fingers.count(1)
            #print(lmList)
            #print(totalFingers)
            if mode==1:
                if totalFingers==2:
                    print("back")
                    #back()
                elif totalFingers==1:
                    print("run")
                    #run()
                elif totalFingers==3:
                    print("left")
                    #left()
                elif totalFingers==4:
                    print("right")
                    #right()
                elif totalFingers==5:
                    print("choose mode")
                    mode = 5
                else:
                    print("stop")
                    #stop()
            if mode==2:
                if(i%50==0):
                    locationx = lmList[9][1]
                    locationy = lmList[9][2]
                    if (locationX - locationx >= 0):
                        # pwmleft()
                        print((locationX - locationx) / 6.4,"----------------x")
                    elif (locationX - locationx < 0):
                        # pwmright()
                        print((locationx - locationX) / 6.4,"----------------x")
                    if (locationY - locationy >= 0):
                        # pwmrun()

                        print((locationY - locationy) / 6.4,"-------------------y")
                    elif (locationY - locationy < 0):
                        print((locationy - locationY) / 6.4,"-------------------y")
                if totalFingers==5:
                    print("choose mode")
                    mode = 5
            if mode==3:
                if(i%50==0):
                    flag = input("derction:")
                    if flag == "w":
                        # run()
                        pass
                    elif flag == "a":
                        pass
                        # left()
                    elif flag == "d":
                        pass
                        # right()
                    elif flag == "s":
                        pass
                        # back()
                    else:
                        pass
                        # stop()
                if totalFingers == 5:
                    print("choose mode")
                    mode = 5
            if mode == 5:
                if totalFingers==1:
                    time.sleep(0.5)
                    if totalFingers==1:
                        mode = 1
                elif totalFingers ==2:
                    time.sleep(0.5)
                    if totalFingers == 2:
                        mode=2
                elif totalFingers ==3:
                    time.sleep(0.5)
                    if totalFingers == 3:
                        mode=3
