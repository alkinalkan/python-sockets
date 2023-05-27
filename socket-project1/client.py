from base64 import encode
import socket
import time


# Definition of host and port names and networks
host_name = "localhost"
port_name = 7777

# Communication channel creation by combining IP and port number
# Creating a socket / Connecting host name and port to the socket
internet_socket = socket.socket()
internet_socket.connect((host_name,port_name))

# Print to indicate that a connection is established
print("{}:{} connection established.".format(host_name,port_name))

# Since the first action will start from the client, a message needs to be sent
message = input("-->")
print("Waiting for the server...")


while message != "exit":
    internet_socket.send(message.encode())
    coming_data = internet_socket.recv(1024).decode()

    print("SERVER: " + coming_data)

    message = input("-->")
    print("Waiting for the server...")  # Message indicating the transition to the server part after the input.

internet_socket.close()
