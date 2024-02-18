import array
import time
from machine import Pin, PWM
import rp2
import _thread
    

LED_PIN_NUM = 13

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1).side(0)[T3 - 1]
    jmp(not_x, "do_zero").side(1)[T1 - 1]
    jmp("bitloop").side(1)[T2 - 1]
    label("do_zero")
    nop().side(0)[T2 - 1]
    wrap()
        
# Initialize relay IO and configure RGB lights
class NeoPixel(object):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)
    WHITE = (255, 255, 255)    


    def __init__(self, pin=LED_PIN_NUM, num=1, brightness=0.2):
        self.pin = pin
        self.num = num
        self.brightness = brightness

        # Create the StateMachine with the ws2812 program, outputting on pin
        self.sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(pin))
        # Start the StateMachine, it will wait for data on its FIFO.
        self.sm.active(1)
        # Display a pattern on the LEDs via an array of LED RGB values.
        self.ar = array.array("I", [0 for _ in range(self.num)])


    # The RGB output
    def pixels_show(self):
        dimmer_ar = array.array("I", [0 for _ in range(self.num)])
        for i, c in enumerate(self.ar):
            r = int(((c >> 8) & 0xFF) * self.brightness)
            g = int(((c >> 16) & 0xFF) * self.brightness)
            b = int((c & 0xFF) * self.brightness)
            dimmer_ar[i] = (g << 16) + (r << 8) + b
        self.sm.put(dimmer_ar, 8)

    # data conversion
    def pixels_set(self, i, color):
        self.ar[i] = (color[1] << 16) + (color[0] << 8) + color[2]

    # Single color output
    def pixels_fill(self, color):
        for i in range(len(self.ar)):
            self.pixels_set(i, color)

    # status lamp
    def flash(self, color, duration=0.5):
        self.pixels_fill(color)
        self.pixels_show()
        time.sleep(duration)
        self.pixels_fill(self.BLACK)
        self.pixels_show()

    
        
#flasher(NeoPixel.GREEN,1)    
