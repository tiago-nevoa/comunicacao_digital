import serial
import os 

def write_to_port(input_data):
    # configure the serial connection
    ser = serial.Serial('/dev/ttyS0', 9600)  
    # write data to the serial port
    for elem in input_data:
        data = str(elem) + os.linesep
        ser.write(data.encode())
    # close the serial connection
    ser.close()        