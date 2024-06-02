import pyprofinet

### Create a PROFINET controller
controller = pyprofinet.Controller()

### Connect to the Cognex 280 camera
device = controller.add_device(
    name="Cognex280",
    ip_address="11.200.0.191", #-191 is a 260; -138 is the 280
    device_type="Cognex280"
)

### Read a data block from the camera
data_block = device.read_data_block(block_number=1)
print(f"Data block: {data_block}")

### Write a command to the camera
command = b"SE8\r\n"
device.write_data_block(block_number=2, data=command)
