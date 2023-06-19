import serial
import ast
from fletcher_checksum import verify_fletcher_checksum

# open the serial port
ser = serial.Serial('/dev/tty.usbserial-1433240', 9600)

while 1:
    # read data from the serial port
    data = ser.readline()
    print(data.decode())

    # read error verification option from the serial port
    error_detection = ser.readline()
    print(error_detection.decode())

    if error_detection == 'True':
        # read original checksum result from the serial port
        original_checksum = int(ser.readline())
        print("fletcher checksum : " + original_checksum.decode())

        # verify if the checksum of the original data matches the one of the transmitted data
        data_array = ast.literal_eval(data.decode())
        print(data_array)
        print("fletcher checksum validation: ", verify_fletcher_checksum(data_array, original_checksum))

# close the serial port
ser.close()
