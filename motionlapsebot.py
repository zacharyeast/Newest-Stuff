#L298N:
# ENA -> GPIO19
# IN1 -> GPIO7
# IN2 -> GPIO11
# IN3 -> GPIO13
# IN4 -> GPIO15
# ENB -> GPIO21
# 
# +12V -> "NO" (normal open) of Relay Module
# GND (both)_ _|-> -4.5v battery terminal
#            \&|-> GPIO6
# 
# OUT1 -> port(left) DC motor negative wire
# OUT2 -> port(left) DC motor positive wire
# 
# OUT3 -> starboard(right) DC motor positive wire
# OUT4 -> starboard(right) DC motor negative wire
#
#Servo ground (brown) -> GPIO20
#Servo V+ (red) -> GPIO17
#Servo PWM (orange) -> GPIO18

#Relay Module
#DC+ -> GPIO2
#DC- -> GPIO14
#IN -> GPIO3
#NO -> LN298N +12V
#COM -> +4.5v battery terminal

import pygame
import RPi.GPIO as GPIO
import time
from pygame import mixer
from time import sleep
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(3, GPIO.OUT) # -> "IN" Relay Module 
GPIO.output(3, 1)
GPIO.output(7,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)
GPIO.output(19,True)
GPIO.output(21,True)
keyslow = GPIO.PWM(19,100)
keyslow2 = GPIO.PWM(21,100)
keyslow.start(100)
keyslow2.start(100)
def stop():
    GPIO.output(7,0)
    GPIO.output(11,0)
    GPIO.output(13,0)
    GPIO.output(15,0)
def key_up():
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(15,True)
def key_slow():
    keyslow.ChangeDutyCycle(56)
    keyslow2.ChangeDutyCycle(56)
def key_slow2():
    keyslow.ChangeDutyCycle(30)
    keyslow2.ChangeDutyCycle(30)
def key_slow3():
    keyslow.ChangeDutyCycle(45)
    keyslow2.ChangeDutyCycle(45)
    
    
def key_slowstop():
    keyslow.ChangeDutyCycle(100)
    keyslow2.ChangeDutyCycle(100)
def key_slowleft():
    keyslow.ChangeDutyCycle(66)
    keyslow2.ChangeDutyCycle(66)
    
def key_down():
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,True)
    GPIO.output(15,False)
def key_left():
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,True)
def key_right():
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,True)
    GPIO.output(15,False)
def key_right2():
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(15,False)
def key_left2():
    GPIO.output(7,False)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,True)    
def turn_off():
    GPIO.output(3,1)
def turn_on():
    GPIO.output(3,0)
GPIO.setup(18,GPIO.OUT)
servo1 = GPIO.PWM(18,50)
servo1.start(0)

def key_p(): #press p to rock the servo, then release 
    servo1.ChangeDutyCycle(11)
def key_o(): #press o to toggle the servo, then press p to release
    servo1.ChangeDutyCycle(11)
def recenter():
    servo1.ChangeDutyCycle(8)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
    sleep(0.1)
def key_more():
    servo1.ChangeDutyCycle(12)
click_rect1  = pygame.Rect(160, 100, 60, 60) #1 (forward)
click_rect2  = pygame.Rect(220, 160, 60, 60) #2 (Right)
click_rect3  = pygame.Rect(100, 160, 60, 60) #3 (left) 
click_rect4  = pygame.Rect(160, 220, 60, 60) #4 (reverse)
click_rect5  = pygame.Rect(100, 100, 60, 60) #5 (slow left)
click_rect6  = pygame.Rect(220, 100, 60, 60) #6 (slow right)
click_rect7  = pygame.Rect(100, 220, 60, 60) #7 (tank left)
click_rect8  = pygame.Rect(220, 220, 60, 60) #8 (tank right)
click_rectp  = pygame.Rect(0, 0, 60, 60) #p
click_rectturnon = pygame.Rect(0, 100, 60, 60) # turn on
click_rectslowforward = pygame.Rect(160, 40, 60, 60) #slow forward
click_rectslowreverse = pygame.Rect(160, 160, 60, 60) #slow reverse

    
def motion_lapse():
    key_up()
    sleep(0.05)
    for i in range(8):
        key_slow2()
        key_up()
        sleep(1)
        stop()
        key_slowstop()
        key_up()
        sleep(0.05)
        stop()

def motion_lapsefullspeed():
    for i in range(10):
        key_up()
        sleep(.25)
        stop()
        sleep(3)
def motion_lapsebackward_fullspeed():
    for i in range(10):
        key_down()
        sleep(0.25)
        stop()
        sleep(3)
def motion_lapseslow():
    for i in range(10):
        key_slow2()
        key_up()
def motion_lapseslow2():
    for i in range(10):
        key_slow3()
        key_up()
def motion_lapseslow3():
    for i in range(10):
        key_slow3()
        key_right2()
        key_up()
        key_slow3()
def main():
    pygame.init()
    screen = pygame.display.set_mode((380, 380))
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(160, 100, 60, 60)) #1 (forward)
    pygame.draw.rect(screen, (128, 0, 128), pygame.Rect(220, 160, 60, 60)) #2 (Right)
    pygame.draw.rect(screen, (128, 128, 255), pygame.Rect(100, 160, 60, 60)) #3 (left) 
    pygame.draw.rect(screen, (128, 128, 0), pygame.Rect(160, 220, 60, 60)) #4 (reverse)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 60, 60)) #p 
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(100, 100, 60, 60)) #5 (slow left) 
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(220, 100, 60, 60)) #6 (slow right)
    pygame.draw.rect(screen, (10, 55, 10), pygame.Rect(100, 220, 60, 60)) #7 (tank left)
    pygame.draw.rect(screen, (12, 35, 13), pygame.Rect(220, 220, 60, 60)) #8 (tank right)
    pygame.draw.rect(screen, (129, 25, 13), pygame.Rect(160, 40, 60, 60)) # slow forward
    pygame.draw.rect(screen, (1, 35, 55), pygame.Rect(160, 160, 60, 60)) #8 slow reverse    
    pygame.draw.rect(screen, (130, 35, 220), pygame.Rect(0, 100, 60, 60)) # turn on
    pygame.display.flip()
    
    while True:                 
        for event in pygame.event.get():            
            turn_on()
            if event.type == pygame.QUIT:                
                GPIO.cleanup()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:                    
                    GPIO.cleanup()
                    sys.exit()
                if event.key == pygame.K_UP:                    
                    key_up()
                if event.key == pygame.K_DOWN:
                    key_down()
                if event.key == pygame.K_LEFT:
                    key_left2()
                if event.key == pygame.K_RIGHT:
                    key_right2()
                if event.key == pygame.K_p:
                    key_more()
                if event.key == pygame.K_o:
                    key_more()
                if event.key == pygame.K_i:
                    turn_on()
                if event.key == pygame.K_u:                
                    turn_off()
                if event.key == pygame.K_m:
                    key_right()
                if event.key == pygame.K_n:
                    key_left()
                if event.key == pygame.K_q:
                    motion_lapseslow()
                if event.key == pygame.K_w:
                    motion_lapseslow2()
                if event.key == pygame.K_e:
                    motion_lapseslow3()
#                if event.key == pygame.K_r:
                    
#                if event.key == pygame.K_t:
                    
                if event.key == pygame.K_y:
                    motion_lapseslow2()                    
                if event.key == pygame.K_s:
                    key_slow()
                    key_down()                    
                if event.key == pygame.K_a:
                    key_slowleft()
                    key_left()
                if event.key == pygame.K_d:
                    key_slowleft()
                    key_right()
                if event.key == pygame.K_KP_DIVIDE:
                    key_slow()
                    key_up()
                if event.key == pygame.K_KP1:
                    key_left()
                if event.key == pygame.K_KP2:
                    key_down()
                if event.key == pygame.K_KP3:
                    key_right()
                if event.key == pygame.K_KP4:
                    key_left2()
                if event.key == pygame.K_KP5:
                    key_slow()
                    key_down()
                if event.key == pygame.K_KP6:
                    key_right2()
                if event.key == pygame.K_KP7:
                    key_slowleft()
                    key_left()
                if event.key == pygame.K_KP8:
                    key_up()
                if event.key == pygame.K_KP9:
                    key_slowleft()
                    key_right()
                if event.key == pygame.K_d:
                    key_slowleft()
                    key_right()
        if event.type == pygame.KEYUP:
               if event.key == pygame.K_UP:
                   stop()
               if event.key == pygame.K_LEFT:
                   stop()
               if event.key == pygame.K_RIGHT:
                   stop()
               if event.key == pygame.K_DOWN:
                   stop()
               if event.key == pygame.K_u:
                   turn_off()                   
               if event.key == pygame.K_p:
                   recenter()
               if event.key == pygame.K_m:
                   stop()
               if event.key == pygame.K_n:
                   stop()
               if event.key == pygame.K_o:
                   servo1.ChangeDutyCycle(0)                   
               if event.key == pygame.K_w:
                   stop()
                   key_slowstop()
               if event.key == pygame.K_s:
                   stop()
                   key_slowstop()
               if event.key == pygame.K_r:
                   stop()
                   key_slowstop()                   
               if event.key == pygame.K_a:
                   stop()
                   key_slowstop()
               if event.key == pygame.K_d:
                   stop()
                   key_slowstop()
               if event.key == pygame.K_KP1:
                   stop()
               if event.key == pygame.K_KP2:
                   stop()
               if event.key == pygame.K_KP3:
                   stop()
               if event.key == pygame.K_KP4:
                   stop()
               if event.key == pygame.K_KP5:
                   stop()
                   key_slowstop()
               if event.key == pygame.K_KP6:
                   stop()
               if event.key == pygame.K_KP7:
                   stop()
                   key_slowstop()
               if event.key == pygame.K_KP8:
                   stop()
               if event.key == pygame.K_KP9:
                   stop()
                   key_slowstop()
               if event.key == pygame.K_KP_DIVIDE:
                   stop()
                   key_slowstop()                   
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if (click_rect1.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_up()                        
                if (click_rect2.collidepoint(mouse_position)):
                    if event.button == 1:
                        key_right2()                        
                if (click_rect3.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_left2()
                if (click_rect7.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_left()
                if (click_rect8.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_right()                      
                if (click_rect4.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_down()
                if (click_rect5.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_slowleft()
                        key_left()
                if (click_rect6.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_slowleft()
                        key_right()                       
                if (click_rectp.collidepoint(mouse_position)):
                    if event.button == 1: #left click to rock the servo, then release 
                        key_more()
                if (click_rectp.collidepoint(mouse_position)):
                    if event.button == 2: #right click to toggle the servo, then left click to release 
                        key_more()                     
                if (click_rectp.collidepoint(mouse_position)):
                    if event.button == 3: #right click to toggle the servo, then left click to release 
                        key_more()
                if (click_rectturnon.collidepoint(mouse_position)):
                    if event.button == 1:
                        turn_off()
                if (click_rectslowforward.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_slow()
                        key_up()
                if (click_rectslowreverse.collidepoint(mouse_position)):
                    if event.button == 1:                         
                        key_slow()
                        key_down()
        if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if (click_rect1.collidepoint(mouse_position)):
                        stop()           
                if event.button == 1:
                    if (click_rectp.collidepoint(mouse_position)):
                        recenter()
                if event.button == 2:
                    if (click_rectp.collidepoint(mouse_position)):
                        recenter()
                if event.button == 3:
                    if (click_rectp.collidepoint(mouse_position)):                       
                        servo1.ChangeDutyCycle(0)
                if event.button == 1:
                    if (click_rect2.collidepoint(mouse_position)):
                        stop()
                if event.button == 1:
                    if (click_rect3.collidepoint(mouse_position)):
                        stop()
                if event.button == 1:
                    if (click_rect5.collidepoint(mouse_position)):
                        stop()
                        key_slowstop()
                if event.button == 1:
                    if (click_rect6.collidepoint(mouse_position)):
                        stop()
                        key_slowstop()                        
                if event.button == 1:
                    if (click_rect4.collidepoint(mouse_position)):
                        stop()
                if event.button == 1:
                    if (click_rect7.collidepoint(mouse_position)):
                        stop()                          
                if event.button == 1:
                    if (click_rect8.collidepoint(mouse_position)):
                        stop()                          
                if event.button == 1:
                    if (click_rectturnon.collidepoint(mouse_position)):
                        turn_off()
                if event.button == 1:
                    if (click_rectslowforward.collidepoint(mouse_position)):                
                       stop()
                       key_slowstop()
                if event.button == 1:
                    if (click_rectslowreverse.collidepoint(mouse_position)):                
                       stop()
                       key_slowstop() 
                elif event.button == 3:
                    stop()
main()
 
