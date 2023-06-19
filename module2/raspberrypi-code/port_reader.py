import serial
import ast
from fletcher_checksum import *

# Open the serial port
ser = serial.Serial('/dev/tty.usbserial-1433240', 9600)

# Read data from the serial port
while 1:
    data = ser.readline()
    print(data.decode())

    received_fletcher_checksum = ser.readline()
    print("fletcher checksum : " + received_fletcher_checksum.decode())

    data_array = ast.literal_eval(data.decode())
    ("fletcher checksum validation: " + verify_fletcher_checksum(data_array, int(received_fletcher_checksum)))


# Close the serial port
ser.close()
