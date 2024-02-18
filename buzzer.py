import time
from machine import Pin, PWM


class Buzzer():
    MAX_VOLUME = 32768

    def __init__(self, pin=6):
        self.pin = pin
        self.pwm = PWM(Pin(pin))
        self.pwm.duty_u16(0)

    def beep(self, freq, duration, volume=MAX_VOLUME):
        self.pwm.freq(freq)
        self.pwm.duty_u16(volume)
        time.sleep(duration)
        self.pwm.duty_u16(0)

# Buzzer().beep(400,1,volume=300)
