# Banner Light Testing

#########################################

# Initial test: toggle banner lights on and off for x time
# Then request user input for banner light state as pass or fail

# Erros should be flagged as needed.

# SERVER BANNER LIGHT = CH6; ERROR circuit breaker = CH16
# ROBOT BANNER LIGHT = CH7; ERROR circuit breaker = CH17

#########################################


import time
from machine import Pin

# Set up the IO-Link master pins
banner_1 = Pin(6, Pin.OUT)
banner_2 = Pin(7, Pin.OUT)

# Toggle the first pin for 10 seconds
start_time = time.time()
while time.time() - start_time < 10:
    banner_1.value(not banner_1.value())
    time.sleep(0.5)

# Prompt the user for feedback through PROFINET
feedback = input("Did the first test pass? (y/n) ")

if feedback.lower() == "y":
    print("First test passed!")
    first_test_result = "Pass"
else:
    print("First test failed.")
    first_test_result = "Fail"

# Toggle the second pin for 10 seconds
start_time = time.time()
while time.time() - start_time < 10:
    banner_2.value(not banner_2.value())
    time.sleep(0.5)

# Prompt the user for feedback on the second test
feedback = input("Did the second test pass? (y/n) ")

if feedback.lower() == "y":
    print("Second test passed!")
    second_test_result = "Pass"
else:
    print("Second test failed.")
    second_test_result = "Fail"

# Log the two answers
print("Logged results:")
print(f"First test result: {first_test_result}")
print(f"Second test result: {second_test_result}")

