from machine import Pin, ADC
import network
import random
import socket
import time


# Just making our internet connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('##########', '##########')

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
  if wlan.status() < 0 or wlan.status() >= 3:
    break
  max_wait -= 1
  print('waiting for connection...')
  time.sleep(1)
# Handle connection error
if wlan.status() != 3:
   raise RuntimeError('network connection failed')
else:
  print('connected')
  status = wlan.ifconfig()
  #print('ip = ' + status[0])

while True:
    ai = socket.getaddrinfo('###.###.##.##', 80) # Address of Web Server
    addr = ai[0][-1]

    # Create a socket and make a HTTP request
    s = socket.socket() # Open socket
    s.connect(addr)
    s.send(b"Anything") # Send request
    ss=str(s.recv(512)) # Store reply
    # Print what we received
    print(ss)
    # Set RGB LED here
    s.close()          # Close socket
    time.sleep(0.2)    # wait
