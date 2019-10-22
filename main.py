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
Pauseplus = 0  #
x = 7          #
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
tlb = 0
thb = 0
trt = 0
tlt = 0
tbt = 0
tne = 0
toi = 0
while True:
    
    if lb == 0 or hb == 0:
        Pause += 1
    
    x += xspeed
    y += yspeed    
    
    if y > 63 or y < 2:
        yspeed *= -1

    if x > 63 or x < 2:
        xspeed *= -1
        
    if p7.value() == 1: #
        lb = 1          #
    if p7.value() == 0: #
        lb = 0          #  Low beam
        hb = 1          #
        rt = 1          #
        lt = 1          #
        tlb = 1         #
    
    if p2.value() == 1: #
        hb = 1          #
    if p2.value() == 0: #
        hb = 0          # High beam
        lb = 1          #
        rt = 1          #
        lt = 1          #
        thb = 1         #
    
    if p5.value() == 0: #
        oi = 0          #
        rt = 1          #  Oile
        lt = 1          # 
        toi = 1         #
    if p5.value() == 1: #   
        oi = 1          #    
        
    if p6.value() == 0: #
        bt = 0          #
        rt = 1          # Battery
        lt = 1          #
        tbt = 1         #
    if p6.value() == 1: #   
        bt = 1          #
        
    if p4.value() == 0: #
        ne = 0          #
        rt = 1          # Neutral
        lt = 1          # 
        tne = 1         #
    if p4.value() == 1: #   
        ne = 1          #    
        
    if p1.value() == 0: #
        rt = 0          #
        lt = 1          #
        lb = 1          #
        hb = 1          #
        oi = 1          # Right turn
        bt = 1          #
        ne = 1          #
        trt = 1         #
    if p1.value() == 1: #
        rt = 1          #
        
    if p3.value() == 0: #
        lt = 0          #
        rt = 1          #
        lb = 1          #
        hb = 1          #
        oi = 1          # Left turn
        bt = 1          #
        ne = 1          #
        tlt = 1         #
    if p3.value() == 1: #   
        lt = 1          #
    
    if rt == 0:
        display.draw_image('rightturn.raw', 0, 0, 128, 128)
        Pause = 0
        
    if rt == 1 and trt == 1:
        display.draw_image('ss.raw', 0, 0, 128, 128)
        trt = 0
    
    if lt == 0:
        display.draw_image('leftturn.raw', 0, 0, 128, 128)
        Pause = 0
    if lt == 1 and tlt == 1:
        display.draw_image('ss.raw', 0, 0, 128, 128)
        tlt = 0
    if lb == 0 and Pause < 1800:
        display.draw_image('lb.raw', 0, 0, 64, 64)
        
    if hb == 0 and Pause < 1800:
        display.draw_image('hb.raw', 0, 0, 64, 64)    
    
    if oi == 0:
        display.draw_image('ol.raw', 64, 0, 64, 64)
        Pause = 0
    if oi == 1 and toi == 1:
        display.draw_image('sort.raw', 64, 0, 64, 64)
        toi = 0
    
    if bt == 0:
        display.draw_image('bt.raw', 0, 64, 64, 64)
        Pause = 0
    if bt == 1 and tbt == 1:
        display.draw_image('sort.raw', 0, 64, 64, 64)
        tbt = 0
    
    if ne == 0:
        display.draw_image('nt.raw', 64, 64, 64, 64)
        Pause = 0
    if ne == 1 and tne == 1:
        display.draw_image('sort.raw', 64, 64, 64, 64)
        tne = 0
    
    if lb == 0 and Pause > 1800:
        display.draw_image('lb.raw', x, y, 64, 64)
    if lb == 1 and tlb == 1:
        display.draw_image('ss.raw', 0, 0, 128, 128)
        tlb = 0
        Pause = 0
        
    if hb == 0 and Pause > 1800:
        display.draw_image('hb.raw', x, y, 64, 64)
    if hb == 1 and thb == 1:
        display.draw_image('ss.raw', 0, 0, 128, 128)
        thb = 0
        Pause = 0
  
