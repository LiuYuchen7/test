# -*- coding:UTF-8 -*-
from __future__ import division
from picamera import  Color
import time
import demjson
from pygame import mixer
from aip import AipBodyAnalysis
from aip import AipSpeech
import cv2
from aip import AipFace
import base64
import pprint
import pyttsx3
import Adafruit_PCA9685
import socket
import RPi.GPIO as GPIO
#ENA = 13
#ENB = 14
IN1 = 5
IN2 = 6
IN3 = 19
IN4 = 20
address=('10.68.6.13',8843)
flag = "Null"

mode = 1
locationX = 320
locationY = 240
locationx = 320
locationy = 240
hand = {'One': '数字1', 'Five': '数字5', 'Fist': '拳头', 'Ok': 'OK',
        'Prayer': '祈祷', 'Congratulation': '作揖', 'Honour': '作别',
        'Heart_single': '比心心', 'Thumb_up': '点赞', 'Thumb_down': 'Diss',
        'ILY': '我爱你', 'Palm_up': '掌心向上', 'Heart_1': '双手比心1',
        'Heart_2': '双手比心2', 'Heart_3': '双手比心3', 'Two': '数字2',
        'Three': '数字3', 'Four': '数字4', 'Six': '数字6', 'Seven': '数字7',
        'Eight': '数字8', 'Nine': '数字9', 'Rock': 'Rock', 'Insult': '竖中指', 'Face': '脸'}

# 下面的key要换成自己的
""" 人体分析 APPID AK SK """
APP_ID = '23839139'
API_KEY = 'REZenPR578Gl1lA2p1hZAmX8'
SECRET_KEY = 'Di9G18DdAZAlSQujhGqGZNrUdO6G9Ck2'
"""人脸识别 APPID AK SK"""
client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

'''cam config'''

""" 读取图片 """
#完成标准的socket连接，绑定，监听，以树莓派为server
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(address)
#初始化舵机

flag=0
GPIO.setmode(GPIO.BCM)
#GPIO.setup(ENA,GPIO.OUT)
#GPIO.setup(ENB,GPIO.OUT)
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
#GPIO.output(ENA,GPIO.HIGH)
#GPIO.output(ENB,GPIO.HIGH)
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
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
cameraCapture = cv2.VideoCapture(0)
fps = cameraCapture.get(cv2.CAP_PROP_FPS)
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('record.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'),fps, size)
success, frame = cameraCapture.read()

if __name__ == "__main__":
    while True:
        res = " "
        success, frame = cameraCapture.read()
        """ 2.调用手势识别 """
        cv2.imwrite('image.jpg', frame)
        image = get_file_content('image.jpg')
        raw = str(client.gesture(image))
        text = demjson.decode(raw)
        try:
            res = text['result'][0]['classname']
            locationx = text['result'][0]['top']+(int)(text['result'][0]['height']/2)
            locationy = text['result'][0]['left']+(int)(text['result'][0]['width']/2)
        except:
            #print('识别结果：什么也没识别到哦~')
            i=1
        else:
            pass
            #print('识别结果：' + hand[res])
        if res=="One":
            mode = 1
            print("mode One")
            PWMIN1.stop()
            PWMIN2.stop()
            PWMIN3.stop()
            PWMIN4.stop()
        if res=="Two":
            mode = 2
            print("mode Two")
            PWMIN1.start(0)
            PWMIN2.start(0)
            PWMIN3.start(0)
            PWMIN4.start(0)
        if res=="Three":
            mode = 3
            print("mode Three")
            PWMIN1.stop()
            PWMIN2.stop()
            PWMIN3.stop()
            PWMIN4.stop()
        if mode==1:
            if res=="Five":
                print("back")
                back()
            elif res=="Thumb_up":
                print("run")
                left()
            elif res=="Thumb_down":
                print("back")
                right()
            elif res=="Fist":
                print("left")
                run()
            else:
                print("stop")
                stop()
        elif mode==2:
            if res == "Fist":
                if(locationX-locationx>=0):
                    PWMIN1.ChangeDutyCycle((locationX-locationx)/4,8)
                elif(locationX-locationx<0):
                    PWMIN2.ChangeDutyCycle((locationx - locationX) / 4.8)
                if (locationY - locationy >= 0):
                    PWMIN3.ChangeDutyCycle((locationY - locationy) / 6.4)
                elif (locationX - locationx < 0):
                    PWMIN4.ChangeDutyCycle((locationy - locationY) / 6.4)
        elif mode==3:
            flag=input("derction:")
            if flag=="w":
                run()
            elif flag=="a":
                left()
            elif flag=="d":
                right()
            elif flag=="s":
                back()
            else:
                stop()




