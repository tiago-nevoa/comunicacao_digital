import serial
import ast
from fletcher_checksum import verify_fletcher_checksum

# open the serial port
ser = serial.Serial('/dev/tty.usbserial-1433240', 9600)

while 1:
    # read data from the serial port
    data = ser.readline().decode()
    print(data)

    # Open the file in write mode
    file = open("data_with_out_error.txt", "w")
    # Write content to the file
    file.write(data)
    # Close the file
    file.close()

    # read error verification option from the serial port
    error_detection = ser.readline().decode().strip()
    print("Error Detection : " + error_detection)

    if error_detection == "True":
        # read original checksum result from the serial port
        original_checksum = int(ser.readline().decode())
        print("fletcher checksum : ", original_checksum)

        # verify if the checksum of the original data matches the one of the transmitted data
        data_array = ast.literal_eval(data)

        # # force isolate error on data
        # data_array[6] = 0
        # # Open the file in write mode
        # file = open("data_with_isolate_error.txt", "w")
        # # Write content to the file
        # file.write(str(data_array))
        # # Close the file
        # file.close()

        # # force burst error on data
        # for i in range(6, len(data_array)):
        #     data_array[i] = 0
        #
        # # Open the file in write mode
        # file = open("data_with_burst.txt", "w")
        # # Write content to the file
        # file.write(str(data_array))
        # # Close the file
        # file.close()

        print(data_array)
        print("fletcher checksum validation: ", verify_fletcher_checksum(data_array, original_checksum))

# close the serial port
ser.close()
