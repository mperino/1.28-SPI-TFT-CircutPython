# Test/Demo Code for 1.28 Inch TFT LCD Display Module Round 240 x 240 Pixel RGB 65K Color GC9A01 Driver 4 Wire SPI on Pico 2W circutpython 9.2.8
# displays a yellow circular border, purple middle circle, and "Hello World!"
import board
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
tft_clk = board.GP10   #SCL
tft_mosi = board.GP11  #SDA
tft_rst = board.GP12   #RST
tft_dc = board.GP13    #DC
tft_cs = board.GP14    #CS
#GND to GND
#VCC to 3.3v


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
color_palette = displayio.Palette(2)
color_palette[0] = 0x00FF00  # Bright Green
color_palette[1] = 0xAA0088  # Purple

bg_sprite = displayio.TileGrid(bg_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)

inner_circle = Circle(pixel_shader=color_palette, x=120, y=120, radius=100, color_index=1)
main_group.append(inner_circle)

# Draw a label
text_group = displayio.Group(scale=2, x=50, y=120)
text = "Hello World!"
text_area = Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling
main_group.append(text_group)

while True:
    pass # Keep the display active
