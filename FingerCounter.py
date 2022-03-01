import cv2
import time
import os
import HandTrackingModule as htm
from __future__ import division
from picamera import  Color
import time
import demjson
from pygame import mixer
import cv2
import base64
import pprint
import Adafruit_PCA9685
import socket
import RPi.GPIO as GPIO
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
IN1 = 5
IN2 = 6
IN3 = 19
IN4 = 20
mode = 1
locationX = 320
locationY = 240
locationx = 320
locationy = 240
address=('10.68.6.13',8843)
pTime = 0
detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]
flag=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO,OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
PWMIN1=GPIO.PWM(IN1,500)
PWMIN2=GPIO.PWM(IN2,500)
PWMIN3=GPIO.PWM(IN3,500)
PWMIN4=PGIO.PWM(IN4,500)
GPIO.output(IN1,GPIO.LOW)
GPIO.output(IN2,GPIO.LOW)
GPIO.output(IN3,GPIO.LOW)
GPIO.output(IN4,GPIO.LOW)
def run():
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
def left():
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
def right():
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
def stop():
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
def back():
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
print("Please choose your mode")
print("Mode 1 figure control")
print("Mode 2 location control")
print("Mode 3 remote control")
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
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
                back()
            elif totalFingers==1:
                print("run")
                run()
            elif totalFingers==3:
                print("left")
                left()
            elif totalFingers==4:
                print("right")
                right()
            elif totalFingers==5:
                print("choose mode")
                mode = 5
            else:
                print("stop")
                stop()
        if mode==2:
            locationx = lmList[9][1]
            locationy = lmList[9][2]
            if (locationX - locationx >= 0):
                PWMIN1.ChangeDutyCycle((locationX - locationx) / 6.4)
                GPIO.output(IN2, GPIO.LOW)
                print((locationX - locationx) / 6.4,"----------------x")
            elif (locationX - locationx < 0):
                PWMIN2.ChangeDutyCycle((locationx - locationX) / 6.4)
                GPIO.output(IN1, GPIO.LOW)
                print((locationx - locationX) / 6.4,"----------------x")
            if (locationY - locationy >= 0):
                GPIO.output(IN4, GPIO.LOW)
                PWMIN3.ChangeDutyCycle((locationY - locationy) / 4.8)
                print((locationY - locationy) / 6.4,"-------------------y")
            elif (locationY - locationy < 0):
                print((locationy - locationY) / 6.4,"-------------------y")
                GPIO.output(IN3, GPIO.LOW)
                PWMIN4.ChangeDutyCycle((locationy - locationY) / 4.8)
            if totalFingers==5:
                print("choose mode")
                mode = 5
        if mode==3:
            flag = input("derction:")
            if flag == "w":
                run()
            elif flag == "a":
                left()
            elif flag == "d":
                right()
            elif flag == "s":
                back()
            else:
                stop()
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
