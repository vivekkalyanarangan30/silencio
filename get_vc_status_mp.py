import pyautogui
import pygetwindow as gw
import time
import serial
import multiprocessing
import os

ser = serial.Serial('/dev/tty.usbmodem14201', 9600) # ls /dev/*

def meet_sync(mute_img, unmute_img):
    while True:
        mute = pyautogui.locateOnScreen(mute_img, grayscale=True)
        unmute = pyautogui.locateOnScreen(unmute_img, grayscale=True)
        if mute:
            ser.write('1'.encode('utf-8'))
            print("Mic is muted")
        if unmute:
            ser.write('0'.encode('utf-8'))
            print("Mic is on")

if __name__ == "__main__":
    zoom_mute, zoom_unmute = 'img/zoom/zoom_mute.png', 'img/zoom/zoom_unmute.png'
    teams_mute, teams_unmute = 'img/teams/teams_mute.png', 'img/teams/teams_unmute.png'
    gmeet_mute, gmeet_unmute = 'img/gmeet/gmeet_mute.png', 'img/gmeet/gmeet_unmute.png'

    p1 = multiprocessing.Process(target=meet_sync, args=(zoom_mute, zoom_unmute))
    p2 = multiprocessing.Process(target=meet_sync, args=(teams_mute, teams_unmute))
    p3 = multiprocessing.Process(target=meet_sync, args=(gmeet_mute, gmeet_unmute))

    p2.start()
    p1.start()
    p3.start()