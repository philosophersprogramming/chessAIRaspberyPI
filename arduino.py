import serial
import time

# Open a serial connection to the Arduino
arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with the appropriate port for your system

# Wait for the serial connection to be established
time.sleep(2)

# Send data to the Arduino
data_to_send = b'Hello Arduino\n'  # Convert string to bytes
arduino.write(data_to_send)

# Close the serial connection
arduino.close()
