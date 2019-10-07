"""SSD1351 demo (bouncing boxes)."""
from machine import Pin, SPI
from random import random, seed
from ssd1351 import Display, color565
from utime import sleep_us, ticks_cpu, ticks_us, ticks_diff


class Box(object):
    """Bouncing box."""

    #def __init__(self, screen_width, screen_height, size, display, color):
       # """Initialize box.

       # self.size = size
       # self.w = screen_width
       # self.h = screen_height
       # self.display = display
       # self.color = color
        # Generate non-zero random speeds between -5.0 and 5.0
       # seed(ticks_cpu())
       # r = random() * 10.0
       # self.x_speed = 5.0 - r if r < 5.0 else r - 10.0
       # r = random() * 10.0
       # self.y_speed = 5.0 - r if r < 5.0 else r - 10.0

     #   self.x = self.w / 2.0
     #   self.y = self.h / 2.0
      #  self.prev_x = self.x
     #   self.prev_y = self.y


def test():
    """Bouncing box."""
    try:
        p1 = Pin(12, Pin.IN, Pin.PULL_UP)
        p2 = Pin(13, Pin.IN, Pin.PULL_UP)
        p3 = Pin(14, Pin.IN, Pin.PULL_UP)
        p4 = Pin(25, Pin.IN, Pin.PULL_UP)
        p5 = Pin(26, Pin.IN, Pin.PULL_UP)
        p6 = Pin(27, Pin.IN, Pin.PULL_UP)
        p7 = Pin(15, Pin.IN, Pin.PULL_UP)
        ind = 1# create input pin on GPIO2
        # get

        # Baud rate of 14500000 seems about the max
        spi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))
        display = Display(spi, dc=Pin(17), cs=Pin(5), rst=Pin(16))
        display.clear()



        while True:
            timer = ticks_us()

            p2.value()
            print(p2.value())
            #for b in boxes:
             #   b.update_pos()
              #  b.draw()

            if p1.value() == 0:
                display.draw_image('rightturn.raw', 0, 0, 128, 128)

            if p3.value() == 0:
                display.draw_image('leftturn.raw', 0, 0, 128, 128)

            if p7.value() == 0 and p1.value() == 1 and p3.value() == 1:
                display.draw_image('kortlys.raw', 0, 0, 64, 64)
            if p2.value() == 0 and p1.value() == 1 and p3.value() == 1:
                display.draw_image('langlys.raw', 0, 0, 64, 64)    
            if p5.value() == 0 and p1.value() == 1 and p3.value() == 1:
                display.draw_image('batteri.raw', 64, 0, 64, 64)
            if p5.value() == 1 and p1.value() == 1 and p3.value() == 1:
                display.draw_image('sort.raw', 64, 0, 64, 64)    
            if p6.value() == 0 and p1.value() == 1 and p3.value() == 1:
                display.draw_image('olie.raw', 0, 64, 64, 64)
            if p6.value() == 1 and p1.value() == 1 and p3.value() == 1:
                display.draw_image('sort.raw', 0, 64, 64, 64)
            if p4.value() == 0 and p1.value() == 1 and p3.value() == 1:
                display.draw_image('neutral.raw', 64, 64, 64, 64)
            if p4.value() == 1 and p1.value() == 1 and p3.value() == 1:
                display.draw_image('sort.raw', 64, 64, 64, 64)
            # Attempt to set framerate to 30 FPS
            timer_dif = 3333 - ticks_diff(ticks_us(), timer)
            if timer_dif > 0:
                sleep_us(timer_dif)

    except KeyboardInterrupt:
        display.cleanup()


test()
