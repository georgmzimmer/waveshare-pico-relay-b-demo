import time
import network

# Function to reconnect WiFi
def reconnect_wifi(wlan, ssid, password, max_wait=10):
    wlan.active(True)
    wlan.config(pm = 0xa11140)
    wlan.connect(ssid, password)
    for _ in range(max_wait):
        if wlan.isconnected():
            print("Wifi is re-connected")
            return wlan
        time.sleep(1)
    print("Failed to reconnect WiFi.")
    return None

def check_wifi_connection(ssid, password):
    print("Wifi setup")
    wlan = network.WLAN(network.STA_IF)
    reconnect_wifi(wlan, ssid, password)
    if wlan.isconnected():
        print("WiFi is connected.")
        return wlan
    else:
        print("WiFi is not connected.")
        return reconnect_wifi(wlan, ssid, password)