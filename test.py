#!/usr/bin/env python

from mitsi import HeatPump
from time import sleep
import logging

log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)
console = logging.StreamHandler()
log.addHandler(console)


# Create our HeatPump object, and start the serial connection
heatpump = HeatPump('/dev/serial0')
heatpump.connect()

# Function to watch the heatpump for 10 seconds, and print the current state
# when a valid packet is found.
def watch_heatpump():
  for i in range(10):
      heatpump.loop()
      if heatpump.valid:
          print(heatpump.to_dict())
      sleep(1)

# Let's see the current state of the heatpump.
watch_heatpump()

# Now set the heatpump's target temperature to 22, and the fan to cooling mode.
heatpump.set({'temp':'22', 'mode': 'COOL'})

# Check the changes have taken effect.
watch_heatpump()

# Now switch off the heatpump.
heatpump.set({'power': 'OFF'})

# And watch for the heatpump to switch off.
watch_heatpump()
