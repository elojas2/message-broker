import socket
import sys

def main():
    if len(sys.argv) < 3:
        print("Use: python3 broker_com.py -c <command>")
        return
    
    command = sys.argv[2]

    host = "127.0.0.1"
    port = 50004

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    if command == "LIST":
        client.send(f"LIST".encode())
        data = client.recv(4096).decode()
        print("List of topics and subscribers:")
        print(data)

if __name__ == "__main__":
    main()
