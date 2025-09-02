import board
import time
import busio
import displayio
from adafruit_gc9a01a import GC9A01A
from fourwire import FourWire
from vectorio import Circle
from adafruit_display_text.bitmap_label import Label
import terminalio
import adafruit_imageload

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

# Load the sprite sheet (bitmap)
sprite_sheet, palette = adafruit_imageload.load("/eyeball64x60.bmp", bitmap=displayio.Bitmap,palette=displayio.Palette)

# Create a sprite (tilegrid)
sprite = displayio.TileGrid(sprite_sheet, pixel_shader=palette, width = 1, height = 1, tile_width = 64, tile_height = 60)

# Create a Group to hold the sprite
group = displayio.Group(scale=1)

# Add the sprite to the Group
group.append(sprite)

# Add the Group to the Display
display.root_group = group

# Set sprite range (display is 240x240 bmp is 64x60)
bmp_x_w = 64
bmp_y_h = 60
display_w = 240
display_h = 240
x_min = 0
x_max = display_w - bmp_x_w
x_mid = int((x_max+x_min)/2)
y_min = 0
y_max = display_h - bmp_y_h
y_mid = int((y_max+y_min)/2)

# set eye movement speeds
move_slow = 0.04
move_fast = 0.01

# set sprite starting position
curr_x = x_mid
curr_y = y_mid

group.x = curr_x
group.y = curr_y

# functions
def look(curr_x, direction, wait):
    if direction == "L":
        end = x_min
    elif direction == "R":
        end = x_max
    else:
        end = x_mid
    if end > curr_x:
        rd = 1
    else:
        rd = -1
    for i in range (curr_x,end,rd):
        group.x = i
        time.sleep(wait)
    return(end)
    

while True:
    curr_x=look(curr_x,"L",move_slow)
    curr_x=look(curr_x,"R",move_fast)
    curr_x=look(curr_x,"M",move_slow)
