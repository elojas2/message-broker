import sys
import socket

def cennection():
    
    #host e porta
    host = "127.0.0.1"
    port = 50055

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))