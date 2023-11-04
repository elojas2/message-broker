import socket
import sys

def main():
    if len(sys.argv) < 3:
        print("Use: python3 broker_com.py -c <command>")
        return

    command = sys.argv[2]
    host = "127.0.0.1"
    port = 12246
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    command_message = f"COMMAND {command}"
    client.send(command_message.encode())
    confirmation = client.recv(1024).decode()

    if confirmation == "COMMAND_CONFIRMATION_ACK":
        data = client.recv(1024).decode()
        print(data)

if __name__ == "__main__":
    main()
