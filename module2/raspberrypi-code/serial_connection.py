import serial
import os 

# Configure the serial connection
def write_to_port(input_data):
    ser = serial.Serial('/dev/ttyS0', 9600)  
    while 1:
    # Write data to the serial port
        data = input_data + os.linesep
        ser.write(data.encode())

    # Close the serial connection
    ser.close()        