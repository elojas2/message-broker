import socket
import sys

def main():

    if len(sys.argv)<3:
        print("use: python3 command_controler_broker.py -c <command>")
        return
    
    command = sys.argv[2]

    host = "127.0.0.1"
    port = 5000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    command_message = f"COMMAND {command}"
    client.send(command_message.encode())

    confirmation = client.recv(1024).decode()

    if confirmation == "CONFIRMATION_COMMANDS_SUCCESSFUL":
        data = client.recv(1024).decode()
        print(data)

if __name__ == "__main__":
    main()