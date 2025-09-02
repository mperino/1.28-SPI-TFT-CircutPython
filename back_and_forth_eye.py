#  TFT Display: https://amzn.to/45YK8Vn
#  on Pico 2 using display I/O drawing and moving Circles, changing circle Diameter
#  https://learn.adafruit.com/circuitpython-display-support-using-displayio/library-overview
import board
import time
import busio
import displayio
from adafruit_gc9a01a import GC9A01A
from fourwire import FourWire
from vectorio import Circle
from adafruit_display_text.bitmap_label import Label
import terminalio

# Release displays to ensure a clean start
displayio.release_displays()

# Define SPI pins (adjust according to your wiring)
tft_clk = board.GP10   #SDA
tft_mosi = board.GP11  #SCL
tft_rst = board.GP12   #
tft_dc = board.GP13    #
tft_cs = board.GP14    #
tft_bl = board.GP15 # Optional, set to None if not controlling backlight

# Initialize SPI bus
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)

# Initialize display bus
display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
# Initialize GC9A01 display
display = GC9A01A(display_bus, width=240, height=240)

#
# Make the display context
main_group = displayio.Group()
display.root_group = main_group

bg_bitmap = displayio.Bitmap(240, 240, 2)
color_palette = displayio.Palette(3)
color_palette[0] = 0xDCFF00  # Nuclear Yellow Green
color_palette[1] = 0xAA0088  # Purple
color_palette[2] = 0xBF0000  # Red


bg_sprite = displayio.TileGrid(bg_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)

inner_circle = Circle(pixel_shader=color_palette, x=120, y=120, radius=70, color_index=2)
main_group.append(inner_circle)
mid = 120
dist = 85 * 2
dir = int(1)
start = int(mid - dist /2)
end = int(mid + dist /2)
while True:
    print (start, end, dir)
    for i in range(start,end,dir):
        time.sleep(0.01)
        inner_circle.x=i
        if i / 10 == int(i/10):
            inner_circle.radius=65
            time.sleep(.1)
            inner_circle.radius=70
        print (i)
    dir = dir * -1
    temp = start
    start = end
    end = temp

while True:
    pass # Keep the display active
