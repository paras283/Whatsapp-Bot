import pyautogui as pt
from time import sleep
import cv2
import random
import pyperclip

sleep(5)
pos1 = pt.locateOnScreen("images/emoji.png", confidence = .6)
x = pos1[0]
y = pos1[1]

def get_msg():
    global x,y

    pos = pt.locateOnScreen("images/emoji.png", confidence = .6)
    x = pos[0]
    y = pos[1]
    pt.moveTo(x,y)
    pt.moveTo(x+75, y-32)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(45,-122)
    pt.click()
    msg = pyperclip.paste()
    pt.moveTo(x,y)
    print("Message received:" + msg)

    return msg


def response(msg):
    a = random.randrange(3)

    if "?" in str(msg).lower():
        return "Don't ask me any question!!!"

    else:
        if a == 0:
            return "That's cool!!"
        elif a == 1:
            return "Hello!"
        else:
            return " Good Morning!"

def reply(msg):
    global x,y
    pos = pt.locateOnScreen("images/emoji.png", confidence = .6)
    x = pos[0]
    y = pos[1]
    pt.moveTo(x+120, y+10)
    pt.click()
    pt.typewrite(msg, interval = 0.1 )

    pt.typewrite("\n", interval = 0.1)
    sleep(3)

def check_for_new_msg():
    global x, y

    while True:
        print(x,y)
        try:
            pos = pt.locateOnScreen("images/unread.png", confidence=.7)

            if pos is not None:
                pt.moveTo(pos)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)
            else:
                print("ERROR!!")
        except(Exception):
            print("No new msg detected.")

        try:
            if pt.pixelMatchesColor(int(x+75), int(y-32), (255,255,255), tolerance = 10):
                print("Msg detected")

                response_msg = response(get_msg())
                reply(response_msg)
            else:
                print("No new messages yet.....")
        except(Exception):
            print("Can't get pixel for the moment")

        sleep(3)


check_for_new_msg()