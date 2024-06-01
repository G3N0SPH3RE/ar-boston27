from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

# Create an instance of ModbusServer
server = ModbusServer("127.0.0.249", 12345, no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    state = [0]
    while True:
        server.data_bank.set_holding_registers(0, [int(uniform(0, 100))]) ## range (0, 100) append list to set more registers
        if state != server.data_bank.get_holding_registers(1): ## check if register has changed
            state = server.data_bank.get_holding_registers(1) ## update state
            print("Value of Register 1 has changed to " +str(state)) ## print new state
        sleep(0.5)

except:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")