import serial

# Open the serial port
ser = serial.Serial('/dev/tty.usbserial-1433240', 9600)  # Replace with the appropriate baud rate

# Read data from the serial port
while 1:
  data = ser.readline()
  print(data.decode())  # Convert bytes to string and print

# Close the serial port
ser.close()