import serial
from fletcher_checksum import *

# Open the serial port
ser = serial.Serial('/dev/tty.usbserial-1433240', 9600)  # Replace with the appropriate baud rate

# Read data from the serial port
while 1:
    data = ser.readline()
    print(data.decode())  # Convert bytes to string and print
    receive_fletcher_checksum = ser.readline()
    print("fletcher checksum : " + receive_fletcher_checksum.decode())

# Close the serial port
ser.close()
