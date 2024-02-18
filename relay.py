import array, time
from machine import Pin



class RelayPin(Pin):
    def __init__(self, pin, *args, **kwargs):
        super().__init__(pin, *args, **kwargs)
        self.pin = pin
        
    def checked(self):
        if int(self.value()):
            return "checked"
        return ""



class Relays(object):
    ON = True
    OFF = False

    def __init__(self):
        self.ch1 = RelayPin(21, Pin.OUT)
        self.ch2 = RelayPin(20, Pin.OUT)
        self.ch3 = RelayPin(19, Pin.OUT)
        self.ch4 = RelayPin(18, Pin.OUT)
        self.ch5 = RelayPin(17, Pin.OUT)
        self.ch6 = RelayPin(16, Pin.OUT)
        self.ch7 = RelayPin(15, Pin.OUT)
        self.ch8 = RelayPin(14, Pin.OUT)
        self.channels = [self.ch1, self.ch2, self.ch3, self.ch4, self.ch5, self.ch6, self.ch7, self.ch8]

    def get_channel(self, channel):
        if channel < 1 or channel > 8:
            raise Exception("channel must be 1 to 8")
        return self.channels[channel - 1]

    @property
    def channel1(self):
        return self.get_channel(1)

    @channel1.setter
    def channel1(self, value):
        self.set_state(1, value)

    @property
    def channel2(self):
        return self.get_channel(2)

    @channel2.setter
    def channel2(self, value):
        self.set_state(2, value)

    @property
    def channel3(self):
        return self.get_channel(3)

    @channel3.setter
    def channel3(self, value):
        self.set_state(3, value)

    @property
    def channel4(self):
        return self.get_channel(4)

    @channel4.setter
    def channel4(self, value):
        self.set_state(4, value)

    @property
    def channel5(self):
        return self.get_channel(5)

    @channel5.setter
    def channel5(self, value):
        self.set_state(5, value)

    @property
    def channel6(self):
        return self.get_channel(6)

    @channel6.setter
    def channel6(self, value):
        self.set_state(6, value)

    @property
    def channel7(self):
        return self.get_channel(7)

    @channel7.setter
    def channel7(self, value):
        self.set_state(7, value)

    @property
    def channel8(self):
        return self.get_channel(8)

    @channel8.setter
    def channel8(self, value):
        self.set_state(8, value)

    def get_state(self, channel):
        ch = self.get_channel(channel)
        return ch.value()

    def set_state(self, channel, state):
        ch = self.get_channel(channel)

        if state:
            ch.high()
        else:
            ch.low()


    def set_all_state(self, state):
        for ch in self.channels:
            if state:
                ch.high()
            else:
                ch.low()


