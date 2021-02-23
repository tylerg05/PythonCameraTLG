from picamera import PiCamera
from gpiozero import Button
from time import sleep
from datetime import date, time, datetime

camera = PiCamera()
camera.rotation = 180
button_cam = Button(5)

def take_picture():
    timestamp = datetime.now()
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/capture%s.jpg' % timestamp)
    camera.stop_preview()

button_cam.when_pressed = take_picture