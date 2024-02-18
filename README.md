# waveshare-pico-relay-b-demo
##Test code for waveshare pico relay b

# installation

Install micropython on your raspberry pi pico.  You can find documentation on this in many places online.

Install your raspberry pi pico W in your waveshare relay b.  You can buy a Waveshare pico relay b here:

[waveshare](https://www.waveshare.com/pico-relay-b.htm)

or here 

[amazon](https://www.amazon.com/Waveshare-Microcontroller-Dual-Core-Protective-Pico-Relay-B/dp/B0BLHGL7D4/ref=sr_1_1?crid=1C79FJXE0GUFA&dib=eyJ2IjoiMSJ9.j3Ue3chi982Fu9m3RZ6HTqvCciJK7jyQY70Z_xUCUeKXXKtZRdGsi5Y9loH1jP4wb6uQVqVSk2hNHVd0phWrX0TV9I9nogWDwOeaYM0d0g0XYpWBjVYdIoX4rjDInEIGGb5iNtPWQvLKBSNcuUKJEMCfmBMraWXxkPbEPKxuIgqsfqQCEpTjfDctaLeAO6RO-EfWPwlLQPAgkJDIP051V8Wz2-wTQLZkaAlOU1myU38.g61odZ93Bbg0Kv-Zr-Z_60XGcoxXuCJtTf-MVoY45rs&dib_tag=se&keywords=waveshare%2Brelay%2Bpico%2Bb&qid=1708227089&sprefix=waveshare%2Brelay%2Bpico%2Bb%2Caps%2C132&sr=8-1&th=1)

Edit main.py, and set your home wifi ssid and password.

```
WIFI_SSID="Your SSID"
WIFI_PASSWORD="Your Password"
```

Copy all the python files to your raspberry pi pico W.  I used thonny for this

open the "main.py file and press "run" in thonny.  It might be necessary to click the "stop" button in thonny first.

Once running it will immediately try to connect to your wifi.  While it is trying to get connected, the onboard green LED will light up on the
Pi Pico.  Once connected to your wifi, the led will turn off.

If you're looking at the thonny shell output, you'll see that it prints several ip addresses,  The first ip address contains the ip address of the
pi pico.  Point your browser at that ip address, and you should see a web form where you can turn on/off the relays on the waveshare
pico relay b board.  

When you turn on or off one or more relays, the buzzer will beep and the neopixel led on the waveshare board will glow bright cyan.

Now that you've copied all the files and tested, you can disconnect the waveshare from your computer and plug it in using a 
usb power supply and access it over a the same ip, provided your wifi system tries to keep client ip's the same.

