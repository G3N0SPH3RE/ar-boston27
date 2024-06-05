###### snap7 attempt ##########
# import snap7
# from snap7.util import set_bool, get_bool

# # PLC connection details
# plc_ip = "11.200.0.193"
# rack = 0
# slot = 1

# # Create a Snap7 client
# client = snap7.client.Client()

# # Connect to the PLC
# #client.connect(plc_ip, rack, slot)
# client.connect(11.200.0.19, rack, slot)

# # Toggle the light on channel 6
# while True:
#     # Read the current state of the light
#     light_state = get_bool(client.read_area(snap7.areas.MK, 0, 6, 1), 0)
    
#     # Toggle the light state
#     set_bool(client.read_area(snap7.areas.MK, 0, 6, 1), 0, not light_state)
    
#     # Write the new state to the PLC
#     client.write_area(snap7.areas.MK, 0, 6, client.read_area(snap7.areas.MK, 0, 6, 1))
    
#     # Wait for a short time before toggling the light again
#     time.sleep(1)

###### pyprofi ?? #########
import time
from pyprofinet.client import PROFINETClient
from pyprofinet.data_types import IODataItem

# Cognex 260 camera details
camera_ip = "11.200.0.193"
camera_station_name = "Cognex260"

# Create a PROFINET client
client = PROFINETClient()

try:
    # Discover the Cognex 260 camera on the network
    devices = client.discover_devices()
    camera_device = next((d for d in devices if d.station_name == camera_station_name), None)
    if not camera_device:
        print(f"Cognex 260 camera not found on the network.")
        exit()

    # Establish a PROFINET connection to the camera
    client.connect(camera_device)
    print(f"Connected to Cognex 260 camera at {camera_ip}")

    # Example: Read a data item from the camera
    data_item = IODataItem(index=0, length=2)
    while True:
        # Read the data item from the camera
        values = client.read_io_data([data_item])
        print(f"Camera data item value: {values[0]}")

        # Wait for 1 second before reading again
        time.sleep(1)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Disconnect from the camera
    client.disconnect()
    print("Disconnected from Cognex 260 camera.")
