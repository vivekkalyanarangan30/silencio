import pyautogui
import pygetwindow as gw
import time
import serial
import asyncio
from PIL import Image
import os

ser = serial.Serial('/dev/tty.usbmodemHIDPC1', 9600) # ls /dev/*
loop = asyncio.get_event_loop()

async def meet_sync(mute_img, unmute_img, region, meeting_id):
    while True:
        mute = pyautogui.locateOnScreen(mute_img, grayscale=True, region=region)
        unmute = pyautogui.locateOnScreen(unmute_img, grayscale=True, region=region)
        if mute:
            if meeting_id == '0':
                ser.write('1'.encode('utf-8'))
            elif meeting_id == '2':
                ser.write('3'.encode('utf-8'))
            elif meeting_id == '4':
                ser.write('5'.encode('utf-8'))
            print("Mic is muted")
        if unmute:
            if meeting_id == '0':
                ser.write('0'.encode('utf-8'))
            if meeting_id == '2':
                ser.write('2'.encode('utf-8'))
            if meeting_id == '4':
                ser.write('4'.encode('utf-8'))
            print("Mic is on")
        await asyncio.sleep(.001)

def cleanup_screen_grabs():
    screenshots = [i for i in os.listdir() if 'screenshot' in i]
    for screenshot in screenshots:
        os.remove(screenshot)
        
if __name__ == "__main__":
    try:
        zoom_mute, zoom_unmute = Image.open('img/zoom/zoom_mute.png'), Image.open('img/zoom/zoom_unmute.png')
        teams_mute, teams_unmute = Image.open('img/teams/teams_mute.png'), Image.open('img/teams/teams_unmute.png')
        gmeet_mute, gmeet_unmute = Image.open('img/gmeet/gmeet_mute.png'), Image.open('img/gmeet/gmeet_unmute.png')

        width, height = pyautogui.size()
        height_mini = int(height*0.4)

        loop.create_task(meet_sync(zoom_mute, zoom_unmute, (0,height_mini,width, height), '4'))
        loop.create_task(meet_sync(teams_mute, teams_unmute, (0,height_mini,width, height), '2'))
        loop.create_task(meet_sync(gmeet_mute, gmeet_unmute, (0,height_mini,width, height), '0'))
        loop.run_forever()
    except KeyboardInterrupt as ke:
        cleanup_screen_grabs()
        exit