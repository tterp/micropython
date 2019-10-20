"""SSD1351 demo (bouncing boxes)."""
from machine import Pin, SPI
from random import random, seed
from ssd1351 import Display, color565
from utime import sleep_us, ticks_cpu, ticks_us, ticks_diff



p1 = Pin(12, Pin.IN, Pin.PULL_UP)
p2 = Pin(13, Pin.IN, Pin.PULL_UP)
p3 = Pin(14, Pin.IN, Pin.PULL_UP)
p4 = Pin(25, Pin.IN, Pin.PULL_UP)
p5 = Pin(26, Pin.IN, Pin.PULL_UP)
p6 = Pin(27, Pin.IN, Pin.PULL_UP)
p7 = Pin(15, Pin.IN, Pin.PULL_UP)
        # create input pin on GPIO2
        # get 

        # Baud rate of 14500000 seems about the max
spi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(17), cs=Pin(5), rst=Pin(16))

Pause = 0      #
x = 8          #
y = 4          # indstillinger for pause
xspeed = 1     #
yspeed = 2     #
lt = 1
rt = 1
hb = 1
lb = 1
bt = 1
ne = 1
oi = 1
ttr = 0
ttl = 0
while True:
    
   
    Pause += 1
            
    x += xspeed
    y += yspeed

    if y > 62 or y < 2:
        yspeed *= -1

    if x > 63 or x < 1:
        xspeed *= -1 
    if p7.value() == 0:
        lb = 0
        hb = 1
        rt = 1
        lt = 1
    if p2.value() == 0:
        hb = 0
        lb = 1
        rt = 1
        lt = 1
    if p5.value() == 0:
        oi = 0
        rt = 1
        lt = 1
    if p6.value() == 0:
        bt = 0
        rt = 1
        lt = 1
    if p4.value() == 0:
        ne = 0
        rt = 1
        lt = 1
    if p1.value() == 0:
        rt = 0
        lt = 1
        lb = 1
        hb = 1
        oi = 1
        bt = 1
        ne = 1
        ttr = 1
    if p1.value() == 1:
        rt = 1
    if p3.value() == 0:
        lt = 0
        rt = 1
        lb = 1
        hb = 1
        oi = 1
        bt = 1
        ne = 1
        ttl = 1
    if p3.value() == 1:    
        lt = 1
    
    #if p2.value() == 0 and Pause > 400:
     #   display.draw_image('sort.raw', x - 8, y - 4, 64, 64) 
      #  display.draw_image('langlys.raw', x, y, 64, 64)          
    
    #if p7.value() == 0 and Pause < 400:
     #   display.draw_image('kortlys.raw', 0, 0, 64, 64)
   
    #if p2.value() == 1 and p1.value() == 1 and p3.value() == 1 and Pause < 400:    
     #   display.draw_image('sort.raw', 0, 0, 64, 64)
    if rt == 0:
        display.draw_image('rightturn.raw', 0, 0, 128, 128)
        Pause = 0
        
    if rt == 1 and ttr == 1:
        display.draw_image('ss.raw', 0, 0, 128, 128)
        ttr = 0
    
    if lt == 0:
        display.draw_image('leftturn.raw', 0, 0, 128, 128)
        Pause = 0
    if lt == 1 and ttl == 1:
        display.draw_image('ss.raw', 0, 0, 128, 128)
        ttl = 0
    if lb == 0:
        display.draw_image('kortlys.raw', 0, 0, 64, 64)
    if hb == 0:
        display.draw_image('langlys.raw', 0, 0, 64, 64)    
    if oi == 0:
        display.draw_image('olie.raw', 64, 0, 64, 64)
    #if p5.value() == 1 and p1.value() == 1 and p3.value() == 1:
     #   display.draw_image('sort.raw', 64, 0, 64, 64)    
    if bt == 0:
        display.draw_image('batteri.raw', 0, 64, 64, 64)
    #if p6.value() == 1 and p1.value() == 1 and p3.value() == 1:
     #   display.draw_image('sort.raw', 0, 64, 64, 64)
    if ne == 0:
        display.draw_image('neutral.raw', 64, 64, 64, 64)
    #if p4.value() == 1 and p1.value() == 1 and p3.value() == 1:
     #   display.draw_image('sort.raw', 64, 64, 64, 64)
    # Attempt to set framerate to 30 FPS
  
