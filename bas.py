import time
import board
import neopixel
import signal
import sys
import argparse

brightness = 0.2
color = (0, 0, 255)
slide_wait = 0.05
blink_wait = 0.5
block_size = 3

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
    pixel_pin, num_pixels, brightness=brightness, auto_write=False, pixel_order=ORDER
)

def slide_pattern():
    for i in range(0, num_pixels, block_size):
        pixels.fill((0, 0, 0))
        for j in range(block_size):
            if i + j < num_pixels:
                pixels[i + j] = color
        pixels.show()
        time.sleep(slide_wait)
    for i in range(num_pixels - block_size, -1, -block_size):
        pixels.fill((0, 0, 0))
        for j in range(block_size):
            if i + j < num_pixels:
                pixels[i + j] = color
        pixels.show()
        time.sleep(slide_wait)

def blink_pattern():
    pixels.fill((0, 0, 0))
    for i in range(block_size):
        pixels[i] = color
    pixels.show()
    time.sleep(blink_wait)
    pixels.fill((0, 0, 0))
    for i in range(num_pixels - block_size, num_pixels):
        pixels[i] = color
    pixels.show()
    time.sleep(blink_wait)

def main_slide():
    while True:
        slide_pattern()

def main_blink():
    while True:
        blink_pattern()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', choices=['slide', 'blink'])
    args = parser.parse_args()
    if args.pattern == 'slide':
        main_slide()
    elif args.pattern == 'blink':
        main_blink()
