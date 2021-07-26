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
#from pygame import mixer
from time import sleep
import sys
from sys import exit

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(3, GPIO.OUT) # -> "IN" Relay Module
#GPIO.setup(23,GPIO.IN) # ir sensor
#sensor=GPIO.input(23)
PIN_TRIGGER = 40 
PIN_ECHO = 38
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
GPIO.output(PIN_TRIGGER, GPIO.LOW)
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
def key_slow_q():
    keyslow.ChangeDutyCycle(29)
    keyslow2.ChangeDutyCycle(29)   
def key_slow():
    keyslow.ChangeDutyCycle(74)
    keyslow2.ChangeDutyCycle(74)
def key_slow2():
    keyslow.ChangeDutyCycle(29)
    keyslow2.ChangeDutyCycle(29)    
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
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,True)
    GPIO.output(15,False)
def key_right():
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,True)
def key_right2():
    GPIO.output(7,False)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,True)
def key_left2():
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(15,False)    
def turn_off():
    GPIO.output(3,0)
def turn_on():
    GPIO.output(3,1)
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
click_rectroveforward = pygame.Rect(0, 320, 60, 60) #rove forward
click_rectendrove = pygame.Rect(0, 380, 60, 60) #end rove forward
pygame.font.init()
textfont=pygame.font.SysFont("hello", 50)
pygame.init()
clock=pygame.time.Clock()
FPS=30
safe_distance = 15
# test_font = pygame.font.Font(None, 50)
# text_surface = test_font.render('MyGame',False,(200,200,200))
# test_surface = pygame.Surface((100,100))
# test_surface.fill((100,250,100))

def main():
    sleep(0.01)
    stop()
    sleep(0.01)
    screen = pygame.display.set_mode((380, 600))
    pygame.display.set_caption("Rover Remote")
    sleep(0.001)
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
    pygame.draw.rect(screen, (135, 255, 210), pygame.Rect(0, 320, 60, 60)) # rove forward
    pygame.draw.rect(screen, (135, 25, 210), pygame.Rect(0, 380, 60, 60)) # end rove forward   

    pygame.display.flip()



    while True:          
        sleep(0.001)
        stop()
        sleep(0.001)
#         screen.blit(test_surface,(10,10))
#         screen.blit(text_surface,(300,500))
        def rover_ultra_sense():
            GPIO.output(PIN_TRIGGER, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(PIN_TRIGGER, GPIO.LOW)
            while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()        
            while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()
            sleep(0.001)
            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            print("Distance:",distance,"cm")
            distance3 = str(distance)
            
            texttbd=textfont.render(distance3,1,(250,250,250))

            screen.blit(texttbd,(1,550))    
            pygame.display.flip()            
#            clock.tick(FPS)
            if distance <= safe_distance:
                print("OBJECT DETECTED AT THE FORWARD")
                stop()
                sleep(0.1)
                main()
                distance4 = "Object Detected!"
                
                texttbd2=textfont.render(distance4,1,(250,250,250))

                screen.blit(texttbd2,(1,550))    
                pygame.display.flip()                 
                clock.tick(FPS)
            
        def rover_forward_back_loop():
            counter = 1
            sleep(0.001)
            while True:
                if (counter % 2) !=0:
                    sleep(0.01)
                    key_up()
                    sleep(0.01)
                    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
                    time.sleep(0.00001)
                    GPIO.output(PIN_TRIGGER, GPIO.LOW)
                    sleep(0.001)

                    while GPIO.input(PIN_ECHO)==0:
                        sleep(0.0001)
                        pulse_start_time = time.time()
                        sleep(0.0001)
                    while GPIO.input(PIN_ECHO)==1:
                        pulse_end_time = time.time()
                    sleep(0.1)
                    pulse_duration = pulse_end_time - pulse_start_time
                    sleep(0.01)
                    distance = round(pulse_duration * 17150, 2)
                    sleep(0.01)
                    print("Distance:",distance,"cm")
                    sleep(0.01)
                    clock.tick(FPS)
                    if distance <= safe_distance:
                        print("OBJECT DETECTED AT THE FORWARD")
                        stop()
                        sleep(0.5)
                        key_down()
                        sleep(0.8)
                        stop()
                        counter = counter + 1
                        sleep(0.01)
                        clock.tick(FPS)
                        continue
                elif (counter % 2) ==0:
                    sleep(0.01)
                    key_down()
                    sleep(0.01)
                    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
                    time.sleep(0.00001)
                    GPIO.output(PIN_TRIGGER, GPIO.LOW)
                    while GPIO.input(PIN_ECHO)==0:
                        pulse_start_time = time.time()        
                    while GPIO.input(PIN_ECHO)==1:
                        pulse_end_time = time.time()
                    sleep(0.001)
                    pulse_duration = pulse_end_time - pulse_start_time
                    sleep(0.01)
                    distance = round(pulse_duration * 17150, 2)
                    sleep(0.01)
                    print("Distance:",distance,"cm")
                    
                    if distance <= safe_distance:
                        print("OBJECT DETECTED AT THE FORWARD")
                        stop()
                        sleep(0.5)
                        key_up()
                        sleep(0.8)
                        stop()
                        counter = counter + 1
                        sleep(0.01)
                        clock.tick(FPS)
                        continue
                clock.tick(FPS)
                for event in pygame.event.get():
                    sleep(0.01)
                    if event.type == pygame.KEYUP:
                        sleep(0.01)
                        if event.key == pygame.K_a:
                            sleep(0.01)
                            forward = 0
                            stop()
                            sleep(0.001)
                            main()
        def rover_forward():
            key_up()
            while True:
                rover_ultra_sense()
                sleep(0.01)
                
                clock.tick(FPS)
                
                for event in pygame.event.get():
                    sleep(0.01)
                    if event.type == pygame.KEYUP:
                        sleep(0.01)
                        if event.key == pygame.K_a:
                            sleep(0.01)
                            forward = 0
                            stop()
                            sleep(0.001)
                            clock.tick(FPS)
                            main()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_position = pygame.mouse.get_pos()                    
                        if (click_rectendrove.collidepoint(mouse_position)):
                            if event.button == 1:                        
                                sleep(0.01)
                                forward = 0
                                stop()
                                sleep(0.001)
                                clock.tick(FPS)
                                main()                            
                    if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_w:
                           stop()
                           sleep(0.001)
                           main()
                           
                          
        def rover_reverse():
            key_down()
            sleep(0.01)
                
            clock.tick(FPS)
            while True:
                rover_ultra_sense()
                sleep(0.001)
                clock.tick(FPS)
                for event in pygame.event.get():
                    sleep(0.01)
                    if event.type == pygame.KEYUP:
                        sleep(0.01)
                        if event.key == pygame.K_a:
                            sleep(0.01)
                            forward = 0
                            stop()
                            sleep(0.001)
                            clock.tick(FPS)
                            main()                        
                    if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_q:
                           stop()
                           sleep(0.001)
                           main()
                
        def ultra_sense():
            GPIO.output(PIN_TRIGGER, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(PIN_TRIGGER, GPIO.LOW)
            while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()        
            while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()
            sleep(0.1)
            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            print("Distance:",distance,"cm")
            distance2 = str(distance)
            
            texttbd=textfont.render(distance2,1,(250,250,250))

            screen.blit(texttbd,(1,550))
            sleep(0.01)
            pygame.display.flip()
            if distance <= safe_distance:
                print("OBJECT DETECTED AT THE FORWARD")
                key_down()
                sleep(0.8)
                stop()
                sleep(0.1)
                texttbd=textfont.render("OBJECT DETECTED AT THE FORWARD",1,(250,250,250))

                screen.blit(texttbd,(0,550))
                pygame.display.flip()
                clock.tick(FPS)

        for event in pygame.event.get():

            turn_on()
            stop()
            sleep(0.001)
#            ultra_sense()
            if event.type == pygame.QUIT:
                sleep(0.01)
#                turn_off()
                sleep(0.01)
                GPIO.cleanup()
                sleep(0.01)
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:                    
                    GPIO.cleanup()
                    sys.exit()                
                if event.key == pygame.K_UP:
                    key_up()
                    sleep(0.001)
                    while True:
                        ultra_sense()
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_UP:
                                   stop()
                                   sleep(0.001)
                                   main()
                    
                if event.key == pygame.K_DOWN:
                    key_down()
                    while True:
                        ultra_sense()
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_DOWN:
                                   stop()
                                   sleep(0.001)
                                   main()
                                   clock.tick(FPS)
                if event.key == pygame.K_LEFT:
                    key_left2()
                    sleep(0.01)
                    while True:
                        sleep(0.001)
                        ultra_sense()
                        sleep(0.001)
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            sleep(0.001)
                            if event.type == pygame.KEYUP:
                                sleep(0.001)
                                if event.key == pygame.K_LEFT:
                                   sleep(0.001)
                                   stop()
                                   sleep(0.001)
                                   main()
                                   clock.tick(FPS)
                                   sleep(0.01)
                if event.key == pygame.K_RIGHT:
                    key_right2()
                    while True:
                        sleep(0.01)
                        ultra_sense()
                        sleep(0.01)
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            sleep(0.01)
                            if event.type == pygame.KEYUP:
                                sleep(0.01)
                                if event.key == pygame.K_RIGHT:
                                    sleep(0.01)
                                    stop()
                                    sleep(0.01)
                                    clock.tick(FPS)
                                    main()
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
                    rover_forward()
                if event.key == pygame.K_w:
                    rover_reverse()
                  
                if event.key == pygame.K_e:
                    rover_forward_back_loop()
#                if event.key == pygame.K_r:
                    
#                if event.key == pygame.K_t:
                    
                if event.key == pygame.K_y:
                    motion_lapseslow2()                    
                if event.key == pygame.K_s:
                    key_slow()
                    key_down()                    
#                if event.key == pygame.K_a:

                if event.key == pygame.K_d:
                    key_slowleft()
                    key_right()
                if event.key == pygame.K_KP_DIVIDE:
                    key_slow()
                    key_up()
                    while True:
                        ultra_sense()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_KP_DIVIDE:
                                   stop()
                                   sleep(0.001)
                                   main()                      
                if event.key == pygame.K_KP1:
                    key_left()
                    sleep(0.001)
                    while True:
                        ultra_sense()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_KP1:
                                   stop()
                                   sleep(0.001)
                                   main()                    
                if event.key == pygame.K_KP2:
                    key_down()
                    while True:
                        ultra_sense()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_KP2:
                                   stop()
                                   sleep(0.001)
                                   main()                      
                if event.key == pygame.K_KP3:
                    key_right()
                    while True:
                        ultra_sense()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_KP3:
                                   stop()
                                   sleep(0.001)
                                   main()                      
                if event.key == pygame.K_KP4:
                    key_left2()
                    while True:
                        ultra_sense()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_KP4:
                                   stop()
                                   sleep(0.001)
                                   main()                      
                if event.key == pygame.K_KP5:
                    key_slow()
                    key_down()
                    while True:
                        ultra_sense()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_KP5:
                                   stop()
                                   sleep(0.001)
                                   main()                      
                if event.key == pygame.K_KP6:
                    key_right2()
                    while True:
                        ultra_sense()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_KP6:
                                   stop()
                                   sleep(0.001)
                                   main()                      
                if event.key == pygame.K_KP7:
                    key_slowleft()
                    key_left()
                    while True:
                        ultra_sense()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_KP7:
                                   stop()
                                   sleep(0.001)
                                   main()                      
                if event.key == pygame.K_KP8:
                    key_up()
                    while True:
                        ultra_sense()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_KP8:
                                   stop()
                                   sleep(0.001)
                                   main()                      
                if event.key == pygame.K_KP9:
                    key_slowleft()
                    key_right()
                    while True:
                        ultra_sense()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                               if event.key == pygame.K_KP9:
                                   stop()
                                   sleep(0.001)
                                   main()                      

            if event.type == pygame.KEYUP:
               if event.key == pygame.K_UP:
                   sleep(0.1)
                   stop()
                   sleep(0.1)
                   main()
               if event.key == pygame.K_LEFT:
                   stop()
                   sleep(0.1)
                   main()  
               if event.key == pygame.K_RIGHT:
                   stop()
               if event.key == pygame.K_DOWN:
                   stop()
               if event.key == pygame.K_u:
                   turn_off()                   
               if event.key == pygame.K_p:
                   recenter()
               if event.key == pygame.K_q:
                   stop()                   
               if event.key == pygame.K_m:
                   stop()
               if event.key == pygame.K_n:
                   stop()
               if event.key == pygame.K_o:
                   servo1.ChangeDutyCycle(0)                   
               if event.key == pygame.K_w:
#                   stop()
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
                        while True:
                            ultra_sense()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    stop()
                                    sleep(0.001)
                                    main()    
                if (click_rect2.collidepoint(mouse_position)):
                    if event.button == 1:                       
                        key_right2()
                        while True:
                            sleep(0.0001)
                            ultra_sense()
                            sleep(0.0001)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    stop()
                                    sleep(0.001)
                                    main()                          
                if (click_rect3.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_left2()
                        while True:
                            sleep(0.0001)
                            ultra_sense()
                            sleep(0.0001)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    stop()
                                    sleep(0.001)
                                    main()                          
                if (click_rect7.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_left()
                        while True:
                            sleep(0.0001)
                            ultra_sense()
                            sleep(0.0001)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    stop()
                                    sleep(0.001)
                                    main()                          
                if (click_rect8.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_right()
                        while True:
                            sleep(0.0001)
                            ultra_sense()
                            sleep(0.0001)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    stop()
                                    sleep(0.001)
                                    main()                          
                if (click_rect4.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_down()
                        while True:
                            sleep(0.0001)
                            ultra_sense()
                            sleep(0.0001)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    stop()
                                    sleep(0.001)
                                    main()                          
                if (click_rect5.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_slowleft()
                        key_left()
                        while True:
                            sleep(0.0001)
                            ultra_sense()
                            sleep(0.0001)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    stop()
                                    sleep(0.001)
                                    main()                          
                if (click_rect6.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_slowleft()
                        key_right()
                        while True:
                            sleep(0.0001)
                            ultra_sense()
                            sleep(0.0001)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    stop()
                                    sleep(0.001)
                                    main()                          
#                 if (click_rectp.collidepoint(mouse_position)):
#                     if event.button == 1: #left click to rock the servo, then release 
#                         key_more()
#                 if (click_rectp.collidepoint(mouse_position)):
#                     if event.button == 2: #right click to toggle the servo, then left click to release 
#                         key_more()                     
#                 if (click_rectp.collidepoint(mouse_position)):
#                     if event.button == 3: #right click to toggle the servo, then left click to release 
#                         key_more()
                if (click_rectturnon.collidepoint(mouse_position)):
                    if event.button == 1:
                        turn_off()
                if (click_rectslowforward.collidepoint(mouse_position)):
                    if event.button == 1: 
                        key_slow()
                        key_up()
                        while True:
                            sleep(0.0001)
                            ultra_sense()
                            sleep(0.0001)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    stop()
                                    sleep(0.001)
                                    main()                          
                if (click_rectslowreverse.collidepoint(mouse_position)):
                    if event.button == 1:                         
                        key_slow()
                        key_down()
                        while True:
                            sleep(0.0001)
                            ultra_sense()
                            sleep(0.0001)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    stop()
                                    sleep(0.001)
                                    main()

                if (click_rectroveforward.collidepoint(mouse_position)):
                    if event.button == 1:                         
                        rover_forward()
                if (click_rectendrove.collidepoint(mouse_position)):
                    if event.button == 1:                        
                        sleep(0.01)
                        forward = 0
                        stop()
                        sleep(0.001)
                        main()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_position = pygame.mouse.get_pos()
                    if (click_rect1.collidepoint(mouse_position)):
                        stop()
                        main()  
#                 if event.button == 1:
#                     if (click_rectp.collidepoint(mouse_position)):
#                         recenter()
#                 if event.button == 2:
#                     if (click_rectp.collidepoint(mouse_position)):
#                         recenter()
#                 if event.button == 3:
#                     if (click_rectp.collidepoint(mouse_position)):                       
#                         servo1.ChangeDutyCycle(0)
                if event.button == 1:
                    if (click_rect2.collidepoint(mouse_position)):
                        stop()
                        main()  
                if event.button == 1:
                    if (click_rect3.collidepoint(mouse_position)):
                        stop()
                        main()  
                if event.button == 1:
                    if (click_rect5.collidepoint(mouse_position)):
                        stop()
                        key_slowstop()
                        main()  
                if event.button == 1:
                    if (click_rect6.collidepoint(mouse_position)):
                        stop()
                        key_slowstop()
                        main()  
                if event.button == 1:
                    if (click_rect4.collidepoint(mouse_position)):
                        stop()
                        main()  
                if event.button == 1:
                    if (click_rect7.collidepoint(mouse_position)):
                        stop()
                        main()  
                if event.button == 1:
                    if (click_rect8.collidepoint(mouse_position)):
                        stop()
                        main()  
                if event.button == 1:
                    if (click_rectturnon.collidepoint(mouse_position)):
                        turn_off()
                        main()  
                if event.button == 1:
                    if (click_rectslowforward.collidepoint(mouse_position)):                
                       stop()
                       key_slowstop()
                       main()  
                if event.button == 1:
                    if (click_rectslowreverse.collidepoint(mouse_position)):                
                       stop()
                       key_slowstop()
                       main()  
                elif event.button == 3:
                    stop()
                    main()
                
#        stop()

        clock.tick(FPS)
main()
