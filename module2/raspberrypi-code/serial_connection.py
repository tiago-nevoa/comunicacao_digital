import serial
import os
import fletcher_checksum

def write_to_port(input_data):
    # configure the serial connection
    ser = serial.Serial('/dev/ttyS0', 9600)  
    # write data to the serial port
    for elem in input_data:
        data = str(elem) + os.linesep
        ser.write(data.encode())
        c_f_c = fletcher_checksum.calculate_fletcher_checksum(data) + os.linesep
        print("fletcher checksum : " + c_f_c)
        ser.write(c_f_c.encode())
    # close the serial connection
    ser.close()        