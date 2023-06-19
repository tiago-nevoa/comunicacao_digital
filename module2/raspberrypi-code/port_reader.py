import serial
import fletcher_checksum

# Open the serial port
ser = serial.Serial('/dev/tty.usbserial-1433240', 9600)  # Replace with the appropriate baud rate

# Read data from the serial port
while 1:
    data = ser.readline()
    print(data.decode())  # Convert bytes to string and print
    receive_fletcher_checksum = ser.readline()
    print("fletcher checksum : " + receive_fletcher_checksum.decode())
    confirm_fletcher_checksum = fletcher_checksum.verify_fletcher_checksum(data.decode(),
                                                                           receive_fletcher_checksum.decode())
    print("confirm fletcher checksum : " + confirm_fletcher_checksum)

# Close the serial port
ser.close()
