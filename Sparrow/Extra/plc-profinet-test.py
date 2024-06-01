import snap7
from snap7.util import set_bool, get_bool

# PLC connection details
plc_ip = "11.200.0.19"
rack = 0
slot = 1

# Create a Snap7 client
client = snap7.client.Client()

# Connect to the PLC
#client.connect(plc_ip, rack, slot)
client.connect(11.200.0.19, rack, slot)

# Toggle the light on channel 6
while True:
    # Read the current state of the light
    light_state = get_bool(client.read_area(snap7.areas.MK, 0, 6, 1), 0)
    
    # Toggle the light state
    set_bool(client.read_area(snap7.areas.MK, 0, 6, 1), 0, not light_state)
    
    # Write the new state to the PLC
    client.write_area(snap7.areas.MK, 0, 6, client.read_area(snap7.areas.MK, 0, 6, 1))
    
    # Wait for a short time before toggling the light again
    time.sleep(1)
