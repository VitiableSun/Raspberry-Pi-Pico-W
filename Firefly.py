from picozero import pico_led, LED, Switch
from time import sleep

pico_led.on()
sleep(1)
pico_led.off()

firefly = LED(13) # Use GP13
switch = Switch(18) # Use GP18

while True:
    if switch.is_closed: # Wires are connected
        firefly.on()
        sleep(0.5) # Stay on for half a second
        firefly.off()
        sleep(2.5) # Stay off for 2.5 seconds
    else: # Wires are not connected
        firefly.off()
        sleep(0.1) # Small delay