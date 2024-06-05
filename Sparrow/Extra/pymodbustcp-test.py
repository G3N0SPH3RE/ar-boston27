##### SERVER ####
# from pyModbusTCP.server import ModbusServer, DataBank
# from time import sleep
# from random import uniform

# # Create an instance of ModbusServer
# server = ModbusServer("127.0.0.191", 5353, no_block=True)

# try:
#     print("Start server...")
#     server.start()
#     print("Server is online")
#     state = [0]
#     while True:
#         server.data_bank.set_holding_registers(0, [int(uniform(0, 100))]) ## range (0, 100) append list to set more registers
#         if state != server.data_bank.get_holding_registers(1): ## check if register has changed
#             state = server.data_bank.get_holding_registers(1) ## update state
#             print("Value of Register 1 has changed to " +str(state)) ## print new state
#         sleep(0.5)

# except:
#     print("Shutdown server ...")
#     server.stop()
#     print("Server is offline")


####### Client ###########
from pyModbusTCP.client import ModbusClient
from time import sleep
from random import uniform

client = ModbusClient(host="127.0.0.154", port=23)

try:
    # Connect to the Modbus server
    if not client.open():
        print("Unable to connect to the Modbus server")
        exit()

    print("Connected to the Modbus server")

    while True:
        # Read the value of register 1
        reg_1_value = client.read_holding_registers(1, 1)[0]
        print(f"Value of Register 1: {reg_1_value}")

        # Write a random value to register 0
        random_value = int(uniform(0, 100))
        client.write_single_register(0, random_value)
        print(f"Wrote value {random_value} to Register 0")

        sleep(0.5)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection to the Modbus server
    client.close()
    print("Disconnected from the Modbus server")
