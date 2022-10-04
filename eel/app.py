import numpy as np
import eel
import cv2
import base64
import time

userData = {
    "capHpX": 90,
    "capHpY": 32,
    "capHpW": 190,
    "capHpH": 6,
    "capMpX": 90,
    "capMpY": 45,
    "capMpW": 190,
    "capMpH": 6,

    "homeUse": False,
    "homeHpMin": 0,
    "homeHpMax": 40,
    "homeKey": "8",
    "homeCount": 2,
    "homeCountDelay": 1,
    "homeCool": 0,
    "homePotionUse": False,
    "homePotionThres": 1000000,
    "homePotionPosX": 472,
    "homePotionPosY": 635,
    "homePotionPosW": 13,
    "homePotionPosH": 13,

    "pkActionUse": False,
    "pkActionThres": 1000000,
    "pkActionPosX": 1057,
    "pkActionPosY": 533,
    "pkActionPosW": 25,
    "pkActionPosH": 25,
    "pkActionKey": "7",
    "pkActionCount": 2,
    "pkActionCountDelay": 0.5,
    "pkActionCool": 5,
    "pkActionInputDelay": 0,

    "timer1Use": False,
    "timer1HpMin": 40,
    "timer1HpMax": 60,
    "timer1MpMin": 0,
    "timer1MpMax": 100,
    "timer1Key": "7",
    "timer1Count": 1,
    "timer1CountDelay": 0.5,
    "timer1Cool": 5,

    "timer2Use": False,
    "timer2HpMin": 60,
    "timer2HpMax": 80,
    "timer2MpMin": 30,
    "timer2MpMax": 100,
    "timer2Key": "4",
    "timer2Count": 1,
    "timer2CountDelay": 0.5,
    "timer2Cool": 5,

    "timer3Use": False,
    "timer3HpMin": 0,
    "timer3HpMax": 40,
    "timer3MpMin": 0,
    "timer3MpMax": 100,
    "timer3Key": "1",
    "timer3Count": 1,
    "timer3CountDelay": 0.5,
    "timer3Cool": 1
}

eel.init("web")


#브라우저 창을 닫으면 종료하는 함수
def callback(route, websockets):
    if not websockets:
        exit()

#HTML canvas로부터 받은 base64 이미지를 opencv 이미지로 바꾸는 함수
def b64ToImg(data):
    return cv2.imdecode(np.frombuffer(base64.b64decode(data.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)

#userData에서 capture관련만 모아서 딕셔너리 만들기
def setCapturePos():
    capturePos = {}
    for key in userData.keys():
        if "cap" in key:
            capturePos[key] = userData[key]
    eel.setCapturePos(capturePos)

#readyState 변경하기
readyState = {"capture" : 0, "arduino" : False}
@eel.expose
def updateReadyState(key, value):
    global readyState
    readyState[key] = value
    print(f"{key}값이 {value}으로 변경되었습니다.")
    if key == "capture":
        setCapturePos()

# eel.start("index.html", block=False, mode="edge", close_callback=callback)
eel.start("index.html", block=False, mode="edge")

while True:
    if readyState["capture"] :
        imgB64 = eel.sendImages()()
        img = b64ToImg(imgB64)
    eel.sleep(0.01)
