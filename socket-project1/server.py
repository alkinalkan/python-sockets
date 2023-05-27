from email import message
from shutil import which
import socket
import time

# Definition of host and port names and networks
host_name = "localhost"
port_name = 7777

# Communication channel creation by combining IP and port number
# Creating a socket / Binding host name and port to the socket
internet_socket = socket.socket()
internet_socket.bind((host_name, port_name))
# For socket listening:
internet_socket.listen(1)

# socket.accept method receives the connection and address, which are used for further operations.
connection, address = internet_socket.accept()

# Print to indicate that a connection is established
print(str(address) + " connection established.")

# Main loop: continuously checking for data from the client part.
# The coming_data part is converted to string for printing it on the console.
# The connection object has the recv method, which represents the return value object.
# It takes a certain byte size and then decodes it.
# It is sent as encoded and received by decoding.

while True:
    while True:
        try:
            coming_data = str(connection.recv(1024).decode())
            print("The client sent: " + coming_data)
            break
        except ConnectionResetError:  # If an error occurs, reconnect and establish the connection again.
            time.sleep(2)
            connection, address = internet_socket.accept()
            print(str(address) + " connection established.")
    if coming_data == "exit":  # If "exit" is written, the program quits.
        break
    else:  # If a message wants to be sent to the other side (client side).
        message = input("-->")
        print("Waiting for the client...")  # Message indicating the transition to the client part after the input.
        connection.send(message.encode())  # The message is encoded (encrypted) and sent to the client.

# The first loop is for sending data (message) to the client.
# The second loop is for checking if there is any data (message) from the client.
# After the loops end, the connection is closed.
connection.close()
