import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
servo1=GPIO.PWM(3,50)
servo1.start(0)
while True:
    print(time.strftime("%I:%M"))
    servo1.ChangeDutyCycle(4)
    time.sleep(.8)
    servo1.ChangeDutyCycle(6)
    time.sleep(0.75)
    servo1.ChangeDutyCycle(0)
    time.sleep(275)
    
    