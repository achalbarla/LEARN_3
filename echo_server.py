
import sys
import socket
import argparse
import codecs


from codecs import encode, decode
host = 'localhost'
data_payload = 4096
backlog = 5
def echo_server(port):
    """ A simple echo server """
# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enable reuse address/port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to the port
server_address = (host, port)
print ("Starting up echo server on %s port %s" %server_address)
sock.bind(server_address)
# Listen to clients, backlog argument specifies the max no. of queued connections
sock.listen(backlog)