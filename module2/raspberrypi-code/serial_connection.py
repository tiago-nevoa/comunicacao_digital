import serial
import os 

# Configure the serial connection
ser = serial.Serial('/dev/ttyS0', 9600)  # Replace '/dev/ttyUSB0' with the appropriate device file and baud rate
while 1:
# Write data to the serial port
    data = "Hello, World, Serial Receiver" + os.linesep
    ser.write(data.encode())

# Close the serial connection
ser.close()        