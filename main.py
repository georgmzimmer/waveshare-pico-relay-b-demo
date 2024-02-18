import usocket
from relay import Relays
from templates import index
from wifi import check_wifi_connection
import gc
import machine
from buzzer import Buzzer
from led import NeoPixel
boot_led = machine.Pin("LED", machine.Pin.OUT)

WIFI_SSID="Mordor"
WIFI_PASSWORD="0liphaunt"

boot_led.value(1)
print("Frequency", int(machine.freq()/(1000*1000)), "Mhz")
#wlan = check_wifi_connection("Worthwhile", "58Q8xSNQRjrD4UwZ")

wlan = None
while not wlan:
    wlan = check_wifi_connection(WIFI_SSID, WIFI_PASSWORD)

boot_led.value(0)
print(wlan.ifconfig())


print("Waiting For Connection")
s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
#s.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(5)

led = NeoPixel()
buzzer = Buzzer()  

relays = Relays()

def parse_post_request(body):
    post_data = {}
    for pair in body.split('&'):
        if "=" in pair:
            key, value = pair.split('=')
            post_data[key] = value
    return post_data

try:
    while True:
        print(gc.mem_free())
        if gc.mem_free() < 100000:
            gc.collect()
        cl, addr = s.accept()
        print('client connected from', addr)
        cl_file = cl.makefile('rwb', 0)
        request = cl_file.readline().decode()
        print('Request:', request)
        
        if request.startswith('POST'):
            # Read the headers to find the content length
            content_length = 0
            while True:
                line = cl_file.readline().decode()
                if line.lower().startswith('content-length'):
                    content_length = int(line.split(': ')[1])
                if not line.strip():  # Header and body are separated by a blank line
                    break
            
            # Read the body of the request according to the content length
            post_body = cl_file.read(content_length).decode()
            
            # Now parse the POST data
            post_data = parse_post_request(post_body)
            print('POST data:', post_data)
            changed = False
            for ch in range(1,9):
                value = int(post_data.get(f"channel{ch}", 0))
                if value != relays.get_state(ch):
                    changed=True
                relays.set_state(ch, value)
                
            if changed:              
                led.flash(led.CYAN,0.2)
                buzzer.beep(1000, 0.2)
        else:
            print(cl.recv(1024))
            
        
        # Send a simple response
        data = index(relays)
        cl.send(f'HTTP/1.0 200 OK\r\nContent-type: text/html\r\nContent-length: {len(data)}\r\nConnection: close\r\n\r\n')
        cl.send(data)
        cl.close()
finally:
    s.close()    
