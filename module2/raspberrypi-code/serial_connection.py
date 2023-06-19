import serial
import os
from fletcher_checksum import calculate_fletcher_checksum


def write_to_port(input_data, error_check):
    # configure the serial connection
    ser = serial.Serial('/dev/ttyS0', 9600)

    # write data to the serial port
    data = str(input_data) + os.linesep
    print("result: " + data)
    ser.write(data.encode())

    # write error verification option to the serial port
    error_check_flag = str(error_check) + os.linesep
    ser.write(error_check_flag.encode())

    # compute errors using checksum if required
    if error_check:
        original_fletcher_checksum = str(calculate_fletcher_checksum(input_data)) + os.linesep
        # write checksum result to the serial port
        print("fletcher checksum : " + original_fletcher_checksum)
        ser.write(original_fletcher_checksum.encode())

    # close the serial connection
    ser.close()
