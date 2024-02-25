import socket
import sys

def command():
    if len(sys.argv) < 3:
        print("Use: python3 broker_com.py -c <command>")
        return
    
    command = sys.argv[2]

    host = "127.0.0.1"
    port = 50055

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    if command == "LIST":
        #envia pro servidor
        client.send(f"LIST".encode())
        #recebe a confirmacao do servidor
        confirmation = client.recv(1024).decode()
        #se for confirmado, entra no if e imprime no terminal
        if confirmation == "COMMAND_ACCEPTED":
            data = client.recv(4096).decode()
            print("List of topics and subscribers:")
            print(data)

command()
