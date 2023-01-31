import time
import board
import neopixel
import signal
import sys
import argparse

def handle_keyboard_interrupt(signum, frame):
    pixels.fill((0, 0, 0,))
    pixels.show()
    print("exiting")
    sys.exit(0)
    
signal.signal(signal.SIGINT, handle_keyboard_interrupt)
                              
pixel_pin = board.D18
num_pixels = 60
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

color = (0, 255, 0)
slide_wait = 0.05
blink_wait = 0.5

def slide_pattern():
    for i in range(num_pixels):
        pixels.fill((0, 0, 0))
        pixels[i] = color
        pixels.show()
        time.sleep(slide_wait)
    for i in range(num_pixels-1, -1, -1):
        pixels.fill((0, 0, 0))
        pixels[i] = color
        pixels.show()
        time.sleep(slide_wait)

def blink_pattern():
    while True:
        pixels.fill((0, 0, 0))
        pixels[0] = color
        pixels.show()
        time.sleep(blink_wait)
        pixels.fill((0, 0, 0))
        pixels[num_pixels - 1] = color
        pixels.show()
        time.sleep(blink_wait)

def main_slide():
    while True:
        slide_pattern()

def main_blink():
    blink_pattern()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', choices=['slide', 'blink'])
    args = parser.parse_args()
    if args.pattern == 'slide':
        main_slide()
    elif args.pattern == 'blink':
        main_blink()
