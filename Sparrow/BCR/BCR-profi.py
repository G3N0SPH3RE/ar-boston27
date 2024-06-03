# import pyprofinet

# ### Create a PROFINET controller
# controller = pyprofinet.Controller()

# ### Connect to the Cognex 280 camera
# device = controller.add_device(
#     name="Cognex280",
#     ip_address="11.200.0.191", #-191 is a 260; -138 is the 280
#     device_type="Cognex280"
# )

# ### Read a data block from the camera
# data_block = device.read_data_block(block_number=1)
# print(f"Data block: {data_block}")

# ### Write a command to the camera
# command = b"SE8\r\n"
# device.write_data_block(block_number=2, data=command)


####### I did a thing... ####

from pyModbusTCP import utils
from pyModbusTCP.client import ModbusClient


scanner_ip_address = "11.200.0.193"

mb_client = ModbusClient(scanner_ip_address)
mb_client.open()

print("ModbusTCP Connected = {}".format(mb_client.is_open))

if mb_client.is_open:
    status_block = mb_client.read_holding_registers(5000)[0]
    print("Status Block = {}".format(status_block))
    print("Status Block Bits = {}".format(utils.get_bits_from_int(status_block)))
    mb_client.close()
    print("ModbusTCP Connected = {}".format(mb_client.is_open))