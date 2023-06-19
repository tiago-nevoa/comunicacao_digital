import serial
import os
from fletcher_checksum import *

def write_to_port(input_data, error_check):

    # configure the serial connection
    ser = serial.Serial('/dev/ttyS0', 9600)

    # write data to the serial port
    data = str(input_data) + os.linesep
    print("result: " + data)
    ser.write(data.encode())

    e_c_trans = str(error_check) + os.linesep
    ser.write(e_c_trans)

    # compute errors using checksum if required
    if error_check:
        c_f_c = str(calculate_fletcher_checksum(input_data)) + os.linesep
        # write checksum result to the serial port
        print("fletcher checksum : " + c_f_c)
        ser.write(c_f_c.encode())

    # close the serial connection
    ser.close()
